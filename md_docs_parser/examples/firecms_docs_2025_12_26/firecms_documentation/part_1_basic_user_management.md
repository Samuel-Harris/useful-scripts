### Part 1: Basic User Management

This section covers how to create a `users` collection to manage users. This is the foundation for implementing permissions.

#### Create a "Users" Collection

This collection will store your users.

```typescript

export type User = {
  name: string;
  email: string;
};

export const usersCollection = buildCollection<User>({
  name: "Users",
  singularName: "User",
  path: "users",
  properties: {
    name: buildProperty({
      name: "Name",
      validation: { required: true },
      dataType: "string"
    }),
    email: buildProperty({
      name: "Email",
      validation: { required: true, email: true },
      dataType: "string"
    })
  }
});
```

:::tip
Don't forget to set up the Firestore security rules for the `users` path to control who can read and write to the collection.
:::

