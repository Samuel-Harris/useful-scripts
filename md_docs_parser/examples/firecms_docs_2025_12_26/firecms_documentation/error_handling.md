### Error Handling

The plugin provides error handling through properties such as `configError` and `collectionErrors` in the
`CollectionEditor` object. These can be used to detect and display error messages when loading or managing collections.

#### Example Error Handling

```jsx
if (collectionEditorPlugin.configError) {
    return <ErrorDisplay error={collectionEditorPlugin.configError}/>;
}

if (collectionEditorPlugin.collectionErrors) {
    return <ErrorDisplay error={collectionEditorPlugin.collectionErrors}/>;
}
```

