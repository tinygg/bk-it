# oracle/mysql �������ڱ��ݽű�
��Ŀ�ж��/�����ݿ⣬�ֶ�����������΢�鷳�����ڱ���Ҳ��Ҫ�˽ű���

##  ʹ�÷���

- �޸������ļ� db_bk.json��bk.bat�ļ�
- �ֶ�����:ִ��db_bk.py����;Windows�Զ�����:ѡ����ִ��bk.bat;

##  json����˵��

json.bkdir Ϊ���ݺ�Ĵ洢Ŀ¼
json.oracle Ϊoracleʵ���ı�����Ϣ��֧�ֶ�ʵ���� nameΪ�����ļ���ǰ׺;temp_pathΪ���ݵ���ʱĿ¼ 
json.mysql Ϊmysql�ı�����Ϣ

````
{
    "bkdir": "C:/Users/Administrator/bk",
    "oracle": [
        { "sid": "AAA", "user": "xx", "pwd": "xxx", "name": "AAA.dmp","temp_path": "D:/app/Administrator/admin/AAA/dpdump" },
        { "sid": "BBB", "user": "xx", "pwd": "xxx", "name": "BBB.dmp","temp_path": "D:/app/Administrator/admin/BBB/dpdump" }
    ],
    "mysql": [
        { "db_name": "CCC", "port": "3306", "user": "xx", "pwd": "xxx", "name": "CCC.sql" },
        { "db_name": "DDD", "host":"10.0.0.2", "port": "3306", "user": "xx", "pwd": "xxx", "name": "DDD.sql" }
    ]
}
````

## bk.bat˵��

���ļ���Ϊwindows�ƻ������Զ�ִ�з����,ָ���˳������ڵ�λ�ã���Ҫ��Ӧ�޸ġ�
PS:��֪��Ϊɶwindows�ƻ�����ֱ������db_bk.py�����Զ�����,ͨ����ô��bat�ļ��Ϳ����ˡ�

## ����˵��

0.1	�������oracle��mysql��һ�����ݹ���.  
0.2	�޸�:���ű�Ŀ¼ͳһ��C��database��;  
	�޸�:������һ��log�쳣;  
	�¹���:mysqlԶ�̱��ݲ���host(��ѡ)  

## NEXT

oracle���ݿ��Զ�̱���(dblink),Ŀǰ��û�д�����,���ǲ������Ϻ���������.����Ҫ�߿������.
