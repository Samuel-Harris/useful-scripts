### New format

Since it is now possible to deploy FireCMS in our hosted service, the output
of your project needs to be in a specific format.

The `index.ts` file should export a `FireCMSAppConfig` object, which is defined as follows:

```typescript

export type FireCMSAppConfig = {

    /**
     * Customization schema version.
     */
    version: "1";

    /**
     * List of the mapped collections in the CMS.
     * Each entry relates to a collection in the root database.
     * Each of the navigation entries in this field
     * generates an entry in the main menu.
     */
    collections?: EntityCollection[] | EntityCollectionsBuilder;

    /**
     * Custom additional views created by the developer, added to the main
     * navigation.
     */
    views?: CMSView[] | CMSViewsBuilder;

    /**
     * List of custom form fields to be used in the CMS.
     * You can use the key to reference the custom field in
     * the `propertyConfig` prop of a property in a collection.
     */
    propertyConfigs?: PropertyConfig[];

    /**
     * List of additional custom views for entities.
     * You can use the key to reference the custom view in
     * the `entityViews` prop of a collection.
     *
     * You can also define an entity view from the UI.
     */
    entityViews?: EntityCustomView[];

}
```

Let's break down the different fields:

