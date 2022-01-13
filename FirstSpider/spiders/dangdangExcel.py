import scrapy
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from FirstSpider.items import FirstspiderItem


class FirstSpider(scrapy.Spider):
    name = 'dangdangExcel'
    # 允许的域名：限定start_urls白名单
    # allowed_domains = ['www.baidu.com']
    # 起始的url列表：列表中的url会被scrapy自动进行请求发送
    # start_urls = ['https://nudebird.biz/']

    # # 数据解析；response响应对象
    # def parse(self, response):
    #     article_list = response.xpath('//div[@id="content_box"]/div/article/a')
    #     for article in article_list:
    #         src = article.xpath('./div/img/@data-lazy-src').extract_first()
    #         item = FirstspiderItem()
    #         item['src'] = src
    #         yield item

    start_urls = ['http://category.dangdang.com/cp01.24.13.00.00.00.html']
    custom_settings = {
        'ITEM_PIPELINES': {'FirstSpider.pipelines.ExcelPipeline': 301},
    }
    
    def parse(self, response):
        div_list = response.xpath('//*[@id="component_59"]/li')
        
        for div in div_list:
            item = FirstspiderItem()
            item['title'] = div.xpath('./a/@title').extract_first()
            item['author'] = div.xpath('./p[5]/span[1]/a/text()').extract_first()
            item['detail'] = div.xpath('./p[@class="detail"]/text()').extract_first()
            #请求地址根路径
            # base_url = get_base_url(response)  
            yield item
        # 获取下一页url //*[@id="12810"]/div[3]/div[2]/div/ul/li[10]/a
        # self.page_url = response.xpath(
        #     '//div[@class="paging"]//ul//li[10]//a/@href').extract()
        # # 当快结束时下一页xpath发生改变
        # if not self.page_url:
        #     self.page_url = response.xpath(
        #         '//div[@class="paging"]/ul/li[8]//a/@href').extract()
        # # page_url 是一个数组
        # for next_url in self.page_url:
        #     yield Request(urljoin("http://category.dangdang.com", next_url), callback=self.parse)

        for page in range(1,5):
            url = f'http://category.dangdang.com/pg{page}-cp01.24.13.00.00.00.html'
            yield Request(url, callback=self.parse)
