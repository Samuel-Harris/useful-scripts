### Custom field example
A custom text field with a background color supplied via `customProps` (scroll below for full prop contract and advanced techniques):

```tsx

interface CustomColorTextFieldProps {
    color: string;
}

export default function CustomColorTextField({
    property,
    value,
    setValue,
    customProps,
    includeDescription,
    showError,
    error,
    isSubmitting,
    context
}: FieldProps<string, CustomColorTextFieldProps>) {

    const { mode } = useModeController();
    const backgroundColor = customProps?.color ?? (mode === "light" ? "#eef4ff" : "#16325f");

    return (
        <>
            <TextField
                inputStyle={{ backgroundColor }}
                error={!!error}
                disabled={isSubmitting}
                label={error ?? property.name}
                value={value ?? ""}
                onChange={(evt: any) => setValue(evt.target.value)}
            />
            <FieldHelperText
                includeDescription={includeDescription}
                showError={showError}
                error={error}
                property={property}
            />
        </>
    );
}
```

Usage in a collection:

```tsx
export const blogCollection = buildCollection({
    id: "blog",
    path: "blog",
    name: "Blog entry",
    properties: {
        // ... other properties
        gold_text: {
            name: "Gold text",
            description: "This field is using a custom component defined by the developer",
            dataType: "string",
            Field: CustomColorTextField,
            customProps: {
                color: "gold"
            }
        }
    }
});
```

