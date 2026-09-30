## 8. Context loss between sessions
Work resumed from summaries; generators were lost and rebuilt; the same checks were re-derived.
**Cause:** everything lived in one conversation.
**Fix:** every artifact (brief, prereg, data dictionary, notebook, results JSON, page) is a file in a git repository; agents read from files, not from chat; the memory store holds only durable lessons and conventions.
