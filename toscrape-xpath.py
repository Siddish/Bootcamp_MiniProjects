import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'text': quote.xpath(".//span[@class='text']/text()").extract_first(),
                'author': quote.xpath(".//small[@class='author']/text()").extract_first(),
                'tags': quote.xpath(".//div[@class='tags']/text()").extract()
            }