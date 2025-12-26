### Configuration

Integrate the Data Import Plugin using the `useImportPlugin` hook. You can optionally provide `ImportPluginProps` to
customize its behavior.

#### ImportPluginProps

- **`onAnalyticsEvent`**: A callback triggered on import-related analytics events.
    - **Type**: `(event: string, params?: any) => void`
    - **Default**: `undefined`

