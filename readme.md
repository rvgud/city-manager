About the Application
====
City-manager is a simple rest service written in python which allows below functionalities:

    1. Add a few sample cities in the database if there is no city in database on startup of application.
    2. Expose an api to get all the cities and their population
    3. Expose an api to add a new city or update any existing city 
    4. Expose an api to get the population of any city
    4. Expose an api to get the health of the service which returns 'OK'

Perform below steps in order to run this application:
====


Install Docker as Runtime 
=====
https://docs.docker.com/get-docker/

Build And publish docker image
=====
docker build -t city-manager .

Docker image is available at docker.io/singhravindra/city-manager



Install minikube
=====

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    minikube addons enable default-storageclass
    minikube addons enable storage-provisione


Install Helm 3
=====
    https://helm.sh/docs/intro/install/

Install Elasticsearch Cluster
=====
    helm repo add elastic https://helm.elastic.co
    helm install elasticsearch elastic/elasticsearch -f ElasticSearch/values.yaml

Install City-Manager 
=====
    helm upgrade city-manager Helm/city-manager --install

To Access the city-manager apis
=====

    minikube ip -> Note down the ip
    kubectl get svc city-manager -o=jsonpath="{.spec.ports[0].nodePort}" -> note down the NodePort

Health API:
=
    <minikube_ip>:<node_port>/health

Cities API(Get all the cities)
=====
    <minikube_ip>:<node_port>/cities

City API(Insert/update any city)
=====

    curl -X PUT \
    http://<minikube_ip>:<node_port>/city/ \
    -d '{"_id":"fjkfjsakjfkfkaf","_index":"cities","_source":{"city_name":"city9","population":900}}'

Population API(To get population of any city)
=====
    http://<minikube_ip>:<node_port>/population/<city_id>

