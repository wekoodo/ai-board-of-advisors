#!/usr/bin/env python3
"""Audit a folder-based routed context (ICM) layout.

Recognizes two valid Layer-2/3 shapes, not just one:

* Stage pipeline  -- a ``stages/`` directory of numbered, sequential stage
  contracts (Inputs/Process/Outputs). This is ICM as described in the paper.
* Reference library -- any directory of numbered ``NN-name/`` members each
  carrying a ``CONTEXT.md`` (e.g. ``advisors/``). A library is Layer-3
  reference material that a stage *selects from* by topic; it is NOT a broken
  pipeline. A project may have a pipeline, a library, both, or neither.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ENTRYPOINTS = [
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".cursor/rules",
]
ROUTERS = ["CONTEXT.md", "CONTEXT-MAP.md"]
STABLE_DIRS = ["_config", "shared", "references", "docs/agents"]
WORKING_DIRS = ["output", "outputs", "input", "inputs", "handoffs", "artifacts", "meetings"]
SKIP_DIRS = {".git", ".agents", ".claude", ".codex", "node_modules", "tmp", "__pycache__"}

STAGE_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
NUMBERED_RE = re.compile(r"^\d{2}[-_][a-z0-9][a-z0-9_-]*$")


@dataclass
class Finding:
    level: str
    message: str
    path: str | None = None


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def existing(root: Path, candidates: list[str]) -> list[Path]:
    return [root / candidate for candidate in candidates if (root / candidate).exists()]


def add(findings: list[Finding], level: str, message: str, path: Path | None = None, root: Path | None = None) -> None:
    findings.append(Finding(level=level, message=message, path=rel(path, root) if path and root else None))


def heading_names(text: str) -> set[str]:
    return {match.group(1).strip().lower() for match in STAGE_HEADING_RE.finditer(text)}


def has_heading(headings: set[str], name: str) -> bool:
    return any(heading == name.lower() or heading.startswith(name.lower() + " ") for heading in headings)


def numbered_members(directory: Path) -> list[Path]:
    """Direct child folders named NN-slug / NN_slug."""
    if not directory.is_dir():
        return []
    return sorted(c for c in directory.iterdir() if c.is_dir() and NUMBERED_RE.match(c.name))


def find_libraries(root: Path) -> list[tuple[Path, list[Path]]]:
    """Directories (other than stages/) whose children are numbered members.

    This is how a roster of personas/specialists (advisors/) is expressed in
    ICM: a Layer-3 library, selected from per run, not a sequential stage list.
    """
    libraries: list[tuple[Path, list[Path]]] = []
    for child in sorted(p for p in root.iterdir() if p.is_dir()):
        if child.name in SKIP_DIRS or child.name == "stages":
            continue
        members = numbered_members(child)
        if members:
            libraries.append((child, members))
    return libraries


def has_recursive_routing(directory: Path) -> bool:
    """A CONTEXT.md nested below the top of a reference area (footnote-4 pattern)."""
    if not directory.is_dir():
        return False
    for context in directory.rglob("CONTEXT.md"):
        if context.parent != directory:
            return True
    return False


def audit_stage(findings: list[Finding], stage: Path, root: Path) -> None:
    context = stage / "CONTEXT.md"
    if not context.exists():
        add(findings, "fail", "Stage is missing CONTEXT.md.", stage, root)
        return

    text = context.read_text(encoding="utf-8")
    headings = heading_names(text)
    missing = [name for name in ["Inputs", "Process", "Outputs"] if not has_heading(headings, name)]
    if missing:
        add(findings, "fail", f"Stage contract is missing required heading(s): {', '.join(missing)}.", context, root)
    else:
        add(findings, "ok", "Stage contract has Inputs, Process, and Outputs.", context, root)

    if not re.search(r"Layer\s*3|reference", text, re.IGNORECASE):
        add(findings, "warn", "Inputs do not clearly mark Layer 3 reference material.", context, root)
    if not re.search(r"Layer\s*4|working", text, re.IGNORECASE):
        add(findings, "warn", "Inputs do not clearly mark Layer 4 working artifacts.", context, root)
    if not has_heading(headings, "Verify"):
        add(findings, "warn", "Stage has no Verify section. Add one for cross-stage alignment checks when useful.", context, root)

    output = stage / "output"
    if output.exists() and output.is_dir():
        add(findings, "ok", "Stage output/ review gate found.", output, root)
    else:
        add(findings, "warn", "Stage has no output/ directory for reviewable handoffs.", stage, root)


def audit(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []

    if not root.exists():
        add(findings, "fail", "Project root does not exist.", root, root)
        return findings

    # Layer 0 / 1 / 3
    entrypoints = existing(root, ENTRYPOINTS)
    if entrypoints:
        add(findings, "ok", f"Layer 0 entrypoint found: {', '.join(rel(p, root) for p in entrypoints)}.")
    else:
        add(findings, "fail", "No Layer 0 entrypoint found. Expected AGENTS.md, CLAUDE.md, or a tool-specific equivalent.")

    routers = existing(root, ROUTERS)
    if routers:
        add(findings, "ok", f"Layer 1 router found: {', '.join(rel(p, root) for p in routers)}.")
    else:
        add(findings, "warn", "No Layer 1 router found. Add CONTEXT.md or CONTEXT-MAP.md when tasks need routed context.")

    stable_dirs = existing(root, STABLE_DIRS)
    if stable_dirs:
        add(findings, "ok", f"Layer 3 reference area found: {', '.join(rel(p, root) for p in stable_dirs)}.")
        for area in stable_dirs:
            if has_recursive_routing(area):
                add(findings, "ok", "Recursive Layer-3 routing found (a CONTEXT.md inside the reference area).", area, root)
    else:
        add(findings, "warn", "No obvious Layer 3 reference area found. Consider _config/, shared/, references/, or docs/agents/.")

    # Layer 2 shape A: a stages/ pipeline
    stages_root = root / "stages"
    has_pipeline = False
    if stages_root.exists():
        stage_dirs = sorted(p for p in stages_root.iterdir() if p.is_dir())
        numbered = [p for p in stage_dirs if NUMBERED_RE.match(p.name)]
        unnumbered = [p for p in stage_dirs if p not in numbered]
        if not numbered:
            add(findings, "fail", "stages/ exists but has no numbered stage folders like 01_research.", stages_root, root)
        else:
            has_pipeline = True
            add(findings, "ok", f"Stage pipeline found: {len(numbered)} numbered stage(s).", stages_root, root)
        for path in unnumbered:
            add(findings, "warn", "Stage folder is not numbered as NN_slug.", path, root)
        for stage in numbered:
            audit_stage(findings, stage, root)

    # Layer 2/3 shape B: numbered reference libraries (e.g. advisors/)
    libraries = find_libraries(root)
    for lib_dir, members in libraries:
        add(findings, "ok", f"Reference library found: {len(members)} numbered member(s) (Layer 3, selected per run).", lib_dir, root)
        if has_recursive_routing(lib_dir):
            add(findings, "ok", "Recursive Layer-3 routing found inside the library.", lib_dir, root)
        for member in members:
            if not (member / "CONTEXT.md").exists():
                add(findings, "warn", "Library member has no CONTEXT.md contract.", member, root)

    # Layer 4 working area
    working = [d for name in WORKING_DIRS for d in [root / name] if d.exists() and d.is_dir()]
    if working:
        add(findings, "ok", f"Layer 4 working area found: {', '.join(rel(d, root) for d in working)}.")

    # Overall shape note -- only when NEITHER pipeline nor library is present.
    if not has_pipeline and not libraries:
        add(
            findings,
            "info",
            "No stage pipeline or numbered reference library found. This is a valid "
            "context-only project (Layers 0-1[/3]). Add a stages/ pipeline for a sequential "
            "workflow, or a numbered library (e.g. advisors/) for a selected-per-run roster.",
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a routed Markdown context (ICM) architecture.")
    parser.add_argument("root", nargs="?", default=".", help="Project root to audit.")
    parser.add_argument("--json", action="store_true", help="Emit JSON findings.")
    args = parser.parse_args()

    findings = audit(Path(args.root))

    if args.json:
        print(json.dumps([finding.__dict__ for finding in findings], indent=2))
    else:
        for finding in findings:
            path = f" ({finding.path})" if finding.path else ""
            print(f"[{finding.level.upper()}] {finding.message}{path}")

    return 1 if any(finding.level == "fail" for finding in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
