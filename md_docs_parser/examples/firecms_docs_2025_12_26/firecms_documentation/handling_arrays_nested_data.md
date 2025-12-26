### Handling arrays & nested data
When your custom field is inside an array:
- `partOfArray` is `true`
- You may receive an index in a parent context when building nested array editors

For nested values (e.g. editing `address.street` inside a composite field), call `setFieldValue("address.street", value)`.

