### Recommended: FireCMS Pro and Cloud

Before implementing custom authentication, we strongly recommend considering **FireCMS Pro** or **FireCMS Cloud**, which include:

- ✅ Built-in user management system
- ✅ Role-based permissions (Admin, Editor, Viewer)
- ✅ Team management interface
- ✅ User invitation system
- ✅ Granular collection and field-level permissions
- ✅ Audit logs and user activity tracking
- ✅ Enterprise-grade security features

These solutions provide a complete authentication and authorization system out of the box, saving you significant development time and ensuring security best practices.

[Learn more about User Management in FireCMS Pro →](/docs/pro/user_management)

[Try FireCMS Cloud →](https://app.firecms.co)

:::note

When you initialize a new FireCMS project using the CLI, you might find a boilerplate authenticator in your `App.tsx` file. It's a standard FireCMS interface and looks something like this (no need to hate Flanders!):

```typescript
const myAuthenticator: Authenticator<FirebaseUserWrapper> = useCallback(async ({
                                                                                   user,
                                                                                   authController
                                                                               }) => {
    if (user?.email?.includes("flanders")) {
        // You can throw an error to prevent access
        throw Error("Stupid Flanders!");
    }
    console.log("Allowing access to", user);
    return true;
}, []);
```

This is just a placeholder to show you where to implement your own authentication logic. You can replace it with one of the authenticators described below.

:::

