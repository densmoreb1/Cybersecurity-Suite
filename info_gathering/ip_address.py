import socket   

hostname = input('Enter the URL: ')
IPAddr = socket.gethostbyname(hostname)   

print("IP Address is: " + IPAddr)
