### Size Variants

The `BooleanSwitch` component can have different sizes, controlled by the `size` prop.

```tsx
import React, { useState } from "react";
import { BooleanSwitch } from "@firecms/ui";

export default function BooleanSwitchSizeDemo() {
    const [value, setValue] = useState<boolean | null>(true);

    return (
        <>
            <BooleanSwitch
                value={value}
                size="small"
                onValueChange={setValue}
            />
            <BooleanSwitch
                value={value}
                size="medium"
                onValueChange={setValue}
            />
        </>
    );
}

```

