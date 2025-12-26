### Checkbox with Indeterminate State

A checkbox that showcases the indeterminate state, typically used for 'select all' scenarios where not all sub-selections are made.

```tsx
import React, { useState } from "react";
import { Checkbox } from "@firecms/ui";

export default function CheckboxIndeterminateDemo() {
    const [indeterminate, setIndeterminate] = useState(true);
    const [checked, setChecked] = useState(false);

    return (
        <Checkbox
            checked={checked}
            indeterminate={indeterminate}
            onCheckedChange={(newChecked) => {
                if (indeterminate) {
                    setIndeterminate(false);
                    setChecked(true);
                } else if (checked) {
                    setChecked(false);
                } else {
                    setIndeterminate(true);
                }
            }}
        />
    );
}

```

