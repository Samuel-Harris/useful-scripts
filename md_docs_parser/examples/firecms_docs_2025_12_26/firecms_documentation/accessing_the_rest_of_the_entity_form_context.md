### Accessing the rest of the entity (form context)
`context` gives you live access to:
- All current values (`context.values`)
- `context.setFieldValue(key, value)` to update any other field
- `context.save(values)` to trigger a save programmatically (rarely needed in fields)
- Metadata: `entityId`, `status` (new/existing/copy), `collection`, `openEntityMode`, `disabled`

This enables cross‑field logic (e.g. auto‑fill slug when title changes) or conditional disabling.

