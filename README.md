Ansible Role: Minio
===================

[![Build Status](https://travis-ci.org/atosatto/ansible-minio.svg?branch=master)](https://travis-ci.org/atosatto/ansible-minio)

Install and configure the [Minio](https://minio.io/) S3 compatible object storage server
on RHEL/CentOS and Debian/Ubuntu.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

    minio_server_bin: /usr/local/bin/minio
    minio_client_bin: /usr/local/bin/mc

Installation path of the Minio server and client binaries.

    minio_user: minio
    minio_group: minio

Name and group of the user running the minio server.
**NB**: This role automatically creates the minio user and/or group if these does not exist in the system.

    minio_server_envfile: /etc/default/minio

Path to the file containing the minio server configuration ENV variables.

    minio_server_addr: ":9091"

The Minio server listen address.

    minio_server_datadirs: [ ]

Directories of the folder containing the minio server data
**NB**: This variable must always be set by the role, otherwise the minio service will not start.

    minio_server_opts: ""

Additional CLI options that must be appended to the minio server start command.

    minio_access_key: ""
    minio_secret_key: ""

Minio access and secret keys.

    skip_server: False
    skip_client: False

Switches to disable minio server and/or minio client installation.

Dependencies
------------

None.

Example Playbook
----------------

    $ cat playbook.yml
    - name: "Install Minio"
      hosts: all
      roles:
         - { role: atosatto.minio,
             minio_server_datadirs: [ "/tmp" ] }

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
