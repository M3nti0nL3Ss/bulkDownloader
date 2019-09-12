import requests
import sys
from urllib.parse import unquote


with open('t.txt', 'r') as f:
    lists = f.readlines()

for x in range(len(lists)):
	lis = unquote((lists[x].split("&title=",1)[1])).replace('\n', '').replace(':', '.')
	file_name = "./ttt/"+lis+".mp4" #The file extension
	with open(file_name, "wb") as f:
	        print ("Downloading %s" % file_name)
	        response = requests.get(lists[x], stream=True)
	        total_length = response.headers.get('content-length')

	        if total_length is None: # no content length header
	            f.write(response.content)
	        else:
	            dl = 0
	            total_length = int(total_length)
	            for data in response.iter_content(chunk_size=4096):
	                dl += len(data)
	                f.write(data)
	                done = int(50 * dl / total_length)
	                sys.stdout.write("\r[%s%s] %s " % ('=' * done, ' ' * (50-done),str(done*2)) )    
	                sys.stdout.flush()
	print(" DONE !")
