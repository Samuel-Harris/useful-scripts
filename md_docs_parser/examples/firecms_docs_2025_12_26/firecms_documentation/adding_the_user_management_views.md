### Adding the user management views

Besides the plugin, you will need to add the user management views to your FireCMS project.
They are exported as an array from the `@firecms/user_management` package.
You can add them to your `useBuildNavigationController` hook configuration, in the `adminViews` array.

```jsx

const navigationController = useBuildNavigationController({
    collections,
    views,
    adminViews: userManagementAdminViews,
    collectionPermissions: userManagement.collectionPermissions,
    authController,
    dataSourceDelegate: firestoreDelegate
});
````

