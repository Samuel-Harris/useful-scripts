### Clickable Card

Shows a card that has an onClick event, making it behave similar to a button.

```tsx
import React from "react";
import { Card } from "@firecms/ui";

export default function CardClickableDemo() {
    const handleClick = () => {
        console.log("Card clicked!");
    };

    return (
        <Card className={"p-4"} onClick={handleClick}>
            Clickable card content.
        </Card>
    );
}

```

