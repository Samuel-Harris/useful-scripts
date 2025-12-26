### Color

The `color` prop sets the color theme of the button. Possible values are `primary`, `secondary`, `text`, `error`, and `neutral`.

```tsx
import React from "react";
import { Button } from "@firecms/ui";

export default function ButtonColorDemo() {
    return (
        <div className={"flex flex-row gap-4 items-center justify-center"}>
            <Button color="primary">
                Primary
            </Button>
            <Button color="secondary">
                Secondary
            </Button>
            <Button color="text">
                Text
            </Button>
            <Button color="error">
                Error
            </Button>
            <Button color="neutral">
                Neutral
            </Button>
        </div>
    );
}

```

