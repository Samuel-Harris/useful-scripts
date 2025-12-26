### Troubleshooting & gotchas
- Value not updating: Ensure you call `setValue` (not mutate `value` directly) and that you don't shadow the `value` in local state without syncing.
- Error never shows: Remember `showError` gates visual display; `error` can exist while `showError` is false.
- Cross‑field updates ignored: Use the exact property key (e.g. `address.street`, array indexes like `items[0].price`).
- Field re-renders too often: Wrap heavy logic in `useMemo` / `useCallback`, avoid creating new objects every render.
- Need read‑only mode: Respect `disabled` from props or `context.disabled`.

