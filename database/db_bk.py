#coding=utf-8

import os
import subprocess
import datetime
import json
import shutil
import logging
import logging.config  
  
##logging.config.fileConfig("logging.conf")

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

#再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

with open('db_bk.json','r') as f:
    ##load config file
    json_obj = json.load(f)

    now = datetime.datetime.now()
    now_str = '%d.%d.%d.%d.%d' % (now.year,now.month,now.day,now.hour,now.minute)
    
    ##make save path
    date_path = '/%d/%d/%d' % (now.year,now.month,now.day)
    bk_dir = json_obj['bkdir'] + date_path
    try:
        os.makedirs(bk_dir,mode=777)
    except Exception,e:
        logger.debug('may have errors:' + e.message)
    finally:
        if os.path.exists(bk_dir):
            logger.debug('%s create ok!' % bk_dir)

    '''
        function:mysql loop execute
        example:mysqldump --hex-blob -uroot -proot -P3306 qar_db > 2016.1.22.00.qar_db.sql
    '''
    for mysql in json_obj['mysql']:
        ##file name
        file_name = now_str + '.' + mysql['name']

        ##execute expdp
        host = mysql.has_key('host') and mysql['host'] or '127.0.0.1'
        p = subprocess.Popen("mysqldump --hex-blob -u%s -p%s -h %s -P%s %s > %s" % (mysql['user'],mysql['pwd'],host,mysql['port'],mysql['db_name'],file_name), stdout=subprocess.PIPE,shell=True)
        (output,err) = p.communicate()
        ##print 'xxxx'+output
        logger.debug('mysql database:%s \t is dumping over,now moving to bkdir...' % mysql['db_name'])
        
        ##moving file mysql['temp_path'] + '/' +
        tmp_route = file_name
        mysql_bk_path = bk_dir + '/' + file_name
        shutil.move(tmp_route,mysql_bk_path)
        if os.path.exists(mysql_bk_path): 
            logger.debug('moving file ok!')
        else: 
            logger.debug('moving failed!')

    '''
        function:oracle loop execute
        example:expdp sms/xxx@sms dumpfile=2016.1.22.00.sms.expdp.dmp
    '''
    for ora in json_obj['oracle']:
        ##file name
        file_name = now_str + '.' + ora['name']

        ##execute expdp
        p = subprocess.Popen("expdp %s/%s@%s dumpfile=%s" % (ora['user'],ora['pwd'],ora['sid'],file_name), stdout=subprocess.PIPE,shell=True)
        (output,err) = p.communicate()
        ##print 'xxxx'+output
        logger.debug('oracle database:%s \t is dumping over,now moving to bkdir...' % ora['sid'])
        
        ##moving file
        tmp_route = ora['temp_path'] + '/' + file_name
        ora_bk_path = bk_dir + '/' + file_name
        shutil.move(tmp_route,ora_bk_path)
        if os.path.exists(ora_bk_path): 
            logger.debug('moving file ok!')
        else: 
            logger.debug('moving failed!')

    logger.debug('every thing backup over!')