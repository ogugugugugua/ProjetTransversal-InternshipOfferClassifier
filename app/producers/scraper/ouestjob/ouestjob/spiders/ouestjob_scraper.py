import scrapy
import re
import json

class OuestjobSpider(scrapy.Spider):
    name = 'ouestjob'
    start_urls = [
        'https://www.ouestjob.com/emplois/recherche.html?k=d%C3%A9veloppeur+stagiaire&ray=20&p=1',
    ]

    def parse(self, response):
        if response.css('#noResult'):
            raise scrapy.exceptions.CloseSpider('No result')


        for offer in response.css('div[data-offerid]'):
            yield response.follow(offer.css('div>h3>a::attr(href)').get(), self.parse_offer)
        

        next_page = re.sub('(\d+)(?!.*\d)', lambda x: str(int(x.group(0)) + 1), response.request.url)
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    
    def parse_offer(self, response):
        yield{
            'id' : json.loads(response.css('section[data-job-description]::attr(data-job-description)').get())['idoffer'],
            'title': response.css('li.single:first-of-type span+span::text').get(),
            'company': json.loads(response.css('section[data-job-description]::attr(data-job-description)').get())['company']
            # 'description': response.css('section[data-job-description]>p').get()
        }


