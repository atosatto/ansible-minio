import os
import yaml
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_minio_server_env_file(host, AnsibleDefaults):

    f = host.file('/opt/minio')
    assert f.is_file
    assert f.exists
    assert f.user == 'root'
    assert f.group == AnsibleDefaults['minio_group']
    assert oct(f.mode) == '0640'


@pytest.mark.parametrize('minio_datadir', [
    '/srv/data1',
    '/srv/data2',
    '/srv/data3',
    '/srv/data4'
])
def test_minio_server_data_directories(host, AnsibleDefaults, minio_datadir):

    d = host.file(minio_datadir)
    assert d.is_directory
    assert d.exists
    assert d.user == AnsibleDefaults['minio_user']
    assert d.group == AnsibleDefaults['minio_group']
    assert oct(d.mode) == '0750'


def test_minio_server_webserver(host):

    host.socket("tcp://127.0.0.1:80").is_listening
