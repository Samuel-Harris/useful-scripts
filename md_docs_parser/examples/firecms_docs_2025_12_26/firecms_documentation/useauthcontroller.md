### `useAuthController`
For state and operations regarding authentication.

The props provided by this hook are:

* `user` The Firebase user currently logged in or null
* `authProviderError` Error dispatched by the auth provider
* `authLoading` Is the login process ongoing
* `loginSkipped` Is the login skipped
* `notAllowedError` The current user was not allowed access
* `skipLogin()` Skip login
* `signOut()` Sign out

Example:

```tsx

export function ExampleCMSView() {

    const authController = useAuthController();

    return (
        authController.user ?
            <div>Logged in as {authController.user.displayName}</div>
            :
            <div>You are not logged in</div>
    );
}
```


