### Using the Plugin within Your Application

Once you have set up the Collection Editor UI Plugin, you will have access to tools and functions for managing your
Firestore collections. You can access the collection management functions and data through the
`useCollectionEditorPlugin` hook.

#### Collection Editor Object

The `collectionEditor` object returned by the `useCollectionEditorPlugin` hook includes the following properties:

- **`loading`**: Indicates if the collection data is being loaded. Boolean value.
- **`collections`**: Array of collection objects. Contains the collections being managed.
- **`saveCollection`**: Function to persist a collection. Takes a `collection` object and returns a promise resolving
  with the saved collection.
- **`deleteCollection`**: Function to delete a collection. Takes a `collection` object and returns a promise resolving
  when the collection is deleted.
- **`configError`**: Holds any error that occurred while loading collection configurations.
- **`collectionPermissions`**: Function that defines the permissions for collections based on user roles and collection
  configurations.
- **`createCollection`**: Function to initiate the creation of a new collection.
- **`reservedGroups`**: Array of group names that are reserved and cannot be used in collection names.
- **`extraView`**: Custom view added to the FireCMS navigation for collection management.
- **`defineRolesFor`**: Function to define roles for a given user, typically integrated into your auth controller.
- **`authenticator`**: Optional. Authenticator callback built from the current configuration of the collection editor.
  It will only allow access to users with the required roles.

#### Example Access

```jsx

const collectionEditor = useCollectionEditorPlugin({
    collectionConfigController,
    configPermissions: customPermissionsBuilder,
    reservedGroups: ["admin"]
});

// Use collectionEditor properties and functions
if (collectionEditor.loading) {
    return <LoadingIndicator/>;
}

return (
    <div>
        {collectionEditor.collections.map(collection => (
            <CollectionCard key={collection.id} collection={collection}/>
        ))}
        <Button onClick={() => collectionEditor.createCollection()}>
            Create New Collection
        </Button>
    </div>
);
```

