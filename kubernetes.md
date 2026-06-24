`kubectl version` # Print the client and server version information, check kubectl version

`minikube version` # Single node kubernetes cluster, check minikube version

`kubectl cluster-info dump` # Print cluster information, `dump` for verbose details


### Kubectl Create Object
`kubectl create -f <object.yaml>` # Create any kubernetes object from manifest file

`kubectl create -f pod.yaml` # Create a pod using the data in pod file

`kubectl apply -f pod.yaml` # Create a pod or apply a change based on pod manifest file

`cat pod.yaml | kubectl create -f -` # Create a pod based on yaml ppassed into stdin

`kubectl run <pod-name> --image=<image-name>:<tag-name>` # Create a pod imperatively

`kubectl get pods`# Print a list of pods

`kubectl get pods -o wide` # Print a list of pods including additional details like nodes

`kubectl describe <pod-name>` # Detailed information of pods

`kubectl delete pod <pod-name>` # Delete a pod

`kubectl delete -f <pod.yaml>`# Delete a pod

`kubectl create -f <replicationController.yaml>` # Create replication controller

`kubectl get rc` # List replication controller

`kubectl describe rs/<rc-name>` # Detailed information about replication controller

`kubectl delete -f <replicationController.yaml>` # Delete a replication controller

`kubectl create -f <replicaset.yaml>` # Create a replicaset

`kubectl get replicaset` # List replicaset

`kubectl describe rs<replicaset-name>` # Detailed information about replicaset

`kubectl scale --replicas=N -f <replicaset.yaml>` # Scale replicas of replicaset

`kubectl scale --replicas=N replicaset <replicaset-name>` # Scale replicas of replicaset

`kubetl edit replicaset <replicaset-name>` # Edit runtime replicaset manifest file

`kubectl delete -f <replicaset.yaml>` # Delete a replicaset

`kubectl create -f <deployment.yaml>` # Create a deployment from manifest file, `--record` optional to record revision

`kubectl get deployment` # List deployment

`kubectl describe deployment <deployment-name>` # Detailed information about deployment

`kubectl delete -f <deployment.yaml>` # Delete a deployment with manifest file

`kubectl set image deployment/<deployment-name> <old-image>=<new-image>` # Change image in existing deployment

`kubectl rollout status deployment/<deployment-name>` # Check status of rollout

`kubectl rollout history deployment/<deployment-name>` # Check history of existing rollout

*Deployment Strategies*
- Recreate
- Rolling Updates

#### Networking 
*Types of Service*
- ClusterIP
- NodePort
- LoadBalancer
- ExternalName

`kubectl create -f <service.yaml>` # Create a service

`kubectl get service` # List services

`kubectl describe service <service-name>` # Detailed information of service

`kubectl delete -f <service.yaml>` # Delete a service

`kubectl create -f <configMap.yaml>` # Create a configMap

`kubectl create configmap <configmap-name> --from-literal=<KEY>:<VALUE>` # Create a configmap imperatively

`kubectl create configmap <configmap-name> --from-file=<config-filename>` # Create a configmap from a file

`kubectl get configmaps` # List configmaps

`kubectl delete -f <configMap.yaml>` # Delete a configMap

`kubectl delete configmap <configmap-name>` # Delete a configMap

`kubectl create -f <secret.yaml>` # Create a secret 

`kubectl create secret generic <secret-name> --from-literal=<key>:<value>` # Create a secret from values

`kubectl create secret generic <secret-name> --from-file=<key>:<value>` # Create a secret from file

`kubectl get secrets` # List all secrets

`kubectl describe secret <secret-name>` # Inspect secret details in encoded, `-o yaml` for full original value

`kubectl delete secret <secrt-name>` # Delete a secret

`kubectl delete -f <secret.yaml>` # Delete a secret


`clusterrole` -> Create a cluster role
`clusterrolebinding` -> Create a cluster role binding for a particular cluster role
`configmap` -> Create a config map from a local file, directory or literal value
`cronjob` -> Create a cron job with the specified name
`deployment` -> Create a deployment with the specified name
`ingress` -> Create an ingress with the specified name
`job` -> Create a job with the specified name
`namespace` -> Create a namespace with the specified name
`poddisruptionbudget` -> Create a pod disruption budget with the specified name
`priorityclass` -> Create a priority class with the specified name
`quota` -> Create a quota with the specified name
`role` -> Create a role with single rule
`rolebinding` -> Create a role binding for a particular role or cluster role
`secret` -> Create a secret using a specified subcommand
`service` -> Create a service using a specified subcommand
`serviceaccount` -> Create a service account with the specified name
`token` -> Request a service account token

#### POD Manifest
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    tier: front-end
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
    - name: redis-container
      image: redis
    envFrom:
      - configMapRef:
          name: <configmap-name>
    envFrom:
      - secretRef:
          name: <secret-name>
    env:
      - name: <configmap-name>
        valueFrom:
          configMapRefKey:
            name: <key-name>
            key: <key-value>
    env:
      - name: <secret-name>
        valueFrom:
          secretKeyRef:
            name: <KEY>
            key: <VALUE>

---
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-rc
  labels:
    app: nginx
spec:
  replicas: 3                   # Desired number of pod replicas
  selector:
    app: nginx                  # MUST match template.labels
  template:
    metadata:
      labels:
        app: nginx              # MUST match spec.selector
    spec:
      containers:
      - name: nginx-container
        image: nginx           # Official nginx image
        ports:
        - containerPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    type: frontend
spec:
  replicas: 3
  selector: 
    matchLabels:
      app: myapp
  template:
    metadata:
      name: myapp-pod
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx-container
          image: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: NodePort
  selector:
    app: myapp
    type: frontend
  ports:
    - targetPort: 80
      port: 80
      nodePort: 30008
---
apiversion: v1
kind: Service
metadata:
  name: backend-service
spec:
  type: ClusterIP # default
  ports:
    - targetPort:80
      port: 80
  selector:
    app: myapp
    tier: frontend
---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: LoadBalancer
  selector:
    name: myapp
  ports:
    - targetPort: 80
      port: 80
      nodePort: 30008
---

apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  <KEY>: <VALUE>

---

apiVersion: v1
kind: Secrets
metadata:
  name: nginx-secret
data:
  <key>:<HASH-value>

*echo -n 'secret' | base64* # Convert secret into base64 value and add as HASH value

*echo -n 'encoded-secret' | base64 --decode* To decode encoded value