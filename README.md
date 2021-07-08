# the-simplest-flask-app

This repo accompanies the post [the-simplest-flask-app]() on [The Purple Unicorn](). Check out the post! 


## Run the app locally 
This runs a local rest microservice expose on port 9000. 
```bash
seldon-core-microservice MyModel --service-type MODEL
```

## Build Docker Image 
```bash
docker build . -t the-simplest-flask-app:0.1
```

## Run Docker Image
This runs your docker image exposed on port 9000. 
```bash
docker run --name "simple-app" -p 9000:9000 the-simplest-flask-app:0.1
```