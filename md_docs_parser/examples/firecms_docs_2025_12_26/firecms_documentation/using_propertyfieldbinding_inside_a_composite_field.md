### Using PropertyFieldBinding inside a composite field

```tsx
function GeoPointField({ context }: FieldProps<any>) {
  return (
    <div style={{ display: "flex", gap: 8 }}>
      <PropertyFieldBinding
        propertyKey="lat"
        property={context.collection?.properties.lat}
        context={context}
        minimalistView
      />
      <PropertyFieldBinding
        propertyKey="lng"
        property={context.collection?.properties.lng}
        context={context}
        minimalistView
      />
      {/* Could add a map picker that calls context.setFieldValue("lat", newLat) */}
    </div>
  );
}
```

