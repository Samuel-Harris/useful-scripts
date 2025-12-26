### Collection configuration

The `name` and `properties` you define for your entity collection will be used to generate the fields in the
spreadsheet-like collection tables, and the fields in the generated forms.

:::tip
You can force the CMS to always open the form when editing a document by setting the `inlineEditing` property
to `false` in the collection configuration.
:::

- **`name`**: The plural name of the collection. E.g., 'Products'.
- **`singularName`**: The singular name of an entry in the collection. E.g., 'Product'.
- **`path`**: Relative Firestore path of this view to its parent. If this view is in the root, the path is equal to the
  absolute one. This path also determines the URL in FireCMS.
- **`properties`**: Object defining the properties for the entity schema. More information
  in [Properties](https://firecms.co/docs/properties/properties_intro).
- **`propertiesOrder`**: Order in which the properties are displayed.
    - For properties, use the property key.
    - For additional field, use the field key.
    - If you have subcollections, you get a column for each subcollection, with the path (or alias) as the
      subcollection, prefixed with `subcollection:`. E.g., `subcollection:orders`.
    - If you are using a collection group, you will also have an additional `collectionGroupParent` column.
    - Note that if you set this prop, other ways to hide fields, like `hidden` in the property definition, will be
      ignored. `propertiesOrder` has precedence over `hidden`.

  ```typescript
  propertiesOrder: ["name", "price", "subcollection:orders"]
  ```

- **`openEntityMode`**: Determines how the entity view is opened. You can choose between `side_panel` (default) or
  `full_screen`.
- **`formAutoSave`**: If set to true, the form will be auto-saved when the user changes the value of a field. Defaults
  to false. You can't use this prop if you are using a `customId`.
- **`collectionGroup`**: If this collection is a top-level navigation entry, you can set this property to `true` to
  indicate that this collection is a collection group.
- **`alias`**: You can set an alias that will be used internally instead of the `path`. The `alias` value will be used
  to determine the URL of the collection while `path` will still be used in the datasource. Note that you can use this
  value in reference properties too.
- **`icon`**: Icon key to use in this collection. You can use any of the icons in the Material
  specs: [Material Icons](https://fonts.google.com/icons). e.g., 'account_tree' or 'person'.
  Find all the icons in [Icons](https://firecms.co/docs/icons).
  You can also pass your own icon component (`React.ReactNode`).
- **`customId`**: If this prop is not set, the ID of the document will be created by the datasource. You can set the
  value to 'true' to force the users to choose the ID.
- **`subcollections`**: Following the Firestore document and collection schema, you can add subcollections to your
  entity in the same way you define the root collections.
- **`defaultSize`**: Default size of the rendered collection.
- **`group`**: Optional field used to group top-level navigation entries under a navigation view. If you set this value
  in a subcollection, it has no effect.
- **`description`**: Optional description of this view. You can use Markdown.
- **`entityActions`**: You can define additional actions that can be performed on the entities in this collection. These
  actions can be displayed in the collection view or in the entity view. You can use the `onClick` method to implement
  your own logic. In the `context` prop, you can access all the controllers of FireCMS.
  You can also define entity actions globally. See [Entity Actions](https://firecms.co/docs/entity_actions) for more details.

```tsx
const archiveEntityAction: EntityAction = {
    icon: <ArchiveIcon/>,
    name: "Archive",
    onClick({
                entity,
                collection,
                context
            }): Promise<void> {
        // Add your code here
        return Promise.resolve(undefined);
    }
}
```

- **`initialFilter`**: Initial filters applied to this collection. Defaults to none. Filters applied with this prop can
  be changed by the user.

```tsx
initialFilter: {
    age: [">=", 18]
}
```
```tsx
initialFilter: {
    related_user: ["==", new EntityReference("sdc43dsw2", "users")]
}
```

- **`forceFilter`**: Force a filter in this view. If applied, the rest of the filters will be disabled. Filters applied
  with this prop cannot be changed.

```tsx
forceFilter: {
    age: [">=", 18]
}
```
```tsx
forceFilter: {
    related_user: ["==", new EntityReference("sdc43dsw2", "users")]
}
```

- **`initialSort`**: Default sort applied to this collection. It takes tuples in the shape `["property_name", "asc"]`
  or `["property_name", "desc"]`.

```tsx
initialSort: ["price", "asc"]
```

- **`Actions`**: Builder for rendering additional components such as buttons in the collection toolbar. The builder
  takes an object with props `entityCollection` and `selectedEntities` if any are set by the end user.
- **`pagination`**: If enabled, content is loaded in batches. If `false` all entities in the
  collection are loaded. This means that when reaching the end of the collection, the CMS will load more entities.
  You can specify a number to specify the pagination size (50 by default)
  Defaults to `true`
- **`additionalFields`**: You can add additional fields to both the collection view and the form view by implementing an
  additional field delegate.
- **`textSearchEnabled`**: Flag to indicate if a search bar should be displayed on top of the collection table.
- **`permissions`**: You can specify an object with boolean permissions with the
  shape `{edit:boolean; create:boolean; delete:boolean}` to indicate the actions the user can perform. You can also pass
  a [`PermissionsBuilder`](https://firecms.co/docs/api/type-aliases/PermissionsBuilder) to customize the permissions based on the user or entity.
- **`inlineEditing`**: Can the elements in this collection be edited inline in the collection view? If this flag is set
  to false but `permissions.edit` is `true`, entities can still be edited in the side panel.
- **`selectionEnabled`**: Are the entities in this collection selectable? Defaults to `true`.
- **`selectionController`**: Pass your own selection controller if you want to control selected entities
  externally. [See `useSelectionController`](https://firecms.co/docs/api/functions/useSelectionController).
- **`exportable`**: Should the data in this collection view include an export button? You can also set
  an [`ExportConfig`](https://firecms.co/docs/api/interfaces/ExportConfig) configuration object to customize the export and add additional
  values. Defaults to `true`.
- **`hideFromNavigation`**: Should this collection be hidden from the main navigation panel if it is at the root level,
  or in the entity side panel if it's a subcollection? It will still be accessible if you reach the specified path. You
  can also use this collection as a reference target.
- **`callbacks`**: This interface defines all the callbacks that can be used when an entity is being created, updated,
  or deleted. Useful for adding your own logic or blocking the operation's execution. [More information](https://firecms.co/docs/callbacks).
- **`entityViews`**: Array of builders for rendering additional panels in an entity view. Useful if you need to render custom
  views for your entities. [More information](https://firecms.co/docs/collections/entity_views).
- **`alwaysApplyDefaultValues`**: If set to true, the default values of the properties will be applied
  to the entity every time the entity is updated (not only when created).
  Defaults to false.

