import scrapy


class DucanhSpider(scrapy.Spider):
    name = 'ducanh'
    allowed_domains = ['https://www.thegioididong.com/dtdd']
    start_urls = ['https://www.thegioididong.com/dtdd/']

    def parse(self, response):
        name = response.css('.listproduct h3::text').extract()
        price = response.css('.listproduct .price::text').extract()
        discount = response.css('.listproduct .percent::text').extract()
        rowdata = zip(name, price, discount)

        for phone in rowdata:
            scraped = {
                'title': phone[0],
                'price': phone[1],
                'discount': phone[2]
            }
            yield scraped
            
        pass
