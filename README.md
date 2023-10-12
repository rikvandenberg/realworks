# Realworks

Dear developer, below you'll find some instructions to get started with deploying

## Prerequisites

- Docker Desktop
- KinD

> Note: I have run and verified this repository working in Windows 11

## Python application (Docker)

Here are the steps to build the application. This Docker image is required in the next steps when deploying to Kubernetes.

1. navigate to `src/api` directory
2. Build the docker image `docker build -f .\Dockerfile -t realworks-api .`

## K8s deployment

**TODO: ISTIO gateway**

1. Navigate to the `deployment` directory
2. Create a new cluster `kind create cluster`
3. Import the previously build image ` kind load docker-image realworks-api:latest`
4. Apply either the test or the product environments with their respective commands `kubectl apply -k test` or `kubectl apply -k prod`
5. Verify the deployment has succeeded and the pods are running. `kubectl get deployment`

```
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
test-api-deployment   4/4     4            4           18m
```
6. Enable the HTTP Proxy `kubectl proxy`
7. (For test) Navigate to http://localhost:8001/api/v1/namespaces/default/services/test-api-service/proxy/configs/message
8. (For prod) Navigate to http://localhost:8001/api/v1/namespaces/default/services/prod-api-service/proxy/configs/message