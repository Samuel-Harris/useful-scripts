### IconButton Variants

Showing the different variants (ghost or filled) available for styling the IconButton.

```tsx
import React from "react";
import { AddIcon, IconButton } from "@firecms/ui";

export default function IconButtonVariantDemo() {
    return (
        <>
            <IconButton variant="ghost" onClick={() => console.log('Ghost Clicked!')}>
                <AddIcon />
            </IconButton>
            <IconButton variant="filled" onClick={() => console.log('Filled Clicked!')}>
                <AddIcon />
            </IconButton>
        </>
    );
}

```
