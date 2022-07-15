import os
import requests

desktops={
    'anydesk':7070,
    'ultraviewer':2112,
    'teamviewer':5938,
    }

detected_connections=[]

remotedesktop=input("Enter the remote desktop name: ")
if remotedesktop in desktops:
    print(f"{remotedesktop} has been selected")
    port=desktops[remotedesktop]
    while True:
        find=os.popen(f"netstat -n | findstr {port}").read()
        if not find in detected_connections:
            detected_connections.append(find)
            find=find.replace("TCP","").replace("ESTABLISHED","").replace(" ","")
            ip=find.split(port)[1].split(":")[0]
            print(f"{remotedesktop} is connected from {ip}")
            url=f"http://ip-api.com/json/{ip}"
            r=requests.get(url)
            data=r.json()
            country=data['country']
            city=data['city']
            if country=="India":
                print(f"{ip} is located in {city}, {country}")
                break
