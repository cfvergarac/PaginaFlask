import scrapy
from  tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'grupomansion'
    start_urls = [
        'https://www.tiendasjumbo.co/tecnologia/televisores-y-video/televisores',
        'https://www.tiendasjumbo.co/electrodomesticos/refrigeracion/neveras',
        'https://www.tiendasjumbo.co/electrodomesticos/lavadoras-y-secadoras/lavadoras',

    ]

    def parse(self, response):
    
       items = TutorialItem()
       
       for producto in response.css('div.product-item__bottom'):
         
         items['tienda'] = 'jumbo'
         items['categoria'] = producto.xpath('div/a/span/text()').get().split(' ', 1)[0]
         items['nombre'] = producto.xpath('div/a/span/text()').get()
         precio = producto.xpath('div[2]/div[2]/span[2]/text()').get()
         items['precio'] = precio[1:]
         items['url'] = producto.xpath('div/a/@href').get()
         
         yield  items

         
