### Controlled Menu

You can control the visibility of the `Menu` component by passing the `open` and `onOpenChange` props.

```tsx
import React from "react";
import { Button, Menu, MenuItem } from "@firecms/ui";

export default function MenuCustomTriggerDemo() {

    const [open, setOpen] = React.useState(false);

    return (
        <Menu
            onOpenChange={setOpen}
            open={open}
            trigger={
                <Button onClick={() => setOpen(true)}>Click me</Button>
            }>
            <MenuItem onClick={() => alert("Action 1")}>Action 1</MenuItem>
            <MenuItem onClick={() => alert("Action 2")}>Action 2</MenuItem>
            <MenuItem onClick={() => alert("Action 3")}>Action 3</MenuItem>
        </Menu>
    );
}

```

