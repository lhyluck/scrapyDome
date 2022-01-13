# Scrapy settings for FirstSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FirstSpider'

SPIDER_MODULES = ['FirstSpider.spiders']
NEWSPIDER_MODULE = 'FirstSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
# Configure maximum concurrent requests performed by Scrapy (default: 16) Scrapy 下载器将执行的最大并发（即并发）请求数
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载程序在从同一网站下载连续页面之前应等待的时间（以秒为单位）
DOWNLOAD_DELAY = 3 
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16  #将对任何单个域执行的最大并发（即并发）请求数
#CONCURRENT_REQUESTS_PER_IP = 16 #将对任何单个 IP 执行的最大并发（即并发）请求数

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default) 是否将启用telnet 控制台（前提是其扩展也已启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers: 用于 Scrapy HTTP 请求的默认标头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares  激活蜘蛛中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'FirstSpider.middlewares.FirstspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares 激活下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'FirstSpider.middlewares.FirstspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions 加载和激活扩展
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines 激活项目管道组件,项目从值较低的类转到值较高的类。习惯上在 0-1000 范围内定义这些数字
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 启用图像管道
   'FirstSpider.pipelines.imgsPipeLine': 300,
   # 启用excel管道
   'FirstSpider.pipelines.ExcelPipeline': 301,
   # 启用文件管道
   #'scrapy.pipelines.files.FilesPipeline': 1
}
# 存储下载图像目录
IMAGES_STORE = './imgs_tmp'
# 允许媒体管道重定向
MEDIA_ALLOW_REDIRECTS = True
# 图片最小高度和宽度设置，可以过滤太小的图片
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
 
# 生成缩略图选项
# IMAGES_THUMBS = {
#  'small': (50, 50),
#  'big': (270, 270),
# }

# 自动限速算法基于以下规则调整下载延迟
#1、spiders开始时的下载延迟是基于AUTOTHROTTLE_START_DELAY的值
#2、当收到一个response，对目标站点的下载延迟=收到响应的延迟时间/AUTOTHROTTLE_TARGET_CONCURRENCY
#3、下一次请求的下载延迟就被设置成：对目标站点下载延迟时间和过去的下载延迟时间的平均值
#4、没有达到200个response则不允许降低延迟
#5、下载延迟不能变的比DOWNLOAD_DELAY更低或者比AUTOTHROTTLE_MAX_DELAY更高
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 启用自动限制扩展
AUTOTHROTTLE_ENABLED = True
# The initial download delay 初始下载延迟（以秒为单位）
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies 在高延迟的情况下要设置的最大下载延迟（以秒为单位）
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server Scrapy 应与远程网站并行发送的平均请求数
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received: 启用自动限制调试模式，该模式将显示收到的每个响应的统计信息，因此您可以实时查看限制参数的调整方式
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 是否将启用 HTTP 缓存
#HTTPCACHE_ENABLED = True
# 缓存请求的过期时间（以秒为单位）
#HTTPCACHE_EXPIRATION_SECS = 0
# 用于存储（低级）HTTP 缓存的目录。如果为空，则将禁用 HTTP 缓存。如果给定了相对路径，则相对于项目数据目录采取
#HTTPCACHE_DIR = 'httpcache'
# 不要使用这些 HTTP 代码缓存响应
#HTTPCACHE_IGNORE_HTTP_CODES = []
# 实现缓存存储后端的类
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
