### CollectionActionsProps

The following properties are available on the `CollectionActionsProps` interface:

- **`path`**: Full collection path of this entity. This is the full path, like `users/1234/addresses`.

- **`relativePath`**: Path of the last collection, like `addresses`.

- **`parentCollectionIds`**: Array of the parent path segments like `['users']`.

- **`collection`**: The collection configuration.

- **`selectionController`**: Use this controller to get the selected entities and to update the selected entities state.

- **`tableController`**: Use this controller to get the table controller and to update the table controller state.

- **`context`**: Context of the app status.

- **`collectionEntitiesCount`**: Count of the entities in this collection.

