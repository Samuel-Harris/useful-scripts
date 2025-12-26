### Part 3: Using Firebase Custom Claims for Permissions

An alternative to storing roles in Firestore is to use Firebase Authentication's custom claims.

#### Step 1: Set Custom Claims

You need to set custom claims for a user from a backend environment using the Firebase Admin SDK. This is typically done in a Cloud Function.

```typescript
// Example Cloud Function to set a role claim

admin.initializeApp();

export const setUserRole = functions.https.onCall(async (data, context) => {
  if (!context.auth?.token.admin) {
    throw new functions.https.HttpsError("permission-denied", "Must be an admin to set roles.");
  }

  const { uid, role } = data;
  await admin.auth().setCustomUserClaims(uid, { role });

  return { message: `Success! User ${uid} has been given the role of ${role}.` };
});
```

#### Step 2: Implement a Claims-Based Authenticator

This authenticator reads the custom claims from the user's ID token.

```typescript

export const claimsAuthenticator: Authenticator<FirebaseUserWrapper> = async ({
  user,
  authController
}) => {
  if (!user) return false;

  try {
    const idTokenResult = await user.firebaseUser.getIdTokenResult(true); // Force refresh
    const role = idTokenResult.claims.role || "viewer"; // Default to 'viewer' if no role claim
    authController.setExtra({ role });
    return true;
  } catch (error) {
    console.error("Authentication error:", error);
    return false;
  }
};
```

#### Step 3: Use Claims in Collections

The `permissions` implementation is the same as with the role-based approach, as the role is extracted and placed in `authController.extra`.

```typescript

export const articlesCollection = buildCollection({
  name: "Articles",
  path: "articles",
  permissions: ({ authController }) => {
    const userRole = authController.extra?.role;
    return {
      read: true,
      edit: userRole === "admin" || userRole === "editor",
      create: userRole === "admin" || userRole === "editor",
      delete: userRole === "admin"
    };
  },
  // ... properties
});
```

