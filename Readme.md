# **# Flask + MySQL Helm Project**



A simple \*\*Flask web application connected to a MySQL database\*\*, deployed on \*\*Kubernetes\*\* using \*\*Helm\*\*.  



This project demonstrates:



\- Running a Flask app inside a Kubernetes pod

\- Connecting Flask to a MySQL database

\- Using Helm charts for deployment

\- Exposing the Flask app via NodePort



---



### **## Architecture Diagram**



&nbsp;      +-----------------+

&nbsp;      |   Browser/User  |

&nbsp;      +--------+--------+

&nbsp;               |

&nbsp;               v

&nbsp;      +-----------------+

&nbsp;      |  Flask Service  |  <-- NodePort exposes this externally

&nbsp;      +--------+--------+

&nbsp;               |

&nbsp;               v

&nbsp;      +-----------------+

&nbsp;      | Flask Pod       |

&nbsp;      | app.py          |

&nbsp;      +--------+--------+

&nbsp;               |

&nbsp;               v

&nbsp;      +-----------------+

&nbsp;      | MySQL Service   |  <-- ClusterIP internal service

&nbsp;      +--------+--------+

&nbsp;               |

&nbsp;               v

&nbsp;      +-----------------+

&nbsp;      | MySQL Pod       |

&nbsp;      | mydb database   |

&nbsp;      +-----------------+



---



### **## Folder Structure**



flask-mysql-chart/

|-- Chart.yaml

|-- values.yaml

|-- templates/

| |-- flask-deployment.yaml

| |-- flask-service.yaml

| |-- mysql-deployment.yaml

| -- mysql-service.yaml |-- app/ |-- app.py -- Dockerfile





---



### **## Features**



\- Waits for MySQL to be ready before starting Flask

\- Environment variables configured via Helm `values.yaml`

\- NodePort service exposes Flask externally

\- Simple route `/` returns database tables in JSON format



---



### **## Prerequisites**



\- Docker installed

\- Kubernetes cluster or KillerCoda lab environment

\- Helm installed

\- GitHub account (optional, for sharing code)



---



### **## Step 1: Build Docker Image**



```bash

cd app

docker build -t <dockerhub-username>/flaskapp:latest .

docker push <dockerhub-username>/flaskapp:latest

Replace <dockerhub-username> with your Docker Hub username.



### **Step 2: Configure Helm Chart**



Edit values.yaml:



flask:

&nbsp; image: "<dockerhub-username>/flaskapp:latest"

&nbsp; replicas: 1

&nbsp; port: 5000



mysql:

&nbsp; image: "mysql:latest"

&nbsp; port: 3306

&nbsp; rootPassword: "admin"

&nbsp; database: "mydb"

&nbsp; user: "admin"

&nbsp; password: "admin"

### 

### **Step 3: Deploy with Helm**



helm uninstall flaskapp  # remove previous deployment if any

helm install flaskapp flask-mysql-chart

kubectl get pods

kubectl get svc

Wait until both mysql and flask-app pods are Running



Access Flask app via NodePort (default 30001) or KillerCoda preview





### **Step 4: Test Flask App**



Visit the NodePort URL or preview in KillerCoda. The output will look like:



{

&nbsp; "message": "Flask + MySQL working!",

&nbsp; "tables": \[]

}



"tables" will display all tables in the MySQL database



Confirms that Flask is connected to MySQL successfully

### 

### **Step 5: Helm Chart Files**



flask-deployment.yaml: Flask deployment with an initContainer waiting for MySQL



flask-service.yaml: NodePort service exposing Flask externally



mysql-deployment.yaml: MySQL deployment



mysql-service.yaml: ClusterIP service for internal MySQL communication



Notes

Minimal working example; frontend is JSON-only (no buttons or forms yet)



Environment variables managed via Helm values.yaml



Flask retries connecting to MySQL if the database isn’t ready initially

