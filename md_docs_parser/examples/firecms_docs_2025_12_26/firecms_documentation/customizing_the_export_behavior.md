### Customizing the Export Behavior

You can customize how the export functionality behaves by providing custom implementations for the `exportAllowed`,
`notAllowedView`, and `onAnalyticsEvent` props.

#### Example: Restricting Export Based on User Role

```jsx
const exportPlugin = useExportPlugin({
    exportAllowed: ({
                        collection,
                        path,
                        collectionEntitiesCount
                    }) => {
        // Allow export only for admins
        return userRoles.includes('admin');
    },
    notAllowedView: <div>Only administrators can export data.</div>,
    onAnalyticsEvent: (event, params) => {
        // Log export events for auditing
        logAnalytics(event, params);
    },
});
```

