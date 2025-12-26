### Tailwind migration and performance improvements

Versions 1.0 and 2.0 of FireCMS were based on Material UI (mui). This was great
for getting started quickly, but it had some drawbacks. The main one was that
**performance was not great**. The styling solution of MUI is based on emotion
which resolves styles at runtime. This means that the browser has to do a lot of
work to resolve the styles. This is not a problem for small applications, but
it can be a problem for large applications.

In FireCMS 3.0 we have migrated to Tailwind CSS. This is a utility-first CSS
framework that allows us to generate a small CSS file with all the styles
resolved at build time. This means that the browser does not have to do any
work to resolve the styles, which results in a **much faster experience**. 🚀

