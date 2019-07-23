import os
import yaml
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults():
    with open('../../defaults/main.yml', 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize('minio_bin_var', [
    'minio_server_bin',
    'minio_client_bin',
])
def test_minio_installed(host, AnsibleDefaults, minio_bin_var):

    f = host.file(AnsibleDefaults[minio_bin_var])
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0755'


def test_minio_server_data_directories(host, AnsibleDefaults):

    for datadir in AnsibleDefaults['minio_server_datadirs']:
        d = host.file(datadir)
        assert d.is_directory
        assert d.exists
        assert d.user == AnsibleDefaults['minio_user']
        assert d.group == AnsibleDefaults['minio_group']
        assert oct(d.mode) == '0750'


def test_minio_server_webserver(host):

    host.socket('tcp://127.0.0.1:9091').is_listening
