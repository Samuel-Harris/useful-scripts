### When should you create a custom field?
Use a custom field when you need one (or more) of the following:
- A visual style not covered by built‑ins (color pickers, tag inputs, sliders, charts, AI assisted fields, etc.)
- Composite UI combining several properties (e.g. lat/lng map picker writing to two numeric fields)
- Integrations (upload to an external API, fetch suggestions, geocode, etc.)

If you only need validation or simple transformation, prefer property level `validation` options first to keep things simple.
If you need dynamic behavior depending on other values, consider using [conditional fields](https://firecms.co/docs/conditional_fields.md) instead.

