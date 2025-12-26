### Indeterminate State

Example of a switch that toggles between `true`, `false`, and `null` (indeterminate).

```tsx
import React, { useState } from "react";
import { BooleanSwitch } from "@firecms/ui";

export default function BooleanSwitchIndeterminateDemo() {
    const [value, setValue] = useState<boolean | null>(null);
    return (
        <BooleanSwitch
            value={value}
            allowIndeterminate={true}
            onValueChange={setValue}
        />
    );
}

```

