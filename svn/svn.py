import os
import subprocess
import datetime

config = file('dump.txt','r')
d = config.readline().strip()
to_dir = config.readline().strip()
projects = config.readlines()

os.chdir(d)


'''foreach dump out'''
for item in projects:
	item = item.strip()
	if item.count > 0:
		now = datetime.datetime.now()
		now_str = '%d.%d.%d.%d.%d' %(now.year,now.month,now.day,now.hour,now.minute)
		os.mkdir(('%s\%s' % (to_dir, now_str)))
		p = subprocess.Popen("svnadmin dump %s > %s\%s\%s.src.%s.dmp" % (item,to_dir,now_str,item,now_str), stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		print('%s is dump over' % item)
	else:
		print('path error:%s' % item)
	
print('every thing dump over')