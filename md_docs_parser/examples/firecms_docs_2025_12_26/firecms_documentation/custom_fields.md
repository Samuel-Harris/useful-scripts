## Custom fields

Custom fields let you fully control how a property's value is edited and displayed in a form. Instead of the built‑in renderer for a `dataType`, you supply a React component. That component receives a rich set of props (`FieldProps`) so it can:

- Read and update the current value (`value`, `setValue`)
- Update any other property in the same form (`setFieldValue` or `context.setFieldValue`)
- Access all current entity values + form utilities (`context`)
- Respect form state (`isSubmitting`, `disabled`, `showError`, `error`, `touched`)
- Adapt layout (`size`, `partOfArray`, `minimalistView`, `autoFocus`)
- Use developer defined `customProps`

<video style={{
    maxWidth: "100%",
    width: "640px",
    margin: "32px 0px 32px",
    alignSelf: "center"
}}
       loop autoPlay muted>
    <source src="/img/custom_fields_dark.mp4" type="video/mp4"/>
</video>

