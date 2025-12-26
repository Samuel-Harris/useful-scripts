## Collection Bar Actions


![collection_actions](/img/collection_actions.png)

You can add your custom components to the collection bar.

This is useful to add actions that are specific to the collection you are working with.

For example, you could add a button to export the **selected data**, or a button to trigger a specific **action in your backend**.

You can also retrieve the **selected filters** and modify them.

#### Sample retrieving selected entities

You need to define a component that receives `CollectionActionsProps` as props.

```tsx

export function SampleCollectionActions({ selectionController }: CollectionActionsProps) {

    const snackbarController = useSnackbarController();

    const onClick = (event: React.MouseEvent) => {
        const selectedEntities = selectionController?.selectedEntities;
        const count = selectedEntities ? selectedEntities.length : 0;
        snackbarController.open({
            type: "success",
            message: `User defined code here! ${count} products selected`
        });
    };

    return (
        <Button onClick={onClick}
                color="primary"
                variant={"text"}>
            My custom action
        </Button>
    );

}
```

then just add it to your collection configuration:

```tsx

export const productCollection: EntitySchema = buildCollection({
    name: "Products",
    Actions: SampleCollectionActions,
    // ...
});
```

#### Sample modifying filters

This is an example of how you can modify the filters in the collection bar:

```tsx

export function CustomFiltersActions({
                                         tableController
                                     }: CollectionActionsProps) {

    const filterValues = tableController.filterValues;
    const categoryFilter = filterValues?.category;
    const categoryFilterValue = categoryFilter?.[1];

    const updateFilter = (value: string | null) => {
        const newFilter = {
            ...filterValues
        };
        if (value) {
            newFilter.category = ["==", value];
        } else {
            delete newFilter.category;
        }
        tableController.setFilterValues?.(newFilter);
    };

    return (
        <Select placeholder={"Category filter"}
                className={"w-44"}
                endAdornment={categoryFilterValue ?
                    <IconButton size={"small"} onClick={() => updateFilter(null)}>
                        <CloseIcon size={"smallest"}/>
                    </IconButton> : undefined}
                onValueChange={updateFilter}
                size={"small"}
                value={categoryFilterValue}>
            <SelectItem value="cameras">Cameras</SelectItem>
            <SelectItem value="bath">Bath</SelectItem>
        </Select>
    );

}

```

then just add it to your collection configuration:

```tsx

export const productCollection: EntitySchema = buildCollection({
    name: "Products",
    Actions: CustomFiltersActions,
    // ...
});
```

