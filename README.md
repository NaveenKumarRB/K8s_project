minikube start
![alt text](image-6.png)
kubectl get nodes
![alt text](image-7.png)
kubectl apply -f k8s/
![alt text](image-8.png)
kubectl get pods
![alt text](image-9.png)
kubectl get svc
![alt text](image-10.png)

git init
git add .
git commit -m "Kubernetes deployment with Minikube"
git branch -M main
git remote add origin https://github.com/NaveenKumarRB/K8s_project.git

git push -u origin main

# Flask + Node.js Kubernetes Deployment

## Technologies Used

- Flask
- Node.js
- Docker
- Kubernetes
- Minikube

## Start Minikube

```bash
minikube start


output
![alt text](image-11.png)

![alt text](image-12.png)