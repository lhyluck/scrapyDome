from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
#同时启动多个爬虫  python crawl.py
process = CrawlerProcess(get_project_settings())

# dangdang是爬虫名
# process.crawl('dangdangImg')
process.crawl('dangdangExcel')
# process.crawl('myspd3')

process.start()