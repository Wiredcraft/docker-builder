Docker Builder
==============

Build script to create images which are based on each other in a certain hierarchy, tag them and push them to a remote repository.

The scenario is a stack of docker images where the 2nd one is made FROM: the 1st, the 3rd one is made FROM: the 2nd, ... and so on.

docker-builder helps to rebuild such a stack from the point where anything might have to changed and therefore a rebuild of an image (and naturally all images on top of that image in such a stack) is required.
Let's say there is a stack of 10 images based on each other and a vulnaribiity turns up in the 7th of those 10. The docker-builder helps to auotmaitcally rebuild the images 7-10


Test
====
.. code-block:: bash

    sudo pip install -r requirements.txt
    make test

Install
=======

.. code-block:: bash

    pip install docker-builder


Usage
=====

.. code-block:: bash

    docker-builder [-f <builder.yaml>] [--no-push] [--no-cache] [<container>...]


Config file
===========

It expects a config file in ``yaml`` format in the current folder named ``builder.yaml``.

Format
------

.. code-block:: yaml

    registries:
      - registry: https://index.docker.io/v1/
        username: user
        password: pass
        email: email

      - registry: local
        username: 127.0.0.1:5000

    containers:
      - container1
      - container2
      - container3


Registries
----------

Each of the containers will be tagged and pushed to each of the registries with the ``latest`` tag.

If registry is ``local``, no login will be attempted and the container will be pushed to the local registry as defined in the username.
If registry is an ``http/https`` based registry, the ``username``, ``password`` and ``email`` will be used to login.

Containers
----------

The ``containers`` attribute defines a list of containers and the order in which they will be built. It effectively defines the dependencies among containers and ensure the "source" ones are built first.

Each of the containers defined in the list must be defined in a matching name folder.

TODO
====

Lots of things; this first version is very crude and only a wrapper arround the regular ``docker`` CLI command.

- use docker-py (why not...)
- better management of hierarchy in a project (e.g. specifying a parent container would automatically re-build the childrens)
- suggestions?
