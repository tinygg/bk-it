#!/usr/bin/python
#coding=utf-8
import os
import subprocess
import datetime

config = file('dump.txt','r')
d = config.readline().strip()
to_dir = config.readline().strip()
projects = config.readlines()

os.chdir(d)

'''执行时间太长的话，目录会变化'''
now = datetime.datetime.now()
now_str = '%d.%d.%d.%d.%d' %(now.year,now.month,now.day,now.hour,now.minute)
		
'''foreach dump out'''
for item in projects:
	item = item.strip()
	if item.count > 0:
		d_dir = '%s\%s' % (to_dir, now_str);
		if not os.path.exists(d_dir):
			os.mkdir(d_dir)
			
		if '@' in item:
			proj = item.split('@')[0]
			from_version = item.split('@')[1]
			p = subprocess.Popen("svnadmin dump %s --revision %s --incremental > %s\%s\%s.src.%s.dmp" % (proj, from_version, to_dir, now_str, proj, now_str), stdout=subprocess.PIPE, shell=True)
		else:	
			p = subprocess.Popen("svnadmin dump %s > %s\%s\%s.src.%s.dmp" % (item,to_dir,now_str,item,now_str), stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		print('%s is dump over' % item)
	else:
		print('path error:%s' % item)	
	
print('every thing dump over')


