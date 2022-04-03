# Tree visualizer


_Steps to install in local machine_
## Pre-requisite:
    1. python3

## steps:
    1. Clone the repo
    2. Run command `python3 tree.py <absolute path>`

_Steps to isntall on docker environment_

##  Pre-requisite:
    1.Docker v20.10.7 +

## steps:
    1. Clone the repo
    2. Build image :- `sudo docker image build -t my-tree .`
    3. Run container in exec mode :- `sudo docker container run --rm -it my-tree /bin/sh`
    4. Run command `python3 tree.py <absolute path>`