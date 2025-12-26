### Migrating custom components (MUI)

FireCMS 3.0 is based on `tailwindcss` instead of `mui`.

Mui was great for the initial versions of FireCMS, but it was being a big performance bottleneck
and it was hard to customize.

The new version of FireCMS has built in almost 50 new components implemented with tailwindcss, that
mimic in a good way the material-ui components. You are encouraged to migrate your custom components
to the new format.

You can try replacing imports from `@mui/material` to `@firecms/ui` and will see that many things work out of the box.

#### Icons

Icons in FireCMS are based on the material icons. You can use all the material icons importing them just like in MUI.

```tsx

```

The prop `fontSize` is called `size` in FireCMS (because it just makes more sense, MUI).

#### Components that have no equivalent:
- `Box`: The box component is just a wrapper used by mui to apply styles. You can use a `div` instead, with some
tailwind classes.
Tip: ChatGPT is great at converting Box components to div with tailwind classes.
- `Link`: Use `a` instead.
- `FormControl`

#### Components that change behaviour (from MUI to FireCMS UI)
- `Menu` and `MenuItem`: Menu items do not have an id anymore. You can add an `onClick` props per menu item.
- `Select` does not use `labelId` anymore. Just add the label as a component in `label`.
- `SelectChangeEvent` is now `ChangeEvent<HTMLSelectElement>`
- `CircularProgress` size is a string instead of a number. You can use `size="small"` or `size="large"`.

#### Continue using MUI

However, if you want to keep using mui: you can still use the old components, but you will need to
install the `mui` package manually.

```
yarn add @mui/material @emotion/react @emotion/styled
```

If you need MUI icons, run:

```
yarn add @mui/icons-material
```


