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


from fireControlPkg.fireControl import *
#config parser is used to read configuration files
from configparser import ConfigParser

from fireControlPkg.fireControl import configure

config = ConfigParser()
config.read('config.ini')

if __name__ == '__main__':
    print('Opening the connection ...............')

    ip = config['connection']['ip']
    ip = config["connection"]['ip']
    device = config['connection']['device']
    user = config['credentials']['user']
    password = config['credentials']['pass']
    connection = establishConnection(ip, device, user, password)

    if args.disable and connection:

        configure(connection)               # put the router in a configuration mode
        print('........disable_Internet..............')
        internetOffHttp(connection)         # dissable rule for tcp
        internetOffHttps(connection)        # disable Https traffic on port 443
        commit(connection)                  # commit the change
        exit(connection)                    # Exit the edit mode
        disconnect(connection)              # Disconnect from the termidisconnect(connection)             i
        # save(connection)                  #Save the change as a permanent change


    elif args.enable and connection:

        configure(connection)               # Put the router in a configuration mode
        print('.........enable_Internet..............')
        internetOnHttp(connection)          # enable the rule for TCP traffic on port 443
        internetOnHttps(connection)         #enable Https traffic
        commit(connection)                  # commit the change and enable the change
        exit(connection)                    # Exit the edit mode
        disconnect(connection)              #Disconnect from the terminal
        #  #save(connection)                #Option to mahe the change permanent

    elif args.uptime and connection:
        print('............Router uptime.............')
        print(upTime(connection))  # show the up time of the router
        disconnect(connection)


    elif args.quit and connection:
        print('...........quitting....................')
        disconnect(connection)  # Disconnect from the terminal


    elif args.show and connection:
        configure(connection)
        show(connection)
        exit(connection)
        disconnect(connection)

    elif args.exit and connection:
        exit(connection)
        a = connection.send_command('whoami')
        if 'edit' not in a:
            print('ok')
        disconnect(connection)

    elif args.host and connection:
        print(connection.send_command('hostname'))
        disconnect(connection)

    elif args.configure and connection:
        configure(connection)
        a=connection.send_command('whoami')
        if 'edit' in a:
            print('ok')
        disconnect(connection)

    else:
        print('...No Commands, so close session......')
        exit(connection)
        disconnect(connection)


