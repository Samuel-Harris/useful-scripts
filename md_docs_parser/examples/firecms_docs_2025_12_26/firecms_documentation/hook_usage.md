### Hook Usage

Use the `useImportPlugin` hook to create the import plugin and include it in the FireCMS configuration.

#### Example: Integrating the Data Import Plugin

```jsx

export function App() {

    const importPlugin = useImportPlugin({
        onAnalyticsEvent: (event, params) => {
            console.log(`Import Event: ${event}`, params);
            // Integrate with your analytics service if needed
        },
    });

    return (
            <FireCMS
                navigationController={navigationController}
                /*... rest of your configuration */
            >
              {({ context, loading }) => {
                  // ... your components
              }}
            </FireCMS>
    );
}

export default App;
```

