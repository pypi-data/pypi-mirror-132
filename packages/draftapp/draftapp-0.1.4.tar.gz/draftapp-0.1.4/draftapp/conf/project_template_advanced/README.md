# Getting Started

## Setting Up Virtualenv
  ```sh
   virtualenv --python={python path} env
   ```

## Activating the virtual environment

  ```sh
   source env/bin/activate
   ```

## Initialize git repository

  ```sh
   git init
   ```
   
## Install the required packages

  ```sh
   make install
   ```
   ***Note***: Running `make install` before initializing git repository will cause 'pre-commit-config' to fail.

## Starting application server

### Run Flask development server (for development)
  ```sh
   make run
   ```

### Run Gunicorn server (for production)
  ```sh
   make gunicorn
   ```

## Open Application in Browser
* open `http://localhost:5000/application/api/docs#/` in browser to access Flasgger

### Running test cases

```sh
make test  # run test cases using pytest
```

### Running Python Lint

```sh
make lint 
```


### Building Docker Image of Application

```sh
make docker 
```

### Deploying Application to a K8s Cluster

* Navigate to `kubernetes_manifest` folder
* Run below command
```sh
kubectl apply -f .
```

