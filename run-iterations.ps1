# Run Board of Advisors (v2) iterations sequentially via claude -p
#
# Each iteration is driven by a self-contained kickoff prompt in tmp/kickoff-iteration-NN.md
# and runs in a fresh, non-interactive session.
#
# Usage:
#   .\run-iterations.ps1            # run all 11 iterations (01 -> 11)
#   .\run-iterations.ps1 -Start 5   # resume from iteration 05 through 11
#   .\run-iterations.ps1 -Start 5 -End 8   # run iterations 05 through 08
#   .\run-iterations.ps1 -Only 8    # run a single iteration (e.g. to test/redo)
#   .\run-iterations.ps1 -Model sonnet -Effort high   # override model/effort
#
# -Model  pins the model for every iteration (default: opus). Accepts an alias
#         (opus, sonnet, haiku, fable, default, best) or a full id (e.g.
#         claude-opus-4-8), optionally with [1m] for extended context.
# -Effort pins the reasoning effort (default: max). One of: low|medium|high|xhigh|max.

param(
    [int]$Start = 1,
    [int]$End = 11,
    [int]$Only = 0,
    [string]$Model = "opus",
    [string]$Effort = "max"
)

if ($Only -gt 0) {
    $Start = $Only
    $End = $Only
}

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot

# Force UTF-8 when piping the prompt to claude. Windows PowerShell 5.1 defaults to
# US-ASCII for native-command pipelines, which would mangle non-ASCII characters
# (em dashes, arrows) in the kickoff files. UTF8Encoding($false) = no BOM.
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

Write-Host "Board of Advisors (v2) - running iterations $Start through $End"
Write-Host "Working directory: $projectRoot"
Write-Host "Model: $Model    Effort: $Effort"
Write-Host ""

for ($i = $Start; $i -le $End; $i++) {
    $padded = $i.ToString("00")
    $kickoffPath = Join-Path $projectRoot "tmp\kickoff-iteration-$padded.md"

    if (-not (Test-Path $kickoffPath)) {
        Write-Error "Kickoff file not found: $kickoffPath"
        exit 1
    }

    Write-Host "=========================================="
    Write-Host "Iteration $padded"
    Write-Host "=========================================="
    # The kickoff prompt is piped via stdin (NOT passed as a CLI argument). Windows
    # caps a command line at ~32K characters; the larger kickoffs exceed it, which
    # fails with "The filename or extension is too long". Piping has no such limit.
    #
    # --dangerously-skip-permissions allows file creation without per-tool prompts.
    # --model / --effort are pinned so a settings or env change cannot silently
    # change the model or reasoning effort mid-build (override via -Model / -Effort).
    Get-Content $kickoffPath -Raw | claude --dangerously-skip-permissions --model $Model --effort $Effort -p

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Iteration $padded exited with code $LASTEXITCODE - stopping."
        exit $LASTEXITCODE
    }

    Write-Host ""
    Write-Host "Iteration $padded complete."
    Write-Host ""
}

Write-Host "All iterations complete."
