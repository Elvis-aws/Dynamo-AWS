################################
# What is docker
################################
- A container bundles an applications code and dependencies into one object
- They use less resources
- Applications running in containers are isolated and separated from the host
################################
# Docker architecture
################################
  # Host
  - The host machine running docker
  # Docker client
  - This is where we execute docker commands such as
  - Docker build
  - Docker pull
  - Docker run
  # Docker engine
  - Consist of the rest api that the docker daemon listens to requests from the client
  # Docker daemon
  - This consist of a host of the below and receives commands via a rest api service and processes the requests
  - Containers
  - Images
  - Data volumes
  - Networks
  # Docker registry
  - For storing images
################################
# Downsides
################################
- Not all apps are supported to run in containers
################################
# Virtual machines vs Containers
################################
# Virtual machines (Hypervisors)
- It is a software that creates and runs virtual machines (VMs)
- It allows one host computer to support multiple guest VMs by virtually sharing its resources, such as memory and 
  processing
- Hypervisors operate at the hardware level
- Isolation of machines
- VMs are independent of each other
- They contain their own OS
- You have to assign RAM and Processors during VM creation, this reduces the efficiency of the host and resources are
  sometimes wasted as the app might not consume all the allocated resources on the VM
- VMs may be many gigabytes in size
- Each VM has its own libraries and binaries
# Containers
- They operate at the operating system level
- Process isolation
- They are running in the same environment
- They can share resources
- They are sharing the same OS and kernel as the host
- They feel as if they have their own OS
- They share resources with the host thus no resource wasting
- They control how much resource the container can access
- Each container share libraries and binaries with the host
- Containers may be only megabytes in size

################################
# Build docker image
################################
docker build -t dockerelvis/flask-demo:latest . 
docker build -t dockerelvis/flask-api-demo:0.0.1.RELEASE .
################################
# Build run image
################################
# -d detached mode so you can access terminal
# p port mapping host:container
# http://localhost:3000
docker container run -d -p 9002:9001 dockerelvis/flask-api-demo:0.0.1.RELEASE
docker container run -e AWS_PROFILE=default -v ~/.aws/:/root/.aws:ro -d -p 9002:9001 dockerelvis/flask-api-demo:0.0.1.RELEASE 
docker container run -d -p 9002:9001 dockerelvis/flask-api-demo:0.0.1.RELEASE -v ~/.aws/:/root/.aws:ro -e AWS_PROFILE=default


docker container run -e AWS_ACCESS_KEY_ID=AKIA5TEEY4RPPQ4HD46H -e AWS_SECRET_ACCESS_KEY=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 -e AWS_DEFAULT_REGION=eu-west-2 -d -p 9002:9001 dockerelvis/flask-api-demo:0.0.1.RELEASE
#ENV AWS_ACCESS_KEY_ID=AKIA5TEEY4RPPQ4HD46H                                                                                                127 ✘  bin   13:58:48
#ENV AWS_SECRET_ACCESS_KEY=1NYMUizrYOQiz4gJF3ytZNW284u3bQTi4W/8p86Q
#ENV AWS_DEFAULT_REGION=eu-west-2
export AWS_DEFAULT_PROFILE=default





################################
# View running containers
################################
docker container ls
################################
# Stop running container
################################
docker container stop <container name>
################################
# Docker push image
################################
docker push dockerelvis/flask-api-demo:0.0.1.RELEASE