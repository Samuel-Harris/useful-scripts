### Types

#### `ImportPluginProps`

Defines the properties for the `useImportPlugin` hook.

```typescript
export type ImportPluginProps = {
    onAnalyticsEvent?: (event: string, params?: any) => void;
}
```

#### `ImportAllowedParams`

Provides context for determining import permissions.

```typescript
export type ImportAllowedParams = { 
    collectionEntitiesCount: number; 
    path: string; 
    collection: EntityCollection; 
};
```

