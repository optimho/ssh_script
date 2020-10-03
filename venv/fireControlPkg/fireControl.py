
import netmiko

# configure command line arguements
import argparse
parser=argparse.ArgumentParser(description='Switch on and off preconfigured edge router firewall rules from command line')
parser.add_argument('-t', '--target', type=str, metavar='', required=False, help='The user being targeted')
group = parser.add_mutually_exclusive_group()
group.add_argument('-e', '--enable', action='store_true',  help='Enable Liams Internet')
group.add_argument('-d', '--disable', action='store_true',  help='Disable  Liams internet')
group.add_argument('-c', '--configure', action='store_true', help='Put the router in configuration mode')
group.add_argument('-u', '--uptime', action='store_true',  help='Is the router up?')
group.add_argument('-s', '--show', action='store_true', help='Show the firewall rules')
group.add_argument('-x', '--exit', action='store_true', help='Leave the configuration console?')
group.add_argument('-q', '--quit', action='store_true', help='Leave and shut connection')
group.add_argument('-n', '--host', action='store_true', help='Router host name')

args=parser.parse_args()



def establishConnection(ip, device, user, password) -> object:
    """

    :rtype: object
    """
    try:
        return netmiko.ConnectHandler(ip=ip, device_type=device, username=user, password=password)
    except Exception as e:
        print("There has been a connection error", e)
        connection = None


def commit(connection):
    """Commits a change in the router and enforces the rule"""
    try:
        connection.send_command("commit")
    except Exception as e:
        print("That command was not successful ", e)

    print('..............committed...............')


def save(connection):
    """Saves the configuration so that it is a permanent change"""
    try:
        connection.send_command("save")
    except Exception as e:
        print("That command was not successful ", e)


def upTime(connection):
    """Return the amount of time that the edge router has been up"""
    try:
        return (connection.send_command("uptime"))
    except Exception as e:
        print("That command was not successful ", e)


def disconnect(connection):
    """method to disconnect from the router """
    try:
        connection.disconnect()
    except Exception as e:
        print('Could not disconnect')
    else:
        print('.............disconnected.............')

def show(connection):
    """method to show firewall configuration """
    try:
        a=connection.send_command('show firewall')
    except Exception as e:
        print('Could not shoe connection', e)
    else:

        print(a)

def configure(connection) -> object:
    """Method to put the router into a configuration mode so that you can configure the router firewall."""
    try:
        connection.config_mode('configure', 'configure\r\n')
    except Exception as e:
        print("That command was not successful ", e)


def exit(connection):
    """Method to get out of edit mode"""
    try:
        connection.exit_config_mode('exit')
    except Exception as e:
        print("That command was not successful ", e)


def internetOffHttp(connection):
    """turns rule number 1 off - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("delete firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)
def internetOffHttps(connection):
    """turns rule number 1 off - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("delete firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)

def internetOnHttp(connection):
    """turns rule number 1 on - preconfigured in the edge router to block internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("set firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)

def internetOnHttps(connection):
    """turns rule number 1 on - preconfigured in the edge router to block internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("set firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)