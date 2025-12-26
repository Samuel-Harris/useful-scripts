### Collection Configuration Plugin

The Collection Editor UI Plugin allows you to include a UI for editing collection configurations. You can choose where
the configuration is stored and pass the configuration to the plugin. The plugin includes a controller that saves the
configuration in your Firestore database. The default path is `__FIRECMS/config/collections`.

The controller includes methods you can use in your components to manage the collection configuration.

```jsx
const collectionConfigController = useFirestoreCollectionsConfigController({
    firebaseApp
});
```

You can define your collections in code or use the UI to define them. It is also possible to allow modification in the
UI of collections defined in code. You can then merge the collections defined in code with those defined in the UI.

```jsx

// The collection builder is passed to the navigation controller
const collectionsBuilder = useCallback(() => {
    // Define a sample collection in code.
    const collections = [
        productsCollection
        // Your collections here
    ];
    // Merge collections defined in the collection editor (UI) with your own collections
    return mergeCollections(collections, collectionConfigController.collections ?? []);
}, [collectionConfigController.collections]);
```

To add the Collection Editor UI Plugin, include it in the list of plugins passed to the `FireCMS` component.

```jsx
const collectionEditorPlugin = useCollectionEditorPlugin({
    collectionConfigController
});
```

This will add an icon in each collection card that allows you to edit the collection configuration.

