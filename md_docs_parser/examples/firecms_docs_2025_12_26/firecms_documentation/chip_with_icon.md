### Chip with Icon

Showcases how to use a chip with an icon for better user interaction or providing more information within the chip.

```tsx
import React from "react";
import { Chip, FaceIcon } from "@firecms/ui";

export default function ChipIconDemo() {
    return (
        <Chip icon={<FaceIcon size={"small"}/>}>
            Chip with Icon
        </Chip>
    );
}

```

