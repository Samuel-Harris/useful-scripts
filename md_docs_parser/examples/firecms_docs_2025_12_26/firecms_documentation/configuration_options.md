### Configuration Options

| Option           | Type                            | Description                                                                                                                                      |
| ---------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `defaultEnabled` | `boolean`                       | If `true`, the history view will be enabled for all collections by default. Each collection can override this by setting its `history` property. |
| `getUser`        | `(uid: string) => User \| null` | Optional function to get the user object (display name, photo, etc.) from a user ID to display in the history log.                               |

