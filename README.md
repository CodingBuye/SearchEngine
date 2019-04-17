# SearchEngine
scrapy分布式爬虫打造搜索引擎

### 开发环境搭建
- IDE：pycharm
    - 官方网站：
      https://www.jetbrains.com/pycharm/download/#section=mac
    - 激活码：
      https://blog.csdn.net/wuyujin1997/article/details/86141775
- 数据库：mysql, redis, elasticsearch
- 开发环境：virtualenv

### 基础知识回顾
- 技术选型：scrapy vs requests+beautifulsoup
	- requests和beautifulsoup都是库，scrapy是框架
	- scrapy框架中可以加入requests和beautifulsoup
	- scrapy基于twisted，性能是最大的优势
	- scrapy方便扩展，提供了很多内置的功能
	- scrapy内置的css和xpath selector非常方便，beautifulsoup最大的缺陷就是慢
- 网页分类
	- 静态网页
	- 动态网页
	- webservice(restapi)
- 爬虫作用
	- 搜索引擎---百度、google、垂直领域搜索引擎(只搜索某一类)
	- 推荐引擎---今日头条
	- 机器学习的数据样本
	- 数据分析(如金融数据分析)、舆情分析等
- 正则表达式
- 深度优先和广度优先
- 爬虫去重策略
    - 将访问过的url保存到数据库中(最简单，但是用的比较少)
    - 将访问过的url保存到set中，只需要O(1)的代价就可以查询url 
      100000000*2byte*50个字符/1024/1024/1024 = 9G(内存消耗大)
    - url经过md5等方法哈希后保存到set中(scrapy采用的方法)
    - 用bitmap方法，将访问过的url通过hash函数映射到某一位
    - bloomfilter方法对bitmap进行改进，多重hash函数降低冲突
- 字符串编码
    - 计算机只能处理数字，文本转换为数字才能处理。计算机中8个bit作为一个字节，
      所以一个字节能表示最大的数字就是255
    - 计算机是美国人发明的，所以一个字节可以表示所有字符了，所以ASCII(一个字节)编码
      就成为美国人的标准编码，但是ASCII处理中文明显是不够的，中文不止255个汉字，
      所以中国制定了GB2312编码，用两个字节表示一个汉字。GB2312还把ASCII包含进去了，
      同理，日文、韩文等等上百个国家为了解决这个问题就都发展了一套字节的编码，
      标准就越来越多，如果出现多种语言混合显示就一定会出现乱码。
      于是unicode出现了，将所有语言统一到一套编码里。
    - 例子：
        - 字母A用ASCII编码十进制是65，二进制是0100 0001
        - 汉字“中”已经超出了ASCII编码的范围，用unicode编码是20013,
          二进制是01001110 00101101
        - A用unicode编码只需要前面补0二进制是00000000 01000001
    - 乱码问题解决了，但是如果内容全是英文，unicode编码比ASCII需要多一倍的存储空间，
      同时如果传输需要多一倍的传输。所以出现了可变长的编码“utf-8”,把英文变成一个字节，
      汉字3个字节。特别生僻的变成4-6字节，如果传输大量的英文，utf8作用就很明显。



### ElasticSearch介绍
我们搭建一个网站或者程序，希望添加搜索功能，发现搜索工作很难：
- 我们希望搜索解决方案要高效
- 我们希望零配置和完全免费的搜索方案
- 我们希望能够简单的通过json和http与搜索引擎交互
- 我们希望我们的搜索服务器稳定
- 我们希望能够简单的将一台服务器扩展到上百台
https://baike.baidu.com/item/elasticsearch/3411206?fr=aladdin
ELK

关系数据库搜索缺点：
1. 无法打分
2. 无分布式
3. 无法解析搜索请求
4. 效率低
5. 分词

安装：(需要java8及以上版本)
1. elasticsearch-rtf(https://github.com/medcl/elasticsearch-rtf)
2. head插件和kibana的安装

elasticsearch概念
- 集群：一个或多个节点组织在一起
- 节点：一个节点是集群中的一个服务器，由一个名字来标识，
  默认是一个随机的漫画角色的名字
- 分片：将索引划分为多份的能力，允许水平分割和扩展容量，
  多个分片相应请求，提供性能和吞吐量
- 副本：创建分片的一份或多份的能力，在一个节点失败其余节点可以顶上

