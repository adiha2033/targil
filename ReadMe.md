<h1 class="title">
    Targil Project:
</h1>

<h3 id="menu" style="text-decoration:underline">
Main Menu:
</h3>

This project is an exercise who has 3 components

- [Dockefile](#docker)
- [Python Application](#python)
- [Jenkins Pipelines](#jenkins)

<br>

<h3 id="docker" style="text-decoration:underline">Dockerfile:</h3>

This Sction is about the Dockerfile to build our docker image

We use Ubuntu 20.04 (Xenail) for base as you can see in down below:
```dockerfile
FROM ubuntu:xenial
```

After that we inset argument `VERSION` inside Dockerfile who has a default argument `1.2.0` (application version number), this argument will inset to environment variable, as you can see down below:
```dockerfile
ARG VERSION="1.2.0"
ENV VERSION=${VERSION}
```

Now we need to install all relevant packages to allow application to run without issue, as we can see below.
```dockerfile
RUN apt-get clean && apt-get update
RUN apt-get install -y \
    vim \
    zip \
    unzip \
    python3
```

in this part we copy our application to conatiner, as we can see below. 
```dockerfile
COPY zip_job.py /tmp
```

Finally, we print OS deatils and check if file is exsits after copt it, s we can see below. 
```dockerfile
CMD cat /etc/lsb-release && ls /tmp/zip_job.py
```

This all part of our Dockerfile you can find in our repository [Dockerfile](/Dockerfile)

<br>

<h3 id="python" style="text-decoration:underline">Python Application:</h3>

This Section is about our python application name zip_job.py who will create files and zip files.<br><br>
this python application use the follow modules for work [`logging`, `errno`, `os`, `zipfile`], as you can see down below.

```python
import os
import errno
from zipfile import ZipFile
import logging
```

in side the python application we are verify the environment variable `VERSION` who came from our docker image.

```python
if "VERSION" not in os.environ:
    exit(200)

version = os.getenv("VERSION")
```

the main action of this python application is in the loop who take the array who is contian ['a','b','c','d'] and create from them  text file base their names and verify the files exist, <br>
After that it will create zip files who base arr names and `VERSION` and take the text file and zip it and verify the zip files exist, as you can see below:

```python
    fileName = "{}.txt".format(name)
    zipName = "{}_{}.zip".format(name, version)

    if os.path.isfile(fileName):
        log.info("{} is already exists".format(fileName))
    else:
        with open(fileName, mode="w") as file:
            file.close()
            log.info("{} was created".format(fileName))

    if not os.path.isfile(fileName):
        log.exception(FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), fileName))

    if os.path.isfile(zipName):
        log.info("{} is already exists".format(zipName))
    else:
        with ZipFile(zipName, mode="w") as zf:
            zf.write(fileName)
            zf.close()
            log.info("{} was created".format(zipName))

    if not os.path.isfile(zipName):
        log.exception(FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), zipName))

```

the python application you can find in the repository [here](/zip_job.py)

<br>

<h3 id="jenkins" style="text-decoration:underline">Jenkins Pipelines:</h3>

This Section is about our Jenkins Pipelines, we are have 2 pipeline from this project.

the amin action of those pipeline will first checkout from git repository then will build our [Dockerfile](#docker), after that run the docker image wiht our [Python Application](#python) to create the files and zip files and finally will upload all zip files to our Artifactory.  <br>

we can find the pipelines:

- [Jenkins Scripted Pipeline](/Jenkinsfile_scripted)
- [Jenkins Declarative Pipeline](/Jenkinsfile_declarative)

[back to top](#menu)
