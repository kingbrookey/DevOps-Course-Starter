**To do application encryption**

Our todo_application leverages Azure Cosmos DB as its database solution. We prioritize data security and compliance with industry standards. As such, we have implemented encryption measures to safeguard sensitive data stored in Cosmos DB.

**Encryption at rest:** Cosmos DB automatically encrypts data at rest using Transparent Data Encryption (TDE). This feature helps protect data by encrypting it while stored on disk.

**Encryption in transit:** Cosmos DB ensures secure communication between the application and the database using Transport Layer Security (TLS) encryption.

**Note:** While we do not currently utilize Azure Key Vault integration, we are actively evaluating its implementation to further enhance our encryption key management strategy.

For detailed information on encryption features and best practices in Cosmos DB, refer to the [official Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/database-encryption-at-resturl).
