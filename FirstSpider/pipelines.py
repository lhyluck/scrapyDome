# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from openpyxl import Workbook
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import scrapy
import re


# class FirstspiderPipeline:
#     def process_item(self, item, spider):
#         return item

# 自定义映像管道 ImagesPipeline是scrapy.pipelines.images图像管道的扩展，用于自定义字段名称并为图像添加自定义行为
class imgsPipeLine(ImagesPipeline):
    # ImagePipeline根据image_urls中指定的url进行爬取，可以通过get_media_requests为每个url生成一个Request
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'], meta={'imgName': item['images_name']})

    # 此方法对每个下载的项目调用一次。它返回源自指定响应的文件的下载路径,此方法还接收原始和response、request、info、item
    def file_path(self, request, response=None, info=None, item=None):
        # 可以这样保留原文件名
        # imgName = request.url.split('/')[-1]
        img_name = request.meta['imgName']
        img_name = re.sub(r'[？\\*|“<>:/]', '', img_name)
        img_type = request.url.split('.')[-1]
        imgName = img_name + '.' + img_type
        return imgName

    # 当对单个项目的所有图像请求都已完成（下载完成或由于某种原因失败）时，处理结果会以二元组的方式返回给item_completed()函数。
    # 这个二元组定义如下：(success, image_info_or_failure)其中，
    # 第一个元素表示图片是否下载成功；
    # 第二个元素是一个字典，包括：url是图片下载的url,path是图片存储的路径，checksum是图片内容MD5 hash
    # results参数是get_media_requests下载完成之后返回的结果，即二元组
    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         # 下载失败忽略该 Item 的后续处理
    #         raise DropItem("Item contains no images")
    #     # 用于与数据容器对象交互的包装类。它提供了一个公共接口来提取和设置数据，而不必考虑对象的类型
    #     adapter = ItemAdapter(item)
    #     img_name = adapter['images_name']
    #     # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
    #     img_name = re.sub(r'[？\\*|“<>:/]', '', img_name)
    #     img_type = image_paths.split('.')[-1]
    #     adapter['images_path'] = image_paths
    #     return item


class ExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['标题', '作者', '简介'])
        self.file_name = "dangdangBook.xlsx"

    def process_item(self, item, spider):
        line = [item['title'], item['author'], item['detail']]
        self.ws.append(line)
        self.wb.save(self.file_name)
        return item

    def close_spider(self, spider):
        # 关闭
        self.wb.close()

