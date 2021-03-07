# container-from-scratch-python
This is building a container from scratch

## Build the Container Yourself and Push to Docker Hub

### Build image
*(If you want to develop yourself)* 
docker build --tag=mx9606/docker-prac .

### List docker images
docker image ls

### Run my newly built container

docker run -it mx9606/docker-prac:dice_roller python app.py --minval 1 --maxval 6

### Push to Docker Hub

*Note:  You will need to change for your Docker Hub Repo*
docker push mx9606/docker-prac:tagname

## Run it yourself

```bash
docker pull mx9606/docker-prac:latest
docker run -it mx9606/docker-prac bash 

#then run python app.py --help
```

## Pass in a command

```bash
docker run -it mx9606/docker-prac:dice_roller python app.py --minval 1 --maxval 6
#the output
Hello User!
The minimum value is 1
The maximum value is 6
************************
ROLLING THE DICE
************************
The Result is 4
```

### More things Do

* Lint the code with Github Actions (see the Makefile)
* Automatically build the container after lint, and push to DockerHub or some other Container Registery



