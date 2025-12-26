### Adding the Collection Editor Views

The Collection Editor UI Plugin provides custom views that need to be added to your FireCMS project. These views are
integrated into the FireCMS navigation and allow users to manage collections.

#### Example Integration

```jsx

const collectionEditorPlugin = useCollectionEditorPlugin({
    collectionConfigController,
    configPermissions: customPermissionsBuilder,
    reservedGroups: ["admin"],
    extraView: {
        View: CustomCollectionView,
        icon: <CollectionIcon/>
    }
});

// Include the plugin in your FireCMS configuration
<FireCMS
    navigationController={navigationController}
    authController={authController}
    dataSourceDelegate={firestoreDelegate}
    plugins={[userManagementPlugin, collectionEditorPlugin]}
>
    {/* Your application components */}
</FireCMS>
```

