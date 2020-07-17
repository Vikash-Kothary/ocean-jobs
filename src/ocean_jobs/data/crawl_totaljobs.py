import os
from scrapy.crawler import CrawlerProcess
from ocean_jobs.data.spiders.totaljobs import JobSpider

def run_crawler(output_file):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': output_file,
        'LOG_LEVEL': 'INFO'
    })
    process.crawl(JobSpider)
    process.start() # the script will block here until the crawling is finished

if __name__ == '__main__':
    output_file = 'data/raw/totaljobs.csv'
    run_crawler(output_file)
