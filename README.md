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
