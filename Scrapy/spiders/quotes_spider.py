import scrapy
from  tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'grupomansion'
    start_urls = [
        'https://grupomansion.com/product-category/audio-y-video/televisores/?product_orderby=price',
        'https://grupomansion.com/product-category/audio-y-video/neveras/?product_orderby=price',
        'https://grupomansion.com/product-category/audio-y-video/lavadoras/?product_orderby=price',
    ]

    def parse(self, response):
    
       items = TutorialItem()
       
       for producto in response.css('div.product-details-container'):
         
         items['tienda'] = 'grupoMansion'
         items['categoria'] = producto.xpath('h3/a/text()').get().split(' ', 1)[0]
         items['nombre'] = producto.xpath('h3/a/text()').get().encode("utf-8")
         items['precio'] = producto.xpath('div/span/ins/span/bdi/text()').get()
         items['url'] = producto.xpath('h3/a/@href').get()
          
         
         yield  items

         
