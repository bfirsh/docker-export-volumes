bfirsh/docker-export-volumes
============================

A Docker image to export volumes from containers running on the same host.

Pass it a container using `--volumes-from` and it'll output a tarball of the volumes from that container to stdout:

    $ docker run --name mycontainer -v /data ubuntu touch /data/test
    $ docker run --volumes-from=mycontainer -v /var/run/docker.sock:/var/run/docker.sock bfirsh/docker-export-volumes > volumes.tar
    $ tar -tf volumes.tar
    data/
    data/test

Note: it only works on Docker hosts which listen on a UNIX socket because the image needs to access the host's remote API. In the example above, `/var/run/docker.sock` is injected into the container as a volume.

