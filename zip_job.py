#!/usr/bin/env python3
import os
import errno
from zipfile import ZipFile
import logging

logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.StreamHandler()])
log = logging.getLogger()

if "VERSION" not in os.environ:
    exit(200)

version = os.getenv("VERSION")
arr = ["a", "b", "c", "d"]

for name in arr:
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
