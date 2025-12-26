### Programmatic History Creation

For advanced use cases where you need to create history entries programmatically (outside of the normal save callbacks), you can use the `createHistoryEntry` function:

```tsx

// Example: Creating a history entry when importing data
const handleDataImport = async (context: FireCMSContext, importedData: any[]) => {
    for (const item of importedData) {
        // Save the entity first
        await context.dataSource.saveEntity({
            path: "products",
            entityId: item.id,
            values: item,
            status: "new"
        });

        // Create a history entry for the import action
        createHistoryEntry({
            context: context,
            previousValues: undefined, // No previous values for new entities
            values: item,
            path: "products",
            entityId: item.id
        });
    }
};

// Example: Creating a history entry for a custom update operation
const handleCustomUpdate = async (context: FireCMSContext, entityId: string, oldValues: any, newValues: any) => {
    // Perform your custom update logic here
    await context.dataSource.saveEntity({
        path: "products",
        entityId: entityId,
        values: newValues,
        status: "existing"
    });

    // Create a history entry to track the change
    createHistoryEntry({
        context: context,
        previousValues: oldValues,
        values: newValues,
        path: "products",
        entityId: entityId
    });
};
```

#### Parameters

| Parameter        | Type                      | Description                                                                                                              |
| ---------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `context`        | `FireCMSContext<User>`    | The FireCMS context object containing the data source and auth controller                                                |
| `previousValues` | `Partial<any>` (optional) | The previous values of the entity. If not provided, the history entry will be marked as a creation rather than an update |
| `values`         | `Partial<any>`            | The current/new values of the entity                                                                                     |
| `path`           | `string`                  | The collection path where the entity is stored                                                                           |
| `entityId`       | `string`                  | The unique identifier of the entity                                                                                      |

#### History Entry Structure

Each history entry is automatically stored in a subcollection `__history` under the entity and includes:

- All entity values at the time of the change
- `__metadata` object containing:
  - `previous_values`: The previous state of the entity (if provided)
  - `changed_fields`: Array of field paths that were modified
  - `updated_on`: Timestamp of when the change occurred
  - `updated_by`: User ID of who made the change (if authenticated)

