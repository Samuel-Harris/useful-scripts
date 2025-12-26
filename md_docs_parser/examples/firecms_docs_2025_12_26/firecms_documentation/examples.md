### Examples

Let's build an example where we add an action to archive a product.
When the action is clicked, we will call a Google Cloud Function that will run some business logic in the backend.

#### Using the `fetch` API

You can use the standard `fetch` API to call any HTTP endpoint, including a Google Cloud Function. This is a general-purpose method that works with any backend.

```tsx

export const productsCollection = buildCollection<Product>({
    id: "products",
    path: "products",
    // other properties
    entityActions: [
        {
            icon: <ArchiveIcon/>,
            name: "Archive",
            collapsed: false,
            onClick({
                        entity,
                        context,
                    }) {
                const snackbarController = context.snackbarController;
                return fetch("[YOUR_ENDPOINT]/archiveProduct", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        productId: entity.id
                    })
                }).then(() => {
                    snackbarController.open({
                        message: "Product archived",
                        type: "success"
                    });
                }).catch((error) => {
                    snackbarController.open({
                        message: "Error archiving product",
                        type: "error"
                    });
                });
            }
        }
    ],
});
```

#### Using the Firebase Functions SDK

If you're using Firebase, the recommended approach is to use the Firebase Functions SDK. It simplifies calling functions and automatically handles authentication tokens.

First, ensure you have the `firebase` package installed and initialized in your project.

Then, you can define your action like this:

```tsx

// Initialize Firebase Functions
// Make sure you have initialized Firebase elsewhere in your app
const functions = getFunctions();
const archiveProductCallable = httpsCallable(functions, 'archiveProduct');

export const productsCollection = buildCollection<Product>({
    id: "products",
    path: "products",
    // other properties
    entityActions: [
        {
            icon: <ArchiveIcon/>,
            name: "Archive with Firebase",
            collapsed: false,
            async onClick({
                        entity,
                        context,
                    }) {
                const snackbarController = context.snackbarController;
                try {
                    await archiveProductCallable({ productId: entity.id });
                    snackbarController.open({
                        message: "Product archived successfully",
                        type: "success"
                    });
                } catch (error) {
                    console.error("Error archiving product:", error);
                    snackbarController.open({
                        message: "Error archiving product: " + error.message,
                        type: "error"
                    });
                }
            }
        }
    ],
});
```

