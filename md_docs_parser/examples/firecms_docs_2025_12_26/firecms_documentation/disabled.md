### Disabled

Setting `disabled` to `true` disables the button, preventing interactions.

```tsx
import React from "react";
import { Button } from "@firecms/ui";

export default function DisabledButtonDemo() {
    return (
        <div className={"flex flex-row gap-4 items-center justify-center"}>
            <Button disabled>
                Disabled Button
            </Button>
        </div>
    );
}

```

