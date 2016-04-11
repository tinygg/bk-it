import os
import subprocess
import datetime

config = file('dump.txt','r')
d = config.readline().strip()
projects = config.readlines()

os.chdir(d)


'''foreach dump out'''
for item in projects:
	item = item.strip()
	if item.count > 0:
		now = datetime.datetime.now()
		now_str = '%d.%d.%d.%d.%d' %(now.year,now.month,now.day,now.hour,now.minute)
		p = subprocess.Popen("svnadmin dump %s > %s.src.%s.dmp" % (item,item,now_str), stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		print('%s is dump over' % item)
	else:
		print('path error:%s' % item)
	
print('every thing dump over')