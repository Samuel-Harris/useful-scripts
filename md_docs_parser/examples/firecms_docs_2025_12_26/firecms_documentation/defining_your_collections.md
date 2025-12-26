### Defining your collections

You can create your collections **in the UI or using code**. You can also mix both approaches, but keep in mind that
collections defined in the UI will take precedence. For example, you might have an enum property with 2 values defined
in code, and one extra value defined in the UI. When merged, the resulting enum will have 3 values.

:::important
You can have the same collection defined in both ways. In that case, the collection defined in the UI will
take precedence.

A deep merge is performed, so you can define some properties in the code, and override them in the UI. For example, you
can define an enum string property and the values will be merged from both definitions.
:::

#### Sample collection defined in code

:::note
FireCMS provides around 20 different fields (such as text fields, selects, and complex ones like reference or
sortable array fields). If your use case is not covered by one of the provided fields, you can create your
own [custom field](https://firecms.co/docs/properties/custom_fields.mdx).
:::

:::tip
You don't need to use `buildCollection` or `buildProperty` for building the configuration. They are identity
functions that will help you detect type and configuration errors
:::

```tsx

type Product = {
  name: string;
  main_image: string;
  available: boolean;
  price: number;
  related_products: EntityReference[];
  publisher: {
    name: string;
    external_id: string;
  }
}

const productsCollection = buildCollection<Product>({
  id: "products",
  path: "products",
  name: "Products",
  group: "Main",
  description: "List of the products currently sold in our shop",
  textSearchEnabled: true,
  openEntityMode: "side_panel",
  properties: {
    name: buildProperty({
      dataType: "string",
      name: "Name",
      validation: { required: true }
    }),
    main_image: buildProperty({
      dataType: "string",
      name: "Image",
      storage: {
        mediaType: "image",
        storagePath: "images",
        acceptedFiles: ["image/*"],
        metadata: {
          cacheControl: "max-age=1000000"
        }
      },
      description: "Upload field for images",
      validation: {
        required: true
      }
    }),
    available: buildProperty({
      dataType: "boolean",
      name: "Available",
      columnWidth: 100
    }),
    price: buildProperty(({ values }) => ({
      dataType: "number",
      name: "Price",
      validation: {
        requiredMessage: "You must set a price between 0 and 1000",
        min: 0,
        max: 1000
      },
      disabled: !values.available && {
        clearOnDisabled: true,
        disabledMessage: "You can only set the price on available items"
      },
      description: "Price with range validation"
    })),
    related_products: buildProperty({
      dataType: "array",
      name: "Related products",
      description: "Reference to self",
      of: {
        dataType: "reference",
        path: "products"
      }
    }),
    publisher: buildProperty({
      name: "Publisher",
      description: "This is an example of a map property",
      dataType: "map",
      properties: {
        name: {
          name: "Name",
          dataType: "string"
        },
        external_id: {
          name: "External id",
          dataType: "string"
        }
      }
    })
  },
  permissions: ({
                  user,
                  authController
                }) => ({
    edit: true,
    create: true,
    delete: false
  })
});
```

In FireCMS Cloud, this collection can then be used by including it in the `collections` prop of your main export,
a `FireCMSAppConfig`
object.

In FireCMS PRO, `collections` are passed directly to the `useBuildNavigationController` hook.

#### Modifying a collection defined in the UI

If you just need to add some code to a collection defined in the UI, you can use the `modifyCollection` function in
your `FireCMSAppConfig` object.

This applies to **FireCMS Cloud** only.

```tsx

const appConfig: FireCMSAppConfig = {
    version: "1",
    collections: async (props) => {
        return ([
            // ... full-code defined collections here
        ]);
    },
    modifyCollection: ({ collection }) => {
        if (collection.id === "products") {
            return {
                ...collection,
                name: "Products modified",
                entityActions: [
                    {
                        name: "Sample entity action",
                        onClick: ({ entity }) => {
                            console.log("Entity", entity);
                        }
                    }
                ]
            }
        }
        return collection;
    }
}

export default appConfig;
```

You can use all the props available in the `Collection` interface.

