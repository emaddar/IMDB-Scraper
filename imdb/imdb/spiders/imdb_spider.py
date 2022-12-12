import scrapy

class imdbSpider(scrapy.Spider):
    name = 'imdb_name'
    start_urls = [    
        'https://www.imdb.com/chart/top/'
    ]

    def parse(self, response):
        # title = response.css('title::text')[0].extract()
        # title = response.css('title::text').extract_first()   # extract_first is better than [0]
        title = response.css('h1.header::text').extract()
        title_subtitle = response.css('div.byline::text').extract()
        yield {'titletext' : title, 'title_subtitle' : title_subtitle}