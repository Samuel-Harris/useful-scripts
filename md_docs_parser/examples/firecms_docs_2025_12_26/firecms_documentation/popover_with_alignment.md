### Popover with Alignment

Showcasing how to align the popover content relative to the trigger element.

```tsx
import React from "react";
import { Button, Popover } from "@firecms/ui";

export default function PopoverAlignDemo() {
    return (
        <div>
            <Popover
                trigger={<Button>Open Left</Button>}
                side="left"
            >
                <div className="p-4">
                    Aligned to the left.
                </div>
            </Popover>
            <Popover
                trigger={<Button>Open Bottom</Button>}
                side="bottom"
            >
                <div className="p-4">
                    Aligned to the bottom.
                </div>
            </Popover>
        </div>
    );
}

```

