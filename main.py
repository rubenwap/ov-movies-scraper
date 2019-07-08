import scrapy
from scrapy.crawler import CrawlerProcess
from vosmovies.spiders.phenomena import PhenomenaSpider
from vosmovies.spiders.verdi import VerdiSpider
from concurrent.futures import ThreadPoolExecutor

def start_crawl(crawler):
    process = CrawlerProcess()
    process.crawl(crawler)
    process.start()

def main():
    with ThreadPoolExecutor(2) as thread:
        thread.map(start_crawl, CRAWL)

if __name__ == "__main__":
    CRAWL = [PhenomenaSpider, VerdiSpider]
    main()
    
