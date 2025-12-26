### Rendering (or composing) other properties inside a custom field
If your custom field wants to include the UI of another property, use `PropertyFieldBinding`.
This keeps validation and consistency:

```tsx

<PropertyFieldBinding
  propertyKey="subtitle"
  property={collection.properties.subtitle}
  context={context}
  includeDescription
/>
```

This is ideal for composite widgets that orchestrate multiple underlying values.
For example, the built-in `map` default widget is just a wrapper around the properties defined

