### Implementing MongoDB in FireCMS

Let's create a new `MongoDBApp` component that integrates MongoDB Atlas (and optionally Firebase).

#### Initialization

Initialize Firebase and MongoDB within your component:

```jsx

const MongoDBApp = () => {
  const name = "My FireCMS App";

  // Initialize Firebase
  const { firebaseApp, firebaseConfigLoading, configError } = useInitialiseFirebase({ firebaseConfig });

  // Initialize MongoDB
  const { app } = useInitRealmMongodb(atlasConfig);

  // ...
};

export default MongoDBApp;
```

#### Controllers and Persistence

Next, set up the mode controller, user configuration persistence, and MongoDB auth controller.

```jsx
const modeController = useBuildModeController();
const userConfigPersistence = useBuildLocalConfigurationPersistence();

const authController: MongoAuthController = useMongoDBAuthController({ app });
const mongoDataSourceDelegate = useMongoDBDelegate({
  app,
  cluster: "mongodb-atlas",
  database: "todo"
});
```

#### Firebase Storage Source

If you plan to use Firebase for file storage, initialize `storageSource`.

```jsx
const storageSource = useFirebaseStorageSource({ firebaseApp });
```

#### Authenticator Validation

Define the validation logic for your authenticator.

```jsx
const { authLoading, canAccessMainView, notAllowedError } = useValidateAuthenticator({
  authController,
  authenticator: () => true, // Replace with your logic
  dataSourceDelegate: mongoDataSourceDelegate,
  storageSource
});
```

#### Navigation Controller

Set up the navigation controller with your collections.

```jsx
const navigationController = useBuildNavigationController({
  collections: [productsCollection],
  authController,
  dataSourceDelegate: mongoDataSourceDelegate
});
```

#### Rendering the Application

Finally, wire everything up inside the return statement of your component.

```jsx
const MongoDBApp = () => {
  const name = "My FireCMS App";

  const { firebaseApp, firebaseConfigLoading, configError } = useInitialiseFirebase({ firebaseConfig });
  const { app } = useInitRealmMongodb(atlasConfig);

  const modeController = useBuildModeController();
  const userConfigPersistence = useBuildLocalConfigurationPersistence();
  const authController: MongoAuthController = useMongoDBAuthController({ app });
  const mongoDataSourceDelegate = useMongoDBDelegate({
    app,
    cluster: "mongodb-atlas",
    database: "todo"
  });
  const storageSource = useFirebaseStorageSource({ firebaseApp });
  const { authLoading, canAccessMainView, notAllowedError } = useValidateAuthenticator({
    authController,
    authenticator: () => true, // Replace with your logic
    dataSourceDelegate: mongoDataSourceDelegate,
    storageSource
  });
  const navigationController = useBuildNavigationController({
    collections: [productsCollection],
    authController,
    dataSourceDelegate: mongoDataSourceDelegate
  });

  if (firebaseConfigLoading || !firebaseApp) {
    return <CircularProgressCenter />;
  }

  if (configError) {
    return <CenteredView>{configError}</CenteredView>;
  }

  return (
    <SnackbarProvider>
      <ModeControllerProvider value={modeController}>
        <FireCMS
          navigationController={navigationController}
          authController={authController}
          userConfigPersistence={userConfigPersistence}
          dataSourceDelegate={mongoDataSourceDelegate}
          storageSource={storageSource}
        >
          {({ context, loading }) => {
            if (loading || authLoading) {
              return <CircularProgressCenter size="large" />;
            }

            if (!canAccessMainView) {
              return (
                <MongoLoginView
                  allowSkipLogin={false}
                  authController={authController}
                  registrationEnabled={true}
                  notAllowedError={notAllowedError}
                />
              );
            }

            return (
              <Scaffold autoOpenDrawer={false}>
                <AppBar title={name} />
                <Drawer />
                <NavigationRoutes />
                <SideDialogs />
              </Scaffold>
            );
          }}
        </FireCMS>
      </ModeControllerProvider>
    </SnackbarProvider>
  );
};

export default MongoDBApp;
```

