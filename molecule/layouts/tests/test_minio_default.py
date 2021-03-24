import os
import yaml
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
dir_path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def AnsibleDefaults():
    with open(os.path.join(dir_path, './../../../defaults/main.yml'), 'r') as stream:
        return yaml.load(stream)

@pytest.fixture()
def AnsiblePlaybook():
    with open(os.path.join(dir_path, './../playbook.yml'), 'r') as stream:
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
    assert oct(f.mode) == '0o755'


def test_minio_server_data_directory(host, AnsibleDefaults, AnsiblePlaybook):

    playbpook = AnsiblePlaybook[0]
    for role in playbpook['roles']:
        layoutName = role['vars']['minio_layout']
        datadir = "/var/lib/minio-{}".format(layoutName)
        d = host.file(datadir)
        assert d.is_directory
        assert d.exists
        assert d.user == AnsibleDefaults['minio_user']
        assert d.group == AnsibleDefaults['minio_group']
        assert oct(d.mode) == '0o750'


def test_minio_server_webservers(host, AnsibleDefaults):

    for layoutName in AnsibleDefaults['minio_layouts'].keys():
        server_addr = AnsibleDefaults['minio_layouts'][layoutName]['server_addr']
        addr = "tcp://127.0.0.1{}".format(server_addr)
        host.socket(addr).is_listening
