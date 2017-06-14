import time
from datetime import datetime as dt
hosts_path="hosts"
hosts_path=r"/etc/hosts"
redirect="127.0.0.1"
website=["www.facebook.com","www.youtube.com","www.gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
    	print "working hours"
    	with open(hosts_path,'r+') as file:
    		content=file.read()
    		for web in website:
    			if web in content:
    				pass
    			else:
    				file.write(redirect+" "+web+"\n")
    	
    else:
    	with open(hosts_path,'r+') as file:
    		content=file.readlines()
    		file.seek(0)
    		for line in content:
    			if not any(web in  line for web in website):
    				file.write(line)
    		file.truncate()

    	print "fun" 
	time.sleep(5)