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
    helm3 install elasticsearch elastic/elasticsearch -f ElasticSearch/values.yaml

Install City-Manager 
=====
    helm3 upgrade city-manager Helm/city-manager --install

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

