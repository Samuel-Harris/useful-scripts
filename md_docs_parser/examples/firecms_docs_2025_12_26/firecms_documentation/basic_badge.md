### Basic Badge

By setting the `invisible` prop to `true`, you can hide the badge, making it not visible to users.

```tsx
import React from "react";
import { Badge, Button, Chip } from "@firecms/ui";

export default function BadgeInvisibleDemo() {
    const [visible, setVisible] = React.useState<boolean | null>(true);
    return (
        <>
            <Badge color="primary" invisible={!visible}>
                <Chip>Content with Badge</Chip>
            </Badge>

            <Button onClick={() => setVisible(!visible)}>
                Toggle badge
            </Button>
        </>
    );
}

```

