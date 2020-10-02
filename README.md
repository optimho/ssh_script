<h1>Fire Control</h1>
<style>
p {indent-text: 0em;}
</style>

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

run the script with python3 <b>fireControl.py -u </b> to see if the router is responsive

To make things work you need to make sure the config.ini file is up to date, rename the config1.ini file to config.ini and make sure your passwords and ip addresses are filled in correctly in the config.ini file
  
  too run this command line program see the following examples
  
  <b>python3 fireControl.py -n</b> 
          <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  or<br>
  <b>python3 fireControl.py host</b>
<h5><u>Comand line switch options</u></h5>  


-e or Enable   &emsp;   Enable Internet <br>
-d or Disable   &emsp;  Disable the internet   
-c or configure &emsp;  Put the router in configuration mode <br>
-u or uptime   &emsp; &emsp;   Is the router up? <br>
-s or show    &emsp;&emsp;  &emsp;   Show the firewall rules<br> 
-x or exit    &emsp; &emsp;&emsp;&emsp;   Leave the configuration console?<br> 
-q or quit    &emsp; &emsp;&emsp;   Leave and shut connection<br>
-n or host    &emsp; &emsp;&emsp;   Router host name<br>
