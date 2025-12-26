### Advanced example: Composite slug editor
Automatically generates a slug from the title, but allows manual override.

```tsx
function SlugField({ value, setValue, context, property, showError, error }: FieldProps<string>) {
    const title = context.values.title as string | undefined;

    React.useEffect(() => {
        if (!value && title) {
            const auto = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
            setValue(auto);
        }
    }, [title]);

    return (
        <TextField
            label={property.name}
            value={value ?? ""}
            error={!!error}
            onChange={(e: any) => setValue(e.target.value)}
            helperText={showError ? error : "Will auto-generate from Title if left empty"}
        />
    );
}
```

