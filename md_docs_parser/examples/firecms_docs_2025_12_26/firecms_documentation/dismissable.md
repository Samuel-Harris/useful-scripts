### Dismissable

Alerts can be dismissable when provided with the `onDismiss` callback function.

```tsx
import React, { useState } from "react";
import { Alert } from "@firecms/ui";

export default function DismissableAlertDemo() {
    const [visible, setVisible] = useState(true);
    return (
        <>
            {visible && (
                <Alert onDismiss={() => setVisible(false)} color="info">
                    This alert can be dismissed with the close button.
                </Alert>
            )}
        </>
    );
}

```

