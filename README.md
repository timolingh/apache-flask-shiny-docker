Most of the components of this repo were sourced from:
[Craicerjack/apache-flask](https://github.com/Craicerjack/apache-flask)

## Run it out of the box
Build the container image
```
docker build -t apache-flask-shiny .
```

Run the container with this command
```
docker run -d -p:80:80 --name flask apache-flask-shiny
```

## Build this to connect to a user defined network
Create the network
```
docker network create my-net
```

Build the container image with network options
```
docker create --name flask \
  --network my-net \
  --publish 8080:80 \
  apache-flask-shiny

docker run flask
```
