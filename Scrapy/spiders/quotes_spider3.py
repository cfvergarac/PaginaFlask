import scrapy
from  tutorial.items import TutorialItem


class electrojaponesa(scrapy.Spider):
    name = 'olimpica'
    start_urls = [
        'https://www.oportunidades.com.co/televisores-y-video',
        'https://www.oportunidades.com.co/refrigeracion/neveras',
        'https://www.oportunidades.com.co/lavado-y-secado/Lavadoras',
        
    ]

    def parse(self, response):
       
       items = TutorialItem()
       
       for producto in response.css('div.data'):
    
        items['tienda'] = 'Oportunidades'
        items['categoria'] = producto.xpath('a/text()').get().encode("utf-8").split(' ', 1)[0]
        items['nombre'] = producto.xpath('a/text()').get().encode("utf-8")
        precio = producto.xpath('div/span[2]/text()').get().encode("utf-8")
        items['precio'] = precio[18:-13]
        items['url'] = producto.xpath('a/@href').get()
        #items['precio'] = producto.xpath('div/span/text()').get().encode("utf-8")
        
        yield  items
            

         