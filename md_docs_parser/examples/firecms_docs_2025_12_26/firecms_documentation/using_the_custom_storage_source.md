### Using the Custom Storage Source

After creating the custom storage source, you can use it in your FireCMS application by initializing it in your component and passing it to the `FireCMS` component.

#### Example Usage

Here is an example of how to use the custom storage source in your FireCMS application

```tsx

const customStorageConfig: CustomStorageSourceProps = {
  apiKey: "your-api-key",
  apiSecret: "your-api-secret",
  region: "your-region",
  defaultBucket: "your-bucket-name"
  // ... other necessary properties
};

const CustomStorageApp: React.FC = () => {
  const name = "My Custom Storage FireCMS App";

  const modeController = useBuildModeController();
  const userConfigPersistence = useBuildLocalConfigurationPersistence();
  const storageSource = useCustomStorageSource(customStorageConfig);

  // const authController = useFirebaseAuthController(); // your auth controller
  // const dataSourceDelegate = {}; // Your data source delegate implementation

  const navigationController = useBuildNavigationController({
    collections: [productsCollection],
    // authController,
    // dataSourceDelegate
  });

  // if (authLoading) {
  //   return <CircularProgressCenter />;
  // }

  return (
    <SnackbarProvider>
      <ModeControllerProvider value={modeController}>
        <FireCMS
          navigationController={navigationController}
          userConfigPersistence={userConfigPersistence}
          storageSource={storageSource}
          // authController={authController}
          // dataSourceDelegate={dataSourceDelegate}
        >
          {({ context, loading }) => {
            if (loading || authLoading) {
              return <CircularProgressCenter size="large" />;
            }

            if (!canAccessMainView) {
              return <CenteredView>{notAllowedError}</CenteredView>;
            }

            return (
              <Scaffold>
                <AppBar title={"My app"} />
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

export default CustomStorageApp;
```

As this example uses AWS S3, you will also need to enable cors in the bucket,
as described in the [AWS documentation - Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html?icmpid=docs_amazons3_console).

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

This documentation provides a clear guide for defining custom storage solutions in FireCMS. Follow the template to integrate other storage services as per your requirements.

