### TextareaAutosize with Max and Min Rows

Demonstrating how to set the minimum and maximum number of rows.

```tsx
import React from "react";
import { TextareaAutosize } from "@firecms/ui";

export default function TextareaAutosizeRowsDemo() {
    return (
        <TextareaAutosize 
            placeholder="Type your text here..."
            minRows={3}
            maxRows={6}
        />
    );
}
```
