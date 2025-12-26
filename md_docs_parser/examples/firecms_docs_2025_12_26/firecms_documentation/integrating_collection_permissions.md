### Integrating Collection Permissions

The Collection Editor UI Plugin includes a `collectionPermissions` function that determines what operations a user can
perform based on their roles and the collection configuration. This function ensures that users have appropriate access
rights throughout your FireCMS project.

#### Example Integration

```jsx
const navigationController = useBuildNavigationController({
    collections: customCollections,
    views: customViews,
    adminViews: userManagementAdminViews,
    collectionPermissions: collectionEditorPlugin.collectionPermissions,
    authController,
    dataSourceDelegate: firestoreDelegate
});
```

**Note:** Applying permissions to a collection overrides the permissions set in the collection configuration.

