### Creating a Custom Storage Source

A custom storage source in FireCMS is defined by implementing the `StorageSource` interface.
Here is a template for creating a custom storage source.

Beware: This is an example on how you can implement and use S3, directly from a custom storage source.
This is not the preferred way of using S3 since it'd discourage to consume it directly from the frontend.
As you will have to insert the API key and secret in the frontend, which is not secure.
Instead, you could use [Amplify/Storage](https://docs.amplify.aws/react/build-a-backend/storage/) or a custom IAM auth.

Below is a template for creating a custom storage source:

```tsx

export interface S3StorageSourceProps {
  apiKey: string;
  apiSecret: string;
  region: string;
  defaultBucket?: string;
}

function initializeCustomClient({apiKey, apiSecret, region, defaultBucket}: S3StorageSourceProps) {
  const s3Client = new S3Client({region, credentials: {accessKeyId: apiKey, secretAccessKey: apiSecret}});

  return {
    uploadFile: async (destinationPath: string, file: File, bucket?: string, metadata?: any) => {
      await s3Client.send(new PutObjectCommand({
        Bucket: bucket || defaultBucket,
        Key: destinationPath,
        Body: file,
        ContentType: metadata?.contentType,
        Metadata: metadata
      }));
      return {
        path: destinationPath,
        bucket: bucket || defaultBucket || ""
      }
    },
    getFile: async (path: string, bucket?: string) => {
      return await s3Client.send(new GetObjectCommand({
        Bucket: bucket || defaultBucket || "",
        Key: path
      }));
    },
    getDownloadURL: async (path: string, bucket?: string) => {
      const command = new GetObjectCommand({Bucket: bucket || defaultBucket, Key: path});
      return await getSignedUrl(s3Client, command, {expiresIn: 3600});
    },
    getMetadata: async (path: string, bucket?: string) => {
      const s3Object = await s3Client.send(new GetObjectCommand({
        Bucket: bucket || defaultBucket,
        Key: path
      }));
      return {
        bucket: (bucket || defaultBucket) ?? "",
        fullPath: path,
        name: path,
        size: s3Object.ContentLength || 0,
        contentType: s3Object.ContentType || "",
        customMetadata: s3Object.Metadata || {}
      }
    }
  };
}

export function useCustomStorageSource(props: S3StorageSourceProps): StorageSource {
  // Initialize your storage client based on the props provided
  // For example, it could be a client for Amazon S3, Google Cloud Storage, etc.
  const customClient = initializeCustomClient(props);

  return {
    async uploadFile({file, fileName, path, metadata, bucket}: UploadFileProps): Promise<UploadFileResult> {
      const usedFilename = fileName ?? file.name;
      const destinationPath = `${path}/${usedFilename}`;
      // Logic to upload file using your storage client
      return await customClient.uploadFile(destinationPath, file, bucket, metadata);
    },

    async getFile(path: string, bucket?: string): Promise<File | null> {
      const targetBucket = bucket ?? props.defaultBucket;
      try {
        // Logic to retrieve the file using your storage client
        const fileData = await customClient.getFile(path, targetBucket);
        if (fileData && fileData.Body) {
          const byteArray = await fileData.Body.transformToByteArray();
          const blob = new Blob([byteArray], {type: fileData.ContentType});
          return new File([blob], path);
        } else {
          return null;
        }
      } catch (e) {
        return null; // File not found
      }
    },

    async getDownloadURL(path: string, bucket?: string): Promise<DownloadConfig> {
      const targetBucket = bucket || props.defaultBucket;
      try {
        // Logic to get the download URL using your storage client
        const url = await customClient.getDownloadURL(path, targetBucket);
        const metadata = await customClient.getMetadata(path, targetBucket);
        return {url, metadata};
      } catch (e) {
        return {url: null, fileNotFound: true};
      }
    }
  };
}
```

