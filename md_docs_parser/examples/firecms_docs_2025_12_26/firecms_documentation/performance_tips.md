### Performance tips
- Debounce network or expensive computations (`useEffect` + `setTimeout` or a utility) instead of per‑keystroke.
- Memo heavy child components based on relevant props.
- Avoid storing large derived objects in state; derive them on render or memoize.

