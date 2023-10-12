# Realworks

## Prerequisites

- Docker Desktop
- KinD

> I have run and verified this repository working in Windows 11 and Ubuntu 22.04

## Python application (Docker)

Here are the steps to build the application. This Docker image is required in the next steps when deploying to Kubernetes.

1. 

## K8s deployment

1. Create a new cluster `kind create cluster`
2. Import the previously build image ``

3. HTTP Proxy `kubectl proxy`
4. http://localhost:8001/api/v1/namespaces/default/services/test-api-service/proxy/config/
5. http://localhost:8001/api/v1/namespaces/default/services/prod-api-service/proxy/config/