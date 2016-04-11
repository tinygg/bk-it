# oracle/mysql 批量定期备份脚本
项目有多个/种数据库，手动备份起来稍微麻烦，定期备份也需要此脚本。

##  使用方法

- 修改配置文件 db_bk.json、bk.bat文件
- 手动备份:执行db_bk.py即可;Windows自动备份:选择定期执行bk.bat;

##  json配置说明

json.bkdir 为备份后的存储目录
json.oracle 为oracle实例的备份信息（支持多实例） name为备份文件的前缀;temp_path为备份的临时目录 
json.mysql 为mysql的备份信息

````
{
    "bkdir": "C:/Users/Administrator/bk",
    "oracle": [
        { "sid": "AAA", "user": "xx", "pwd": "xxx", "name": "AAA.dmp","temp_path": "D:/app/Administrator/admin/AAA/dpdump" },
        { "sid": "BBB", "user": "xx", "pwd": "xxx", "name": "BBB.dmp","temp_path": "D:/app/Administrator/admin/BBB/dpdump" }
    ],
    "mysql": [
        { "db_name": "CCC", "port": "3306", "user": "xx", "pwd": "xxx", "name": "CCC.sql" },
        { "db_name": "DDD", "port": "3306", "user": "xx", "pwd": "xxx", "name": "DDD.sql" }
    ]
}
````

## bk.bat说明

此文件是为windows计划任务自动执行服务的,指定了程序所在的位置，需要对应修改。
PS:不知道为啥windows计划任务直接配置db_bk.py不能自动备份,通过这么个bat文件就可以了。