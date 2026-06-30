 Wisecow DevOps Assessment Project (Problem 1 + Problem 2)

This project is developed as part of the **Accuknox DevOps Trainee Practical Assessment**. It demonstrates a complete end-to-end DevOps workflow including containerization, CI/CD automation, Kubernetes deployment, and system/application monitoring using Python scripts.

---

Project Overview

This project implements a full DevOps pipeline covering:

- Application containerization using Docker
- Continuous Integration & Deployment using GitHub Actions
- Kubernetes deployment using Minikube
- Service exposure using NodePort
- System monitoring using Python scripts
- Application health checking using HTTP validation

---

 Architecture Flow



GitHub Repository
↓
GitHub Actions CI/CD
↓
Docker Image Build
↓
Docker Hub Registry
↓
Kubernetes Cluster (Minikube)
↓
Deployment + Service
↓
Running Application
↓
Monitoring Scripts



---

 Problem 1: Containerization, CI/CD & Kubernetes Deployment

 Dockerization

The application is containerized using Docker.

 Build Image
bash
docker build -t kavyaark/wisecow-app:latest .


 Run Container

bash
docker run -p 4499:4499 kavyaark/wisecow-app:latest


---

 CI/CD Pipeline (GitHub Actions)

A fully automated pipeline is implemented using GitHub Actions.

Features:

* Builds Docker image on every push to `main`
* Authenticates with Docker Hub
* Pushes image to Docker registry

Workflow File:


.github/workflows/ci-cd.yml


---

 Kubernetes Deployment

The application is deployed on a Kubernetes cluster using Minikube.

Apply Deployment

bash
kubectl apply -f k8s/


 Verify Resources

bash
kubectl get all


---

 Service Exposure

The application is exposed using a NodePort service.

* Service Type: NodePort
* Port Mapping: 4499:30449

 Access Application

bash
minikube service wisecow-service


OR


http://<minikube-ip>:30449


---
 Problem 1 Status

* ✔ Docker Image Build Completed
* ✔ CI/CD Pipeline Working
* ✔ Docker Hub Push Successful
* ✔ Kubernetes Deployment Running
* ✔ Service Exposed Successfully
* ✔ Application Accessible

---

 Problem 2: System Monitoring & Health Checks

This section includes Python scripts for system monitoring and application health verification.

---

 System Health Monitoring Script

This script monitors system performance metrics such as CPU usage, memory usage, disk usage, and running processes.

File: `system_health_monitor.py`

python
import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    print("=" * 50)
    print("System Health Report")
    print("Time:", datetime.now())
    print("=" * 50)
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")

    if cpu > CPU_THRESHOLD:
        print("ALERT: High CPU usage")

    if memory > MEMORY_THRESHOLD:
        print("ALERT: High Memory usage")

    if disk > DISK_THRESHOLD:
        print("ALERT: High Disk usage")

monitor_system()


 Run Script

bash
python3 system_health_monitor.py


---

 Application Health Checker

This script checks whether the Wisecow application is running by validating HTTP response codes.

File: `app_health_checker.py`

python
import requests

URL = "http://192.168.49.2:30449"

def check_application():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            print("Application Status: UP")
            print("HTTP Status Code:", response.status_code)
        else:
            print("Application Status: DOWN")
            print("HTTP Status Code:", response.status_code)

    except Exception as e:
        print("Application Status: DOWN")
        print("Error:", e)

check_application()


 Run Script

bash
python3 app_health_checker.py


---

 Problem 2 Status

* ✔ System Health Monitoring Completed
* ✔ Application Health Checker Completed
* ✔ Kubernetes Service Integration Verified

---

 Key Skills Demonstrated

* Docker containerization
* GitHub Actions CI/CD automation
* Kubernetes deployment (Minikube)
* Linux system monitoring
* Python automation scripting
* Application health monitoring
* DevOps debugging & troubleshooting



 Final Outcome

This project demonstrates a complete DevOps lifecycle:

Code → Docker → CI/CD → Docker Hub → Kubernetes → Running Application → Monitoring


