## App Check

You can integrate Firebase App Check with your app to protect your backend resources from abuse, such as billing fraud
or phishing. Firebase App Check works alongside other Firebase services, such as Firebase Authentication,
to help secure your backend resources.

FireCMS provides a simple way to integrate Firebase App Check with your app.

:::important
Remember to add the domain where you will be deploying your app to the list of allowed domains in AppCheck provider
configuration.
:::

For self-hosted versions, you can enable Firebase App Check in your app by providing the `options`
and `firebaseApp` props in the `useAppCheck` hook.

The `useAppCheck` hook is used to initialize Firebase App Check and monitor its status.
It handles the asynchronous initialization process, provides loading state, and captures any errors that
may occur during initialization.

#### Parameters

- `firebaseApp` (optional): An instance of `FirebaseApp` to use for App Check initialization.
- `options` (optional): Configuration options for App Check.
    - `provider`: The provider you want to use.
    - `isTokenAutoRefreshEnabled`: Whether to automatically refresh the token.
    - `debugToken`: A debug token to use.
    - `forceRefresh`: Whether to force a token refresh.

#### Return Value

Returns an object that includes:
- `loading`: A boolean indicating whether the initialization is in progress.
- `appCheckVerified` (optional): A boolean indicating whether the app has been verified by App Check.
- `error` (optional): Any error encountered during the initialization process.

#### Example

```tsx

const {
    loading,
    error,
    appCheckVerified
} = useAppCheck({
    options: {
        provider: new ReCaptchaEnterpriseProvider(process.env.VITE_RECAPTCHA_SITE_KEY as string),
        isTokenAutoRefreshEnabled: true,
    }
});
```

