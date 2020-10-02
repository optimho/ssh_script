#
#       !!!!netmiko!!!!!
#
# This script logs onto the edge router and enables or disables firewall entries.
# This is to switch off kids access to the internet or social media at certain times
# This script can be run from Crontab to control  what times the kids are free to access the internet.
# This was made becaus it was hard to have complicated time slots programed into the router firewall
# I use an edgrouter, and the rules have been created and tested in the edgrouter GUI, then disabled.
# It is then possible to enable and disable rules at will by runing the script or setting cronTab up to do the work.

"""Internet connection control

This is to stop liam playing too many games.
From a computer on the net work log onto:sudo ssh Optimho@192.168.1.1
The password is Blackmamba

There are currently 4 rules setup in the edge router.
Use crontab or a script on the lab computer to enable or disable the rules.

configure  //*this is to put the router in a command mode

set firewall name Internet rule 1 disable     //* to dissable the the rule
delete firewall name Internet rule 1 disable  //* to enable the rule.

commit        //* This enables the changes
save          //* This makes the changes permanent, possibly not requited but the kids could get clever and reset the switch to get access again, if that is the case then rather save each change.

The rules have been set up in the edgerouter.
The rules are working on out bound traffic through the eth0.10 port,
The eth0.10 is a virtual port that is used to connect to the vodafone network.

Thus to get onto the internet you have to pass through this Vlan

The rule  is one of 4 in this case, the first one DROPS all tcp data from mac address e0:d5:5e:aa:0a:d5
The next rule drops all UDP data from e0:d5:5e:aa:0a:d5
The following rules are the same but for Liams mobile phone with mac address b0:6f:e0:40:06:8e

The IP addresses in the edge-router are static for the known mac addresses.
There is possibly a work around if one changes the mac address of the computer,  saying that we could have a white list of mac addresses if they figure out how to do that.

Some more rules can be switched on with deep packet  inspection for social media and maybe you tube so that the internet works but blocks media, this can be switched on and off the same way I  guess.

The next part is to write a script that can run on a local machine that can remotely  enable or disable a rule

netmiko is used as the terminal  see its API here https://ktbyers.github.io/netmiko/docs/netmiko/index.html#header-submodules


edit the config_bak,ini file and rename it to config.ini
"""


import netmiko

# configure command line arguements
import argparse
parser=argparse.ArgumentParser(description='Switch on and off preconfigured edge router firewall rules from command line')
parser.add_argument('-t', '--target', type=str, metavar='', required=False, help='The user being targeted')
group = parser.add_mutually_exclusive_group()
group.add_argument('-e', '--internet_enable', action='store_true',  help='Enable Liams Internet')
group.add_argument('-d', '--internet_disable', action='store_true',  help='Disable  Liams internet')
group.add_argument('-c', '--configure', action='store_true', help='Put the router in configuration mode')
group.add_argument('-u', '--uptime', action='store_true',  help='Is the router up?')
group.add_argument('-s', '--show', action='store_true', help='Show the firewall rules')
group.add_argument('-x', '--exit', action='store_true', help='Leave the configuration console?')
group.add_argument('-q', '--quit', action='store_true', help='Leave and shut connection')
group.add_argument('-n', '--host', action='store_true', help='Router host name')
group.add_argument('-md', '--mobile_disable', action='store_true', help='disable mobile internet connection')
group.add_argument('-me', '--mobile_enable', action='store_true', help='enable mobile internet connection')

args = parser.parse_args()

#config parser is used to read configuration files
from configparser import ConfigParser
config= ConfigParser()
config.read('config.ini')

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
    """turns rule number 1 off - preconfigured in the edge router to dissable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("delete firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)
def internetOffHttps(connection):
    """turns rule number 2 off - preconfigured in the edge router to dissable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("delete firewall name Internet rule 2 disable")
    except Exception as e:
        print("That command was not successful ", e)

def internetOnHttp(connection):
    """turns rule number 1 on - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("set firewall name Internet rule 1 disable")
    except Exception as e:
        print("That command was not successful ", e)

def internetOnHttps(connection):
    """turns rule number 2 on - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this computer"""
    try:
        connection.send_command("set firewall name Internet rule 2 disable")
    except Exception as e:
        print("That command was not successful ", e)


def moblieInternetOffHttp(connection):
    """turns rule number 3 off - preconfigured in the edge router to disable internet traffic going to the internet
    from the mac address of this device, a mobile phone in this case"""
    try:
        connection.send_command("delete firewall name Internet rule 3 disable")
    except Exception as e:
        print("That command was not successful ", e)
def mobileInternetOffHttps(connection):
    """turns rule number 4 off - preconfigured in the edge router to disable internet traffic going to the internet
    from the mac address of this device, a mobile phone in this case"""
    try:
        connection.send_command("delete firewall name Internet rule 4 disable")
    except Exception as e:
        print("That command was not successful ", e)

def mobileInternetOnHttp(connection):
    """turns rule number 3 on - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this of device, a mobile phone in this case"""
    try:
        connection.send_command("set firewall name Internet rule 3 disable")
    except Exception as e:
        print("That command was not successful ", e)

def mobileInternetOnHttps(connection):
    """turns rule number 4 on - preconfigured in the edge router to enable internet traffic going to the internet
    from the mac address of this device, a mobile phone in this case"""
    try:
        connection.send_command("set firewall name Internet rule 4 disable")
    except Exception as e:
        print("That command was not successful ", e)

if __name__ == '__main__':
    print('Opening the connection ...............')

    ip = config['connection']['ip']
    device = config['connection']['device']
    user = config['credentials']['user']
    password = config['credentials']['pass']

    connection: object = establishConnection(ip, device, user, password)


    if args.internet_disable and connection:  #disable internet connection
        configure(connection)                 # put the router in a configuration mode
        print('........disable_Internet..............')
        internetOffHttp(connection)           # dissable rule for tcp
        internetOffHttps(connection)          # disable Https traffic on port 443
        commit(connection)                    # commit the change
        exit(connection)                      # Exit the edit mode
        disconnect(connection)                # Disconnect from the termidisconnect(connection)             i
        # save(connection)                    # Save the change as a permanent change


    elif args.internet_enable and connection: # Enable internet connection
        configure(connection)                 # Put the router in a configuration mode
        print('.........enable_Internet..............')
        internetOnHttp(connection)            # enable the rule for TCP traffic on port 443
        internetOnHttps(connection)           #enable Https traffic
        commit(connection)                    # commit the change and enable the change
        exit(connection)                      # Exit the edit mode
        disconnect(connection)                # Disconnect from the terminal

    elif args.mobile_disable and connection:  # Disable Mobile internet via wifi this will not stop mobile data connection
        configure(connection)                 # put the router in a configuration mode
        print('........disable_Mobile................')
        internetOffHttp(connection)           # dissable rule for tcp
        internetOffHttps(connection)          # disable Https traffic on port 443
        commit(connection)                    # commit the change
        exit(connection)                      # Exit the edit mode
        disconnect(connection)                # Disconnect from the terminal              i
        # save(connection)                    # Save the change as a permanent change


    elif args.mobile_enable and connection:  # Enable Mobile internet via wifi
        configure(connection)                # Put the router in a configuration mode
        print('.........enable_Mobile................')
        internetOnHttp(connection)           # enable the rule for TCP traffic on port 443
        internetOnHttps(connection)          #enable Https traffic
        commit(connection)                   # commit the change and enable the change
        exit(connection)                     # Exit the edit mode
        disconnect(connection)               #Disconnect from the terminal
        #  #save(connection)                 #Option to mahe the change permanent    #  #save(connection)                #Option to mahe the change permanent

    elif args.uptime and connection:
        print('............Router uptime.............')
        print(upTime(connection))  # show the up time of the router
        disconnect(connection)

    elif args.quit and connection:
        print('...........quitting....................')
        disconnect(connection)  # Disconnect from the terminal

    elif args.show and connection: # show the rule set of the firewall
        configure(connection)
        show(connection)
        exit(connection)

    elif args.exit and connection: # Exit the terminal
        exit(connection)
        a = connection.send_command('whoami')
        if 'edit' not in a:
            print('ok')

    elif args.host and connection: #report the host name of the router
        print('................{}....................'.format(connection.send_command('hostname')))
        exit(connection)
        disconnect(connection)

    elif args.configure and connection:
        configure(connection)
        a=connection.send_command('whoami')
        if 'edit' in a:
            print('ok')
    else:                           # No commands recognised exit the program
        print('...No Commands, so close session......')
        exit(connection)
        disconnect(connection)

