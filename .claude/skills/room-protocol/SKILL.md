---
name: room-protocol
description: How the team communicates through the room/ directory and the file-ownership rule. Read at the start of every session.
---

# Room protocol

- The team's conversation is `room/`. Every request, answer, status and verdict is a note using templates/ROOM-NOTE.md, named `room/<owner>-<YYYY-MM-DD>-<slug>.md`.
- **Start every turn** by listing `room/` and reading every note whose `to` header names you that you have not answered; answer each with a note before other work. Record answered notes in `room/<owner>-answered.txt` (one path per line), which you own.
- **Ownership.** Each path has one owner (see README.md). You create and edit only your own paths. To comment on another agent's file, write a note to its owner; never edit it, never overwrite it, never "fix" it. The director sends back any turn that breaks this.
- **Point, don't paste.** Notes name file paths; they do not reproduce tables or long results.
- **Escalation.** If two agents disagree after one exchange, either writes an `escalation` note to the director; the referee's verdict stands unless the human overrules.
- **Status notes** end every phase: files produced, checks passed, open questions.
- **Gates.** Only the director writes gate messages to the human; specialists never address the human directly.
- **Version control.** The repository is mounted with push rights. The sandbox has no git identity, so every commit supplies it: `git -c user.name="Emily Birch" -c user.email="emily.a.l.birch@gmail.com" commit ...`. Specialists commit only their own files; the director commits room notes and pre-registrations and pushes main at the end of a phase; the editor pushes only `postN-draft` branches. Pull before pushing (`git pull --rebase origin main`).
