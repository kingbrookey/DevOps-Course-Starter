# To-Do App Setup with Minikube

This README provides step-by-step instructions for setting up Minikube and running the To-Do app on it.

## Prerequisites

1. **Install Minikube**:
   - Follow the [Minikube installation guide](https://minikube.sigs.k8s.io/docs/start/) to install Minikube for your operating system.

2. **Install kubectl**:
   - Follow the [kubectl installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/) to install kubectl, the command-line tool for interacting with Kubernetes clusters.

## Setup Instructions

```bash
# 1. Start Minikube
minikube start

# 2. Verify Minikube Installation
kubectl cluster-info

## Create the Kubernetes Secrets
Save the following YAML content as secrets.yaml:

```bash

apiVersion: v1
kind: Secret
metadata:
  name: mod-14-secrets
type: Opaque
data:
  API_KEY: <BASE64_ENCODED_API_KEY>
  API_TOKEN: <BASE64_ENCODED_API_TOKEN>
  database_password: <BASE64_ENCODED_DATABASE_PASSWORD>
  mongodb_connectionstring: <BASE64_ENCODED_MONGODB_CONNECTIONSTRING>
  MONGODB_CONNECTION_STRING: <BASE64_ENCODED_MONGODB_CONNECTION_STRING>
  SECRET_KEY: <BASE64_ENCODED_SECRET_KEY>
  LOGGLY_TOKEN: <BASE64_ENCODED_LOGGLY_TOKEN>
  ARM_SUBSCRIPTION_ID: <BASE64_ENCODED_ARM_SUBSCRIPTION_ID>
  ARM_TENANT_ID: <BASE64_ENCODED_ARM_TENANT_ID>
  ARM_CLIENT_ID: <BASE64_ENCODED_ARM_CLIENT_ID>
  ARM_CLIENT_SECRET: <BASE64_ENCODED_ARM_CLIENT_SECRET>

```
Replace the placeholders (<BASE64_ENCODED_...>) with the actual base64-encoded values. Apply the secret with:

```bash
kubectl apply -f secrets.yaml
```

## Create the Deployment
Save the following YAML content as deployment.yaml:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: module-14
spec:
  selector:
    matchLabels:
      app: module-14
  replicas: 1
  template:
    metadata:
      labels:
        app: module-14
    spec:
      containers:
        - name: my-todo-app-mod8
          image: my-todo-app-mod8:latest
          imagePullPolicy: Never
          ports:
            - containerPort: 80
          env:
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: API_KEY
            - name: API_TOKEN
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: API_TOKEN
            - name: database_password
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: database_password
            - name: mongodb_connectionstring
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: mongodb_connectionstring
            - name: MONGODB_CONNECTION_STRING
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: MONGODB_CONNECTION_STRING
            - name: LOGGLY_TOKEN
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: LOGGLY_TOKEN
            - name: ARM_SUBSCRIPTION_ID
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: ARM_SUBSCRIPTION_ID
            - name: ARM_TENANT_ID
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: ARM_TENANT_ID
            - name: ARM_CLIENT_ID
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: ARM_CLIENT_ID
            - name: ARM_CLIENT_SECRET
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: ARM_CLIENT_SECRET
            - name: DATABASE_NAME
              value: "terraformed-cosmos-db-mod12"
            - name: BOARD_ID
              value: "64a2a69fcc4da212f15c6cee"
            - name: DOING_LIST_ID
              value: "64a2a69fcc4da212f15c6cf6"
            - name: DONE_LIST_ID
              value: "64a2a69fcc4da212f15c6cf7"
            - name: TO_DO_LIST_ID
              value: "64a2a69fcc4da212f15c6cf5"
            - name: SECRET_KEY
              valueFrom:
                secretKeyRef:
                  name: mod-14-secrets
                  key: SECRET_KEY
            - name: FLASK_APP
              value: todo_app/app
          resources:
            requests:
              memory: "0.5Gi"
              cpu: "500m"
            limits:
              memory: "1Gi"
              cpu: "1"

```

Apply the deployment with

```bash
kubectl apply -f deployment.yaml
```

## Expose the Service
Save the following YAML content as service.yaml:

```bash
apiVersion: v1
kind: Service
metadata:
  name: module-14-service
spec:
  selector:
    app: module-14
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer

```

Apply the service with
```bash
kubectl apply -f service.yaml

```

## Access the Application
After each deployment, run the command below to link up our minikube Service with a port on localhost.

```bash
kubectl port-forward service/module-14 7080:80
```

Open http://localhost:7080/ in a browser to view the application.

```bash
minikube service module-14-service --url
```

## Troubleshooting
# Check Pod Status
```bash
kubectl get pods
```


# Check Logs
```bash
kubectl logs <pod-name>
```


# Access Minikube Dashboard
```bash
minikube dashboard
```

