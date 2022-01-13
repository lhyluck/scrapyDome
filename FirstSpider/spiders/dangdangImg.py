import scrapy
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from FirstSpider.items import FirstspiderItem


class FirstSpider(scrapy.Spider):
    name = 'dangdangImg'
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
        'ITEM_PIPELINES': {'FirstSpider.pipelines.imgsPipeLine': 300},
    }
    
    def parse(self, response):
        # div_list = response.xpath('//*[@id="search_nature_rg"]/ul/li/a')
        # //*[@id="component_59"]
        div_list = response.xpath('//*[@id="component_59"]/li/a')
        
        for div in div_list:
            # 图片懒加载，动态加载后src，为没有浏览器页面加载时为src2，
            # 注意：使用伪属性（不一定是src2，也可能是其他）
            src = div.xpath('./img/@data-original').extract_first()
            if src is None:
                src = div.xpath('./img/@src').extract_first()
            # print(src)
            pgname = div.xpath('./img/@alt').extract_first()

            item = FirstspiderItem()
            item['image_urls'] = 'http:'+src
            item['images_name'] = pgname
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

        for page in range(1,2):
            url = f'http://category.dangdang.com/pg{page}-cp01.24.13.00.00.00.html'
            yield Request(url, callback=self.parse)
