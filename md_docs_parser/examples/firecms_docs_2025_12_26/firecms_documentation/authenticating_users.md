### Authenticating Users

The Collection Editor UI Plugin integrates with your authentication system to ensure that only authorized users can
manage collections. You can use the `useValidateAuthenticator` hook to authenticate users and determine their access
levels.

#### Example Usage

```jsx

const {
    authLoading,
    canAccessMainView,
    notAllowedError
} = useValidateAuthenticator({
    disabled: collectionEditorPlugin.loading,
    authController: authController,
    authenticator: customAuthenticator,
    dataSourceDelegate: firestoreDelegate,
    storageSource: storageSource
});

if (authLoading) {
    return <LoadingIndicator/>;
}

if (!canAccessMainView) {
    return <AccessDeniedError message={notAllowedError}/>;
}

// Render your main application view
```

