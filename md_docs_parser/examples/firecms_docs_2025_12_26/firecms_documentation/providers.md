### Providers

The `provider` property is required and should be an instance of a Firebase AppCheck provider.
You can use one of the following providers:

#### ReCaptchaEnterpriseProvider

In order to set up the ReCaptchaEnterpriseProvider, you need to create a new reCAPTCHA Enterprise site key.
Follow the instructions in the [Firebase documentation](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider).

:::important
Make sure you have added the domain `app.firecms.co` to the list of allowed domains in the reCAPTCHA Enterprise console.
:::

```tsx

const {
    loading,
    error,
    appCheckVerified
} = useAppCheck({
    options: {
        provider: new ReCaptchaEnterpriseProvider("your-site-key"),
        isTokenAutoRefreshEnabled: true,
    }
});
```

#### ReCaptchaV3Provider

In order to set up the ReCaptchaV3Provider, you need to create a new reCAPTCHA v3 site key.
Follow the instructions in the [Firebase documentation](https://firebase.google.com/docs/app-check/web/recaptcha-provider).

```tsx

const {
    loading,
    error,
    appCheckVerified
} = useAppCheck({
    options: {
        provider: new ReCaptchaV3Provider("your-site-key")
        isTokenAutoRefreshEnabled: true,
    }
});
```

#### Custom provider

You can also create a custom provider by implementing the `AppCheckProvider` interface.

