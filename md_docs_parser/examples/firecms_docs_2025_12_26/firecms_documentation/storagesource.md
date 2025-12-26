### StorageSource

The `StorageSource` is the controller responsible for managing the file storage. The delegate will
be passed to FireCMS and will be used internally by CMS.

You can access the storage source in any component using the `useStorageSource` hook. You can also access the storage
source from callbacks where there is a `context` object defined, under `context.storageSource`.

FireCMS provides default implementations for:

- Firebase `useFirebaseStorageSource` (package `@firecms/firebase`)

#### Description of Methods

**uploadFile**: Upload a file to storage, specifying a name and a path. Accepts parameters
like `file`, `fileName`, `path`, `metadata`, and `bucket`.

**getDownloadURL**: Convert a storage path or URL into a download configuration. Accepts `pathOrUrl` and
optionally `bucket`.

**getFile**: Retrieve a file from a storage path. Returns `null` if the file does not exist. Accepts `path` and
optionally `bucket`.

