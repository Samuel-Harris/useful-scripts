## Getting started

<video className="intro_video" loop autoPlay muted>
    <source src="/img/full_screen_dark.mp4" type="video/mp4"/>
</video>

:::important
FireCMS is an **open source headless CMS and admin panel**. It is a platform where you can build full companies, or your weekend side project.
:::

FireCMS uses [**Firebase**](https://firebase.google.com/) or **MongoDB Atlas** as a **backend**. You are the **owner**
of your Firebase project, and FireCMS is a tool that helps you build your admin panel on top of it. FireCMS provides all
the editing options you lack in a simple Firebase project.

FireCMS creates **CRUD views** based on your configurations with ease. It's simple to set up for common cases and just
as easy to extend and customize to fit your specific needs.

FireCMS imposes **no data structure restrictions**, allowing seamless integration with any project right from the start.

FireCMS **3.0** is the latest version of FireCMS. It can be used in different ways:
- As a managed service in the Cloud: [**FireCMS Cloud**](https://app.firecms.co). In this version you can create and
manage your content in a user-friendly interface, and use it as a no-code tool, or extend its functionality with code.
- You also have self-hosted options in the [**PRO**](/pro) plan and community plan. In this versions, you need to deploy FireCMS to
your server, and you have full control over the code, with many customization options.

#### Navigation

FireCMS takes care of the **navigation** for you, it generates routes and menus based on the configuration that you set
up.

:::tip
The collections can be defined asynchronously, so you can fetch data from your backend to build them. It might be
useful if you want to build the collections based on the logged-in user, or if you want to fetch some data to build
the schema of your collections. Check the [**dynamic collections**](https://firecms.co/docs/collections/dynamic_collections) section
for more information.
:::

You have two main ways of creating the top-level views in FireCMS, either creating **entity collections** that get
mapped to CMS views, or create your own top-level **React views**:
- Check all the possible configurations for defining [**collections**](https://firecms.co/docs/collections)
- Otherwise, you can define your own [**custom top-level views**](https://firecms.co/docs/custom_top_level_views.mdx).

