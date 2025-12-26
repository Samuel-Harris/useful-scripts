### Updating the imports

The main change is that the imports have changed. You need to update the imports in your project.
Before you would import everything from `firecms` (or even `@camberi/firecms`). Now you need to import from
different packages.
- All UI components are now in `@firecms/ui`. Everything including buttons, textfields, layouts, etc.
- The core of FireCMS is in `@firecms/core`. This includes the `FireCMSApp`, `FireCMSContext`, etc.
- All Firebase related code is in `@firecms/firebase`, including `useFirebaseAuthController`, `use` etc.
Most of the imports can be found in `@firecms/core`, so we recommend starting there.

