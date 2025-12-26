### Wiring it all up

Once you have all the controllers set up, you can pass them to the
`FireCMS` component, along with the plugins you want to use. The `FireCMS` component will handle the rest, and
render the main view or the login view based on the user's authentication status.

Note how you can customize the main view based on the user's authentication status and permissions.
The default login view is a Firebase login view, but you can define your own login view.

The `SideDialogs` component is used to render the lateral dialogs, like the entity detail view.
The `NavigationRoutes` component is used to render the main navigation routes. It uses `react-router-dom` to handle
the routing, but you are free to replace it with your own routing system.

```jsx
    return (
        <SnackbarProvider>
            <ModeControllerProvider value={modeController}>

                <FireCMS
                    navigationController={navigationController}
                    authController={authController}
                    userConfigPersistence={userConfigPersistence}
                    dataSourceDelegate={firestoreDelegate}
                    storageSource={storageSource}
                    plugins={[dataEnhancementPlugin, importPlugin, exportPlugin, userManagementPlugin, collectionEditorPlugin]}
                >
                    {({
                          context,
                          loading
                      }) => {

                        let component;
                        if (loading || authLoading) {
                            component = <CircularProgressCenter size={"large"}/>;
                        } else {
                            if (!canAccessMainView) {
                                component = (
                                    <FirebaseLoginView
                                        allowSkipLogin={false}
                                        signInOptions={signInOptions}
                                        firebaseApp={firebaseApp}
                                        authController={authController}
                                        notAllowedError={notAllowedError}/>
                                );
                            } else {
                                component = (
                                    <Scaffold autoOpenDrawer={false}>
                                        <AppBar title={"My amazing CMS"}/>
                                        <Drawer/>
                                        <NavigationRoutes/>
                                        <SideDialogs/>
                                    </Scaffold>
                                );
                            }
                        }

                        return component;
                    }}
                </FireCMS>
            </ModeControllerProvider>
        </SnackbarProvider>
    );
```

Find more details about the main components in the [Main Components](https://firecms.co/docs/self/main_components) section.

