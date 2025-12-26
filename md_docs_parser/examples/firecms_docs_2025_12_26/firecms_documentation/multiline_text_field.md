### Multiline Text Field

A text field that supports multiline inputs, suitable for comments or notes:

```tsx
import React, { useState } from "react";
import { TextField } from "@firecms/ui";

export default function TextFieldMultilineDemo() {
    const [value, setValue] = useState("");

    return (
        <TextField
            value={value}
            onChange={(e) => setValue(e.target.value)}
            label="Multiline Text Field"
            placeholder="Enter text"
            multiline
            minRows={4}
        />
    );
}

```

