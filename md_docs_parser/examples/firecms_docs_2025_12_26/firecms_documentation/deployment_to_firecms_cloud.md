### Deployment to FireCMS Cloud

FireCMS is unique among CMSs in that it allows to upload custom code to
its Cloud version. This is a very advanced feature enables you to tailor
the CMS according to your requirements.

The code is bundled and compiled using **module federation** and
**vite**. This means that you can use any npm package you want to build your CMS.
The bundle will not include any of the dependencies that are already
included in FireCMS, so you can use any version of any package you want.

Deploy your code to [FireCMS Cloud](https://app.firecms.co) with a single command,
and it will be served from there:

```bash
yarn deploy
```

The benefit of this approach is that you can use any npm package you want,
and you can use the latest version of FireCMS without having to manually
update your code.

#### FireCMS CLI

The FireCMS CLI is a tool that allows you to deploy your CMS to FireCMS Cloud
with a single command. In your project, you should have `firecms` as a dev
dependency. This package was previously `@firecms/cli`.

The available commands are:

```bash
firecms login
```

```bash
firecms logout
```

and

```bash
firecms deploy --project=your-project-id
```

