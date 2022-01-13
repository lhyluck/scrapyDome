# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class FirstspiderItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field() #图片下载地址列表
    images_path = scrapy.Field() #图片本地存储路径（相对地址）
    images_name = scrapy.Field() #文件名称
    # pass
    title = scrapy.Field()
    author = scrapy.Field()
    detail = scrapy.Field()


