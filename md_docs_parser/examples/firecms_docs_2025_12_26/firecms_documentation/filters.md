### Filters

:::tip
If you need to have some filters and sorting applied by default, you can use the `initialFilter`and `initialSort`
prop. You can also force a filter combination to be always applied by using the `forceFilter`prop.
:::

Filtering is enabled by default for string, numbers, booleans, dates, and arrays. A dropdown is included in every
column of the collection where applicable.

Since Firestore has limited querying capabilities, each time you apply a filter or new sort, the previous sort/filter
combination gets reset by default (unless filtering, sorting by the same property).

If you need to enable filtering/sorting by more than one property at a time, you can specify the filters that you have
enabled in your Firestore configuration. In order to do so, just pass the indexes configuration to your collection:

```tsx

const productsCollection = buildCollection<Product>({
    id: "products",
    path: "products",
    name: "Product",
    properties: {
        // ...
    },
    indexes: [
        {
            price: "asc",
            available: "desc"
        }
    ]
});
```

