### FireCMS PRO

If you are migrating from previous beta versions of FireCMS PRO, you will need to make some updates to your project.
The main components have changed theis composition. Instead of having a single `Scaffold` components with all the configuration,
you have additionally an `AppBar` and a `Drawer` component.

More information about the main components can be found in the [Main Components](/docs/self/main_components) section.

#### User management auth controller

For self-hosted versions, there has been a change in the API for the data management controllers. The
`authController` is now passed to the User Management controller, instead of the other way around. The `userManagementController`
can be used as an auth controller, but with all the added logic for user management.

❌ Code before:
```typescript
    /**
     * Controller in charge of user management
     */
    const userManagement = useBuildUserManagement({
        dataSourceDelegate: firestoreDelegate
    });

    /**
     * Controller for managing authentication
     */
    const authController: FirebaseAuthController = useFirebaseAuthController({
        firebaseApp,
        signInOptions,
        loading: userManagement.loading,
        defineRolesFor: userManagement.defineRolesFor
    });
```

✅ Code after:

```typescript
    /**
     * Controller for managing authentication
     */
    const authController: FirebaseAuthController = useFirebaseAuthController({
        firebaseApp,
        signInOptions
    });

    /**
     * Controller in charge of user management
     */
    const userManagement = useBuildUserManagement({
        dataSourceDelegate: firestoreDelegate,
        authController
    });
```

The `userManagement` controller now also qualifies as an `authController`, so you can use it as such, but it is not
necessary to do so.

#### Styling

You also will need to import the default FireCMS styles in your project. You can do this by adding the following import to your `index.css` file:

```css
@import "@firecms/ui/index.css";
```

Your `index.css` file should look like this:

```css
@import "@firecms/ui/index.css";
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
    --fcms-primary: #0070F4;
    --fcms-primary-bg: #0061e610;
    --fcms-secondary: #FF5B79;
}
```

#### Dependencies

The default fonts are now imported in the clients project (so they can be replaced if needed).
You need to add these imports:
```
    "typeface-rubik": "^1.1.13",
    "@fontsource/jetbrains-mono": "^5.0.20",
```

