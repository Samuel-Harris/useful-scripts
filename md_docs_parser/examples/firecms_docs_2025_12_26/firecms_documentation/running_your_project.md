### Running your project

To run your project locally, you can run the following command, like any
other Vite project:

```
npm run dev
```
or

```
yarn dev
```

This will execute a version of your project that uses FireCMS backend to
store config data but runs locally.

You should be able to see your FireCMS instance in your browser, including all the configuration you
have already created in the Cloud version... Awesome!

If you want to deploy to FireCMS Cloud your module must export a
`FireCMSAppConfig` object. You can find more information about this object
in the [App config section](https://firecms.co/docs/app_config) reference.

:::important
Vite uses the default url `http://127.0.0.1:5173` for the development server
in versions of `node` < 18.0.0.
If you are using a version of node < 18.0.0, you will need to add this url to
the authorized domains in the Firebase console.
Firebase Auth will require to add this url to the authorized domains in the
Firebase console.
Alternatively, you can use the url `http://localhost:5173`.
:::

