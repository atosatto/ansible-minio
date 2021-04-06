<p><img src="https://avatars0.githubusercontent.com/u/695951?s=200&v=4" alt="minio logo" title="minio" align="right" height="60" /></p>

# Ansible Role: Minio

[![Build Status](https://travis-ci.org/atosatto/ansible-minio.svg?branch=master)](https://travis-ci.org/wireapp/ansible-minio)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![GitHub tag](https://img.shields.io/github/tag/atosatto/ansible-minio.svg)](https://github.com/wireapp/ansible-minio/tags)

Install and configure the [Minio](https://minio.io/) S3 compatible object storage server
on RHEL/CentOS and Debian/Ubuntu.

## Requirements

Ansible: `ansible >= 2.8, < 2.9`

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
minio_server_bin: /usr/local/bin/minio
minio_client_bin: /usr/local/bin/mc
```

Installation path of the Minio server and client binaries.

```yaml
minio_server_release: ""
minio_client_release: ""
```

Release to install for both server and client; lastest if the default.
Can be 'RELEASE.2019-06-27T21-13-50Z' for instance.

```yaml
minio_user: minio
minio_group: minio
```

Name and group of the user running the minio server.
**NB**: This role automatically creates the minio user and/or group if these does not exist in the system.

```yaml
minio_server_envfile: /etc/default/minio
```

Path to the file containing the minio server configuration ENV variables.

```yaml
minio_server_addr: ":9091"
```

The Minio server listen address.

```yaml
minio_server_datadirs:
  - /var/lib/minio
```

Directories of the folder containing the minio server data

```yaml
minio_server_make_datadirs: true
```

Create directories from `minio_server_datadirs`

```yaml
minio_server_cluster_nodes: [ ]
```

Set a list of nodes to create a [distributed cluster](https://docs.minio.io/docs/distributed-minio-quickstart-guide).

In this mode, ansible will create your server datadirs, but use this list for the server startup. Note you will need a number of disks to satisfy Minio's distributed storage requirements.

Example:

```yaml
minio_server_datadirs:
  - '/minio-data'
  - ...
minio_server_cluster_nodes:
  - 'https://server1/minio-data'
  - 'https://server2/minio-data'
  - 'https://server3/minio-data'
  - ...
```

```yaml
minio_server_env_extra: ""
```

Additional environment variables to be set in Minio server environment

```yaml
minio_server_opts: ""
```

Additional CLI options that must be appended to the minio server start command.

```yaml
minio_access_key: ""
minio_secret_key: ""
```

Minio access and secret keys. Change the value in order to rotate credentials. 

```yaml
minio_install_server: true
minio_install_client: true
```

Switches to disable minio server and/or minio client installation.

## Dependencies

None.

## Example Playbook

```yaml
- name: "Install Minio"
  hosts: all
  become: yes
  roles:
    - { role: atosatto.minio }
  vars:
    minio_server_datadirs: [ "/minio-test" ]
```

## Changelog

See [changelog](CHANGELOG.md).

## License

MIT
