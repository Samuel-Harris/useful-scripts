### Validation strategies
Prefer declarative validation in the property config when possible. You can still implement client‑side
guards in the field (e.g. ignore invalid keystrokes) but allow the central validation to surface errors.

Common patterns:
- Trim on blur but preserve user typing: keep raw input in local state, call `setValue` with cleaned value on blur.
- Async validation (e.g. uniqueness): debounce the check, set a transient local error, do not block typing.

