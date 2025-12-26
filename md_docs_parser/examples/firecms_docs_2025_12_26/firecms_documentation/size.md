### Size

The prop `size` can be used to change the size of the button.

Buttons come in three sizes: `small`, `medium`, `large`, `xl` and `2xl`.

```tsx
import React from "react";
import { Button } from "@firecms/ui";

export default function ButtonSizeDemo() {
    return (
        <>
            <Button
                size={"small"}
                onClick={() => console.log("Button clicked")}>
                Small
            </Button>
            <Button onClick={() => console.log("Button clicked")}>
                Medium
            </Button>
            <Button
                size={"large"}
                onClick={() => console.log("Button clicked")}>
                Large
            </Button>
            <Button
                size={"xl"}
                onClick={() => console.log("Button clicked")}>
                XLarge
            </Button>
            <Button
                size={"2xl"}
                onClick={() => console.log("Button clicked")}>
                XXLarge
            </Button>
        </>
    );
}

```

