### New UI collection schema editor

Until now, the collection schema was defined in the client-side code. This was
great for simple use cases, but it limited the flexibility of the library. For
example, it was not possible to customize collections from the UI, since they
were hard coded in the clients code.

In FireCMS Cloud, **the collection schema is stored in FireCMS backend**, but you are also able to define
your collections in code for greater flexibility. Your end users will be able to modify the
collection schema. Let's say you have a collection of `Posts` and you want to
add a new possible value for the enum `status`. You can now open the collection
editor and add the new value. Even better, FireCMS can find new values and add
them to your schema with one click!

You can still limit the properties that can be modified from the UI, and you
can also define the default values for new documents.

#### New data inference

Do you have a few collections in your project, and you want to get started
quickly? FireCMS can now **infer the schema from your data**. This means that
you can get started with FireCMS in a few minutes, without having to write a
single line of code.

