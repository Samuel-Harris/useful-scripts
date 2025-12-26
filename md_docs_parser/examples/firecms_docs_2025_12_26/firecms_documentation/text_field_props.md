### Text Field Props

The `TextField` component in FireCMS UI is highly customizable through various props.
Below is a comprehensive list of props you can use to tailor the `TextField` to your needs:

- `value`: The current value of the text field. Required.
- `onChange`: Handler function called when the text field value changes. Required.
- `label`: The label displayed above the text field.
- `placeholder`: Placeholder text displayed when the text field is empty.
- `multiline`: If `true`, the text field will allow multiline input. Defaults to `false`.
- `rows`: Specifies the number of visible text lines for a multiline text field.
- `variant`: The variant to use for the text field. Options are `'standard'`, `'outlined'`, or `'filled'`. Defaults to `'standard'`.
- `fullWidth`: If `true`, the input will take up the full width of its container. Defaults to `false`.
- `size`: The size of the text field. Options are `'small'` or `'medium'`. Defaults to `'medium'`.
- `color`: The color of the text field. Options are `'default'`, `'primary'`, or `'secondary'`. Defaults to `'default'`.
- `type`: The type of input element; e.g., `password`, `text`, `number`, `email`, etc. Defaults to `'text'`.
- `disabled`: If `true`, the text field will be disabled. Defaults to `false`.
- `helperText`: Text that appears below the text field.
- `error`: If `true`, the text field will have an error state. Defaults to `false`.
- `startAdornment`: Element to be placed at the start of the text field.
- `endAdornment`: Element to be placed at the end of the text field.

