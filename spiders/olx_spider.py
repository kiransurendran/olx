# -*- coding: utf-8 -*-
import scrapy


class OlxSpiderSpider(scrapy.Spider):
    name = 'olx_spider'
    allowed_domains = ['olx.in']
    # start_urls = ['http://olx.in/']
    def start_requests(self):
        yield scrapy.Request(url='https://www.olx.in/mumbai_g4058997/q-cycle',callback=self.parse)

    def parse(self, response):
        # pass
        for cycle in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
           _link= cycle.xpath(".//a/@href").extract_first()
           prod_link = 'olx.in'+ _link
           yield scrapy.Request(url=prod_link, callback=self.parse_data)
           # yield{
            #     'product_name': cycle.xpath(".//a/div/span[@class='_2tW1I']/text()").extract_first(),
            #     'link': cycle.xpath(".//a/@href").extract_first()
            # }
    
    def parse_data(self,response):
        
           
            

# //ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']