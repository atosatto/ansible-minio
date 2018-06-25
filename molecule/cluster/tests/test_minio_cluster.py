import yaml
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("./defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dirs", [
    "/minio-test"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists
    assert d.user == AnsibleDefaults['minio_user']
    assert d.group == AnsibleDefaults['minio_group']
    assert oct(d.mode) == '0750'


def test_env_file(host):
    env_file = host.file("/etc/default/minio")
    assert env_file.contains('MINIO_VOLUMES="https://172.17.0.2:9091/test"')


def test_minio_service(Service):
    s = Service('minio')
    assert s.is_running
    assert s.is_enabled
