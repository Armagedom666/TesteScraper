from pathlib import Path
import scrapy


class LotoSpider(scrapy.Spider):
    name = "loto"

    def start_requests(self):
        urls = [

        ]
