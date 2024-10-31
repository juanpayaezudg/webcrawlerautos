from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "buscadordenaves"
    allowed_domains = ["abacoautos.mx"]
    start_urls = ["https://www.abacoautos.mx/categoria-producto/seminuevo/"]
    
    rules = (
        Rule(
            LinkExtractor(allow="categoria-producto/seminuevo/"), 
            callback='parse_item', 
            follow=True
        ),
    )

    def parse_item(self, response):
        for anuncio in response.css('div.product'): 
            
            modelo = anuncio.css('h2.woocommerce-loop-product__title::text').get() or 'Sin modelo'
            link = anuncio.css('a::attr(href)').get() or 'Sin enlace'
            
            if "aveo" in modelo.lower():
                yield {
                    'modelo': modelo,
                    'link': response.urljoin(link)
                }
