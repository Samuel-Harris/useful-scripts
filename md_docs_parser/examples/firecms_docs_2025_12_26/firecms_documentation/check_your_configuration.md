### Check your configuration

FireCMS Cloud can share dependencies with your uploaded app. It is important than your app and FireCMS Cloud use the same version of Firebase App Check.
In order to do so, make sure, in your `vite.config.ts`, you are using the shared dependency provided by FireCMS.
You need to have the dependency `@firebase/app-check` in your `vite.config.ts`. Federation plugin `shared` configuration.

This is a sample configuration:

```tsx

// https://vitejs.dev/config/
export default defineConfig({
    esbuild: {
        logOverride: { "this-is-undefined-in-esm": "silent" }
    },
    plugins: [
        react(),
        federation({
            name: "remote_app",
            filename: "remoteEntry.js",
            exposes: {
                "./config": "./src/index"
            },
            shared: [
                "react",
                "react-dom",
                "@firecms/cloud",
                "@firecms/core",
                "@firecms/firebase",
                "@firecms/ui",
                "@firebase/firestore",
                "@firebase/app",
                "@firebase/functions",
                "@firebase/auth",
                "@firebase/storage",
                "@firebase/analytics",
                "@firebase/remote-config",
                "@firebase/app-check" // Add this line
            ]
        })
    ],
    build: {
        modulePreload: false,
        minify: false,
        target: "ESNEXT",
        cssCodeSplit: false,
    }
});
```

