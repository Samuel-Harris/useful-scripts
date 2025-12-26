### AuthController

The `AuthController` is the controller responsible for managing the authentication. The delegate will
be passed to FireCMS and will be used internally by CMS.

You can access the auth controller in any component using the `useAuthController` hook.
You can also access the auth controller from callbacks where there is a `context` object defined,
under `context.authController`.

FireCMS provides default implementations for:

- Firebase `useFirebaseAuthController` (package `@firecms/firebase`)
- MongoDB `useMongoDBAuthController` (package `@firecms/mongodb`)

#### Description of Properties and Methods

**user**: The user currently logged in. Can be the user object or `null` if login was skipped.

**roles**: (Optional) Roles related to the logged-in user.

**initialLoading**: (Optional) A flag used to avoid displaying the login screen when the app first loads and the login
status has not yet been determined.

**authLoading**: A flag used to display a loading screen while the user is logging in or out.

**signOut**: A method to sign out the user. Returns a `Promise<void>`.

**authError**: (Optional) An error object representing issues initializing authentication.

**authProviderError**: (Optional) An error object dispatched by the authentication provider.

**getAuthToken**: A method to retrieve the authentication token for the current user. Returns a `Promise<string>`.

**loginSkipped**: A flag indicating whether the user skipped the login process.

**extra**: An object containing additional data related to the authentication controller.

**setExtra**: A method to set the additional data for the authentication controller. Accepts `extra` parameter of
type `ExtraData`.

##### Additional Methods for `useFirebaseAuthController`

**googleLogin**: A method to initiate login using Google authentication.

**anonymousLogin**: A method to log in anonymously.

**appleLogin**: A method to initiate login using Apple authentication.

**facebookLogin**: A method to initiate login using Facebook authentication.

**githubLogin**: A method to initiate login using GitHub authentication.

**microsoftLogin**: A method to initiate login using Microsoft authentication.

**twitterLogin**: A method to initiate login using Twitter authentication.

**emailPasswordLogin**: A method to log in using an email and password. Takes `email` and `password` as parameters.

**fetchSignInMethodsForEmail**: A method to fetch sign-in methods for a given email. Takes `email` as a parameter and returns a `Promise<string[]>`.

**createUserWithEmailAndPassword**: A method to create a new user using an email and password. Takes `email` and `password` as parameters.

**sendPasswordResetEmail**: A method to send a password reset email. Takes `email` as a parameter and returns a `Promise<void>`.

**phoneLogin**: A method to log in using a phone number. Takes `phone` and `applicationVerifier` as parameters.

**confirmationResult**: (Optional) An object containing the result of a phone number authentication operation.

**skipLogin**: A method to skip the login process.

**setUser**: A method to set the user object. Takes `user` of type `FirebaseUser` or `null` as a parameter.

**setRoles**: A method to set roles for the logged-in user. Takes an array of `Role` objects as a parameter.


