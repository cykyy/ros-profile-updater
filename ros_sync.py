import pyros_api

from helper import read_dict_from_file


def ros_api():
    conf = read_dict_from_file("config.conf")
    m_ip = conf.get('m_ip')
    username = conf.get('username')
    password = conf.get('password')

    x = pyros_api.RosCall(username=username, password=password, ros_ip=m_ip, plaintext_login=True)
    if x.connection.connected:
        print('Connected', x.connection.connected)
        return x
    else:
        x.login()
        print('New Mikrotik Connection:', x.connection.connected)
        return x
