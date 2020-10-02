# ssh_script
<h1>Fire Control</h1>

Allows one to enable and disable pre configured firewall rules on an edge router with a simple command line tool.
The tool can be installed on any computer on the same network as the router. 

The program has been written on a linux mint machine and has only been tested on linux.
It is possible running the scrip from a button push on a raspberry PI as a possibility. 

Obviously this is quite a custom piece of software for my application, but can be used to craft, or modify as required. 
The rules are set up in the edge router and tested then they can be disabled.

It also nicely demonstrates how you can use the netmiko to control the edge router.
The application is intended as a command line tool so has a raft of options, although the 'enable' and 'disable' coare the 
The ssh_script called firecontrol can be called on very easily to switch the firwall rule on or off.mmand line options are the most useful.

The script can be run from a cron tool to make configuring of more complicated time of use and makes it easier to make a one time change.
