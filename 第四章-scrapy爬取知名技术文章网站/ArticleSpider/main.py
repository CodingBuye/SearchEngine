from scrapy.cmdline import execute
import sys
import os

# print(os.path.abspath(__file__))  # 获取当前文件的路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 命令： scrapy crawl jobbole
execute(['scrapy', 'crawl', 'jobbole'])
