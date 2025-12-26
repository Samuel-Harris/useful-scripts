### Basic Text Field

A basic text field with minimal configuration:

```tsx
import React, { useState } from "react";
import { TextField } from "@firecms/ui";

export default function TextFieldBasicDemo() {
    const [value, setValue] = useState("");

    return (
        <TextField
            value={value}
            onChange={(e) => setValue(e.target.value)}
            label="Basic Text Field"
            placeholder="Enter text"
        />
    );
}
```

