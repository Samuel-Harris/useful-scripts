### Example Usage

Below is an example of how to integrate the Collection Editor UI Plugin into a FireCMS application.

#### Plugin Setup

```jsx

export function App() {

  const title = "My CMS app";

  const {
    firebaseApp,
    firebaseConfigLoading,
    configError
  } = useInitialiseFirebase({
    firebaseConfig
  });

  /**
   * Controller used to save the collection configuration in Firestore.
   * Note that this is optional and you can define your collections in code.
   */
  const collectionConfigController = useFirestoreCollectionsConfigController({
    firebaseApp
  });

  const collectionsBuilder = useCallback(() => {
    // Here we define a sample collection in code.
    const collections = [
      productsCollection
      // Your collections here
    ];
    // You can merge collections defined in the collection editor (UI) with your own collections
    return mergeCollections(collections, collectionConfigController.collections ?? []);
  }, [collectionConfigController.collections]);

  const signInOptions: FirebaseSignInProvider[] = ["google.com", "password"];

  /**
   * Controller used to manage the dark or light color mode
   */
  const modeController = useBuildModeController();

  /**
   * Delegate used for fetching and saving data in Firestore
   */
  const firestoreDelegate = useFirestoreDelegate({
    firebaseApp
  })

  /**
   * Controller used for saving and fetching files in storage
   */
  const storageSource = useFirebaseStorageSource({
    firebaseApp
  });

  /**
   * Controller for managing authentication
   */
  const authController: FirebaseAuthController = useFirebaseAuthController({
    firebaseApp,
    signInOptions,
  });

  /**
   * Controller for saving some user preferences locally.
   */
  const userConfigPersistence = useBuildLocalConfigurationPersistence();

  /**
   * Use the authenticator to control access to the main view
   */
  const {
    authLoading,
    canAccessMainView,
    notAllowedError
  } = useValidateAuthenticator({
    authController,
    dataSourceDelegate: firestoreDelegate,
    storageSource
  });

  const navigationController = useBuildNavigationController({
    collections: collectionsBuilder,
    authController,
    dataSourceDelegate: firestoreDelegate
  });

  const collectionEditorPlugin = useCollectionEditorPlugin({
    collectionConfigController
  });

  if (firebaseConfigLoading || !firebaseApp) {
    return <CircularProgressCenter/>;
  }

  if (configError) {
    return <>{configError}</>;
  }

  return (
          <SnackbarProvider>
            <ModeControllerProvider value={modeController}>

              <FireCMS
                      apiKey={import.meta.env.VITE_FIRECMS_API_KEY}
                      navigationController={navigationController}
                      authController={authController}
                      userConfigPersistence={userConfigPersistence}
                      dataSourceDelegate={firestoreDelegate}
                      storageSource={storageSource}
                      plugins={[
                        collectionEditorPlugin
                      ]}
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
                              <Scaffold
                                      // logo={...}
                                      autoOpenDrawer={false}>
                                <AppBar title={title}/>
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
}
```


