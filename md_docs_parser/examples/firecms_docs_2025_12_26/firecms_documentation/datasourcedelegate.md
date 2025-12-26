### DataSourceDelegate

The `DataSourceDelegate` is the delegate responsible for managing the data source. The delegate will
be passed to FireCMS and will be used internally by the `DataSource`.

You can retrieve the data source in any component using the `useDataSource` hook. You can also access the data source
from callbacks where there is a `context` object defined, under `context.dataSource`.

FireCMS provides default implementations for:

- Firebase `useFirestoreDelegate` (package `@firecms/firebase`)
- MongoDB `useMongoDBDelegate` (package `@firecms/mongodb`)

#### Creating your own DataSourceDelegate

If you want to create your own `DataSourceDelegate`, you will need to implement the following methods:

**fetchCollection**: Used to fetch a collection of entities from your data source. Accepts various parameters
like `path`, `filter`, `limit`, etc.

**listenCollection**: (Optional) Listen for real-time updates on a collection. Returns a function to cancel the
subscription. If not implemented, the `fetchCollection` method will be used instead.

**fetchEntity**: Fetch a single entity based on `path` and `entityId`.

**listenEntity**: (Optional) Listen for real-time updates on a single entity. Returns a function to cancel the
subscription. If not implemented, the `fetchEntity` method will be used instead.

**saveEntity**: Save or update an entity at a specific path.

**deleteEntity**: Delete an entity by providing the entity to delete.

**checkUniqueField**: Check the uniqueness of a particular field in a collection.

**generateEntityId**: Generate a unique ID for a new entity.

**countEntities**: (Optional) Count the number of entities in a collection.

**isFilterCombinationValid**: (Optional) Check if a given filter combination is valid.

**currentTime**: (Optional) Get the current timestamp object.

**delegateToCMSModel**: Convert data from the source model to CMS model.

**cmsToDelegateModel**: Convert data from the CMS model to the source model.

**setDateToMidnight**: (Optional) Set the date to midnight.

**initTextSearch**: (Optional) Initialize text search capabilities.

