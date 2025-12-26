### Custom Class Name

The `className` prop allows you to pass custom CSS classes to the button component.

```tsx
import React from "react";
import { Button } from "@firecms/ui";

export default function CustomClassNameButtonDemo() {
    return (
        <div className={"flex flex-row gap-4 items-center justify-center"}>
            <Button className="bg-red-500 hover:bg-red-600 border-red-600 hover:ring-red-600">
                Button with Custom Class
            </Button>
        </div>
    )
}

```

