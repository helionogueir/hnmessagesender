# hnmessagesender
Message Sender API with JWT key.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Introduction 
Step by step to create environment for application execution. The instructions below are for Linux OS.

## Getting Started
1.	Install Docker
2.	Prepare Containers
3.	Execute Application

## Contribute
- [Helio Nogueira](mail:helio.nogueir@gmail.com)

---
## 1. Install Docker
For install Docker, follow the instructions in [Docker](https://www.docker.com/community-edition#/download).

---
## 2. Prepare Containers
Instructions for preparing application containers.

### 2.1. Packages
```bash
$ mkdir -p "${HOME}/workspace"
$ cd "${HOME}/workspace"
$ git clone "https://github.com/helionogueir/hnmessagesender.git"
$ cd "${HOME}/workspace/hnmessagesender"
$ cp "config.example.json" "config.json" 
```

### 2.2. Database Container
Follow the instructions below.

```bash
$ docker run \
    --name "hnmessagesender" \
    --volume "${HOME}/workspace/hnmessagesender":/var/www/application \
    --tty --interactive python:2.7 /bin/bash
```

## 3. Execute Application
Here you will prepare and execute the application. Follow the instructions below. You need connected on container "hnmessagesender".

```bash
$ cd "/var/www/application"
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```