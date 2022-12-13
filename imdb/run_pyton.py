from scrapy import cmdline
# cmdline.execute("scrapy runspider imdb/spiders/crawl_films.py -O films.csv".split())
cmdline.execute("scrapy runspider imdb/spiders/crawl_series.py -O series.csv".split())
