#  备份svn脚本

为了防范风险，托管在SVN的代码也需要备份，这就是此脚本出现的缘由。

##  使用方式

- 编辑dump.txt

- 执行svn.py即可


## dump.txt 说明
第一行填repo所在目录.
后面每一行都是一个repository


##  小技巧
cmd下cd到svn repo根目录
dir /a:d 显示所有文件夹
将文件夹部分粘贴至notepad ++，摁下  alt键+鼠标跨行拖动  即可跨行获取你需要的文件夹名列，正是我们需要的格式.

```
Microsoft Windows [版本 10.0.10586]

tiny@DESKTOP-TINY C:\Users\tiny
> D:

tiny@DESKTOP-TINY D:\
> cd Repositories

tiny@DESKTOP-TINY D:\Repositories
> dir /a:d
 驱动器 D 中的卷是 四道风
 卷的序列号是 0006-9F52

 D:\Repositories 的目录

2016/04/11  13:55    <DIR>          .
2016/04/11  13:55    <DIR>          ..
2016/02/15  16:47    <DIR>          xx
2016/02/18  12:58    <DIR>          xxx.GUI
2016/04/08  14:55    <DIR>          xxx.Service
2016/01/28  20:42    <DIR>          xxx.Web
2016/03/14  11:40    <DIR>          design
2016/01/28  17:36    <DIR>          xxx.DC
2016/02/24  16:41    <DIR>          xxx.HX
2016/01/28  17:20    <DIR>          xxxxx
2016/01/28  17:20    <DIR>          xxxx
2016/01/28  17:21    <DIR>          xxxxxx
2016/01/28  17:38    <DIR>          xxxxxxxx.Project
2016/01/28  17:39    <DIR>          xxxxxxxx
2016/01/28  17:41    <DIR>          xxxxxxxxxxxx
               0 个文件              0 字节
              15 个目录 156,827,242,496 可用字节

tiny@DESKTOP-TINY D:\Repositories
```

最后dump.txt应该是这样的样子

````
D:\Repositories
xx
xxx.GUI
xxx.Service````
xxx.Web
design
xxx.DC
xxx.HX
xxxxx
xxxx
xxxxxx
xxxxxxxx.Project
xxxxxxxx
xxxxxxxxxxxx
````

##  

更新:2017/07/21 
1.备份至指定目录的功能,dump.txt第二行指定。  
2.文件SVN.xml是Windows定期执行的计划任务  



