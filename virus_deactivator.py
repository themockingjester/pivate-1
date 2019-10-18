
import psutil,os,time
list1=list()
for proc in psutil.process_iter():	
	# Get process name from process object.
	processName = proc.name()
	list1.append(processName)
for i in list1:
	

        print(i)
        time.sleep(1)
        if "explorer.exe" not in i and "sihost.exe" not in i and "ApplicationFrameHost.exe" not in i and "hj.exe" not in i and "SearchUI.exe" not in i and "conhost.exe" not in i: #here hj.exe is the current name of our script and rest of others are necessary apps
                try:
                        m="taskkill /f /im "+i
                        os.system(m)
                except:
                        pass
        else:
                continue
input()
