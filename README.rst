Docker Builder
==============

Build script to create containers, tag them and push them to a remote repository.

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