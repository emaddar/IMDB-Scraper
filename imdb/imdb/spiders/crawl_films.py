import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlFilmsSpider(CrawlSpider):
    name = 'crawl_films'
    allowed_domains = ['imdb.com']
    # start_urls = ['https://www.imdb.com/chart/top/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/', headers={
            'User-Agent': self.user_agent
        })


    le_films_details = LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a")
    le_films_details_acteurs = LinkExtractor(restrict_xpaths='//*[@id="iconContext-chevron-right-inline"]/path')
    
    
    rule_films_details = Rule(le_films_details,
                             callback='parse_item',
                              follow=False)

    
    
    rule_films_details_acts = Rule(le_films_details_acteurs,
                            callback='parse_item',
                            follow=True)
                            
    rules = (
      rule_films_details  , rule_films_details_acts
    )

    def parse_item(self, response):

        # languages = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[13]/div[2]/ul/li[4]/div/ul/li/a/text()').extract()
        title = response.xpath('//h1/text()').extract()
        year = response.xpath('//span[@class="sc-8c396aa2-2 itZqyK"]/text()').extract_first()
        duration = response.xpath('//li[@class="ipc-inline-list__item"]/text()').extract()
        note = response.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()').extract_first()
        n_total = response.xpath('//div[@class="sc-7ab21ed2-3 dPVcnq"]/text()').extract_first()
        Genre = response.xpath('//span[@class="ipc-chip__text"]/text()').extract()
        Descriptions = response.xpath('//span[@class="sc-16ede01-2 gXUyNh"]/text()').extract()
        Director = response.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').extract_first()
        Acteurs = response.xpath('//a[@class="sc-bfec09a1-1 gfeYgX"]/text()').extract()
        Public = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/a/text()').extract()
        Pays = response.xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").extract()
        languages = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section/div[2]/ul/li[4]/div/ul/li/a/text()').extract()
        avis = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[1]/a/span/span[1]/text()').extract()
        Metacritic = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[2]/a/span/span[1]/text()').extract()
        

        yield{ 
            'Metacritic' : Metacritic,
            'avis' : avis,
            'Pays' : Pays,
            'languages' : languages,
            'title': title,
            'year' : year,
            'duration' : duration,
            'note' : note,
            'n_total' : n_total,
            'Genre' : Genre,
            'Director' : Director,
            'Acteurs' : Acteurs,
            'Public' : Public,



            'Descriptions' : Descriptions,
            
        }




