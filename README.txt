# ssh_script
Allows one to enable and disable pre configured firewall rules on an edge router with a simple command line tool.
Fire Control
<style> p {indent-text: 0em;} </style>
Allows one to enable and disable pre configured firewall rules on an edge router with a simple command line tool. The tool can be installed on any computer on the same network as the router.

The program has been written on a linux mint machine and has only been tested on linux. It is possible running the scrip from a button push on a raspberry PI as a possibility.

Obviously this is quite a custom piece of software for my application, but can be used to craft, or modify as required. The rules are set up in the edge router and tested then they can be disabled.

It also nicely demonstrates how you can use the netmiko to control the edge router. The application is intended as a command line tool so has a raft of options, although the 'enable' and 'disable' coare the The script called fireControl can be called on very easily to switch the firewall rules on or off.mmand line options are the most useful.

The script can be run from a cron tool to make configuring of more complicated time of use and makes it easier to make a one time change.

run the script with python3 fireControl.py -u to see if the router is responsive

To make things work you need to make sure the config.ini file is up to date, rename the config_bak.ini file to config.ini and make sure your passwords and ip addresses are filled in correctly in the config.ini file

too run this command line program see the following examples

python3 fireControl.py -n
               or
python3 fireControl.py host

Comand line switch options
-e or enable      Enable Internet
-d or disable      Disable the internet
-c or configure    Put the router in configuration mode
-u or uptime      Is the router up?
-s or show      Show the firewall rules
-x or exit       Leave the configuration console?
-q or quit        Leave and shut connection
-n or host       Router host name

To taylor make this application, just look at expanding the methods in the fireControl.py and the command line options in main py
