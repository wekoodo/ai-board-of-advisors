# `_inbox/` — Pre-Meeting Document Intake

Drop documents here that the board should have on hand for a meeting — entity
structures, contracts, spreadsheets, statements, anything an advisor may need to
read. Add them any time, between sessions.

**These documents are local-only.** Git ignores documents here and when the board moves them
into a meeting `inputs/` or entity `sources/` folder, even when you opt in to private sync.
Git tracks this README so the inbox exists on a fresh clone. Content sent to a cloud model
follows that provider's policies.

**What happens to them.** At the start of a meeting the board chair lists whatever
is waiting here, asks which files are relevant to that meeting, and **moves** the
ones you confirm into `meetings/<meeting>/inputs/` (`<YYYY-MM-DD-HHMM>-<topic-slug>` or
`<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>` — see `meetings/CONTEXT.md`). During in-depth entity
onboarding, confirmed sources move into that entity's profile `sources/` folder
instead — see `_config/setup/entity-onboarding.md`. Anything you don't pick stays
here for a future meeting.
