### Select Component Props

The `Select` component in FireCMS UI is highly customizable through various props. Below is a comprehensive list of props you can use to tailor the `Select` component to your needs:

- `open`: Controls whether the select dropdown is open. Defaults to `false`.
- `name`: The name attribute for the select input element.
- `id`: The id attribute for the select input element.
- `onOpenChange`: Callback when the open state changes.
- `value`: The current value(s) of the select component, which can be a `string` or an array of `strings` for multiple selections.
- `className`: Additional classes to apply to the root element.
- `inputClassName`: Additional classes to apply to the input element.
- `onChange`: Handler function called when the select value changes.
- `onValueChange`: Callback when the value changes.
- `onMultiValueChange`: Callback when the value changes in a multiple select.
- `placeholder`: The placeholder text displayed when no value is selected.
- `renderValue`: Custom render function for the selected value.
- `renderValues`: Custom render function for the selected values in multiple select.
- `size`: The size of the select component, can be `"small"` or `"medium"`. Defaults to `"medium"`.
- `label`: The label displayed above the select field, can be a `ReactNode` or a `string`.
- `disabled`: Disables the select component. Defaults to `false`.
- `error`: Sets the select component in an error state. Defaults to `false`.
- `position`: Position of the dropdown relative to the trigger, can be `"item-aligned"` or `"popper"`. Defaults to `"item-aligned"`.
- `endAdornment`: Element to be placed at the end of the select input.
- `multiple`: Enables multiple selection mode. Defaults to `false`.
- `inputRef`: Ref object for the select input element.
- `padding`: Adds padding to the select input. Defaults to `true`.
- `invisible`: Hides the select component but keeps it in the DOM.
- `children`: Content to be rendered as the options within the select component.


