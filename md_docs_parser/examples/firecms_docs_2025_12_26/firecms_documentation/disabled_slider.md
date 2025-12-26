### Disabled Slider

Illustrating how to use the `disabled` prop to create a non-interactive Slider.

```tsx
import React from "react";
import { Slider } from "@firecms/ui";

export default function SliderDisabledDemo() {
    return (
        <Slider
            value={[30]}
            min={0}
            max={100}
            disabled
        />
    );
}
```

