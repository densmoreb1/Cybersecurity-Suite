
# Cybersecurity Suite

- Link for requirements and outlines
https://content.byui.edu/file/c05247fa-94c6-4359-b670-a575f25773a7/1/content/499-course-information.html#proposal

### Info Gathering script ideas
- network scanner
- find ip address of a website
- test strength of password

### Exploitation script ideas
- send phising emails
    - could use machine learning to put together an email that looks similar to a compnay the user inputs
- create a program that will display cat pictures every 5 seconds
- keylogger

# Notes

## Scanning with NMAP

### TCP Scans (-sT)
- you send a __SYN__ flag
- the server sends a response with __SYN/ACK__ flags
- you send a __ACK__ flag back to the server
$\space$
- if the port is __closed__ you will recieve a __RST__ flag 
- if the port is __blocked__ by a firewall then there will be no response

### SYN Scans (-sS)
- you send a __SYN__ flag
- the server sends a response with __SYN/ACK__ flags
- instead of sending an __ACK__ flag it sends a __RST__ flag which prevents the server from repeatedly trying to make the request
$\space$
Advantages
- bypass intrusion detection systesm
- most likley not logged by applications
Disadvantages
- sudo permissions
- unstable enviroments could be shutdown by SYN scans

### UDP Scans (-sU)
- 