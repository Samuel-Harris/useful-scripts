### MongoDB Atlas Configuration

Begin by setting up your MongoDB Atlas project and obtaining the required configuration parameters.
These parameters include `appId`, `appUrl`, `baseUrl`, `clientApiBaseUrl`, `dataApiBaseUrl`, `dataExplorerLink`,
and `dataSourceName`.

```js
const atlasConfig = {
  appId: "your-app-id",
  appUrl: "https://services.cloud.mongodb.com/groups/your-group-id/apps/your-app-id",
  baseUrl: "https://services.cloud.mongodb.com",
  clientApiBaseUrl: "https://your-region.gcp.services.cloud.mongodb.com",
  dataApiBaseUrl: "https://your-region.gcp.data.mongodb-api.com",
  dataExplorerLink: "https://cloud.mongodb.com/links/your-group-id/explorer/Cluster0/database/collection/find",
  dataSourceName: "mongodb-atlas"
};
```

