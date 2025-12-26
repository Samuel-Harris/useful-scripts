### Basic IconButton

A simple icon button with minimal configuration.

```tsx
import React from "react";
import { AddIcon, IconButton } from "@firecms/ui";

export default function IconButtonBasicDemo() {
    return (
        <IconButton
            variant="filled"
            onClick={() => console.log("Clicked!")}>
            <AddIcon/>
        </IconButton>
    );
}

```

