### Component contract (FieldProps)
Your component must at minimum:
1. Read the current `value` (it can be `undefined` or `null` for empty)
2. Call `setValue(newValue)` when the user changes it

Recommended good practices:
- Honor `disabled` / `isSubmitting`
- Show the label and error (use your own UI or `<FieldHelperText>` / built‑ins)
- Avoid heavy side effects on every keystroke (debounce network calls)

Full interface: [`FieldProps`](https://firecms.co/docs/api/interfaces/FieldProps) (includes detailed comments).

