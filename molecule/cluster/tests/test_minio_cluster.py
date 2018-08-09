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


@pytest.mark.parametrize('minio_datadir', [
    '/test1',
    '/test2',
    '/test3',
    '/test4'
])
def test_directories(host, AnsibleDefaults, minio_datadir):

    d = host.file(minio_datadir)
    assert d.is_directory
    assert d.exists
    assert d.user == AnsibleDefaults['minio_user']
    assert d.group == AnsibleDefaults['minio_group']
    assert oct(d.mode) == '0750'
