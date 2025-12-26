### Chip Sizes

Illustrating how to use different sizes for the chip component. You can choose between `tiny`, `small`, and `medium`.

```tsx
import React from "react";
import { Chip } from "@firecms/ui";

export default function ChipSizesDemo() {
    return (
        <>
            <Chip size="small">Small Chip</Chip>
            <Chip size="medium">Medium Chip</Chip>
            <Chip size="large">Large Chip</Chip>
        </>
    );
}

```

