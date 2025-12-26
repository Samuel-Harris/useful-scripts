### Usage with Icons and Buttons

Badges can be wrapped around icons or buttons to provide status indicators.

```tsx
import React from "react";
import { AnchorIcon, Badge, Button, IconButton } from "@firecms/ui";

export default function BadgeIconDemo() {
    return (
        <>
            <Badge color="error">
                <IconButton>
                    <AnchorIcon/>
                </IconButton>
            </Badge>

            <Badge color="secondary">
                <Button>
                    Fix
                </Button>
            </Badge>
        </>
    );
}

```

