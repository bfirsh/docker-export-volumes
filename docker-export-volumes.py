#!/usr/bin/env python
import docker
import os
import socket
import sys
import tarfile

def print_usage(err):
    print >>sys.stderr, """%s

$ docker run -v /var/run/docker.sock:/var/run/docker.sock --volumes-from=container_to_export bfirsh/docker-export-volumes > volume.tar""" % err

if not os.path.exists("/var/run/docker.sock"):
    print_usage("You need to run this image with /var/run/docker.sock injected as a volume.")
    sys.exit(1)

client = docker.Client("unix://var/run/docker.sock")
container = client.inspect_container(socket.gethostname())

volume_paths = [k for k in container['Volumes'].keys() if k != "/var/run/docker.sock"]

if len(volume_paths) == 0:
    print_usage("You need to use the --volumes-from option to docker to specify which container's volumes you want to export.")
    sys.exit(1)

tar = tarfile.open(fileobj=sys.stdout, mode="w|")
for path in volume_paths:
    tar.add(path)
tar.close()

