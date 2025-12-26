### Date-Time Selection

Enables selection of both date and time, suitable for scenarios where precise timing is crucial.

```tsx
import React, { useState } from "react";
import { DateTimeField } from "@firecms/ui";

export default function DateTimeFieldDateTimeDemo() {
    const [selectedDateTime, setSelectedDateTime] = useState<Date | undefined>(new Date());

    return (
        <DateTimeField
            value={selectedDateTime}
            onChange={setSelectedDateTime}
            label="Select date and time"
            mode="date_time"
        />
    );
}

```

