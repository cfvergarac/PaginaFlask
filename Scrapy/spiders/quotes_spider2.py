import scrapy
from  tutorial.items import TutorialItem


class electrojaponesa(scrapy.Spider):
    name = 'electrojaponesa'
    start_urls = [
        'https://www.electrojaponesa.com/tv-audio--y-video/tv/smart-tv?PS=16&O=OrderByPriceASC',
        'https://www.electrojaponesa.com/electrohogar/refrigeracion/neveras-convencionales?PS=16&O=OrderByPriceASC',
        'https://www.electrojaponesa.com/electrohogar/lavado-y-secado/lavadora-carga-superior?PS=16&O=OrderByPriceASC',

    ]

    def parse(self, response):
       
       items = TutorialItem()
       
       for producto in response.css('a.vitrin-home'):
    
        items['tienda'] = 'electrojaponesa',
        items['categoria'] = producto.xpath('h4/text()').get().encode("utf-8").split(' ', 1)[0]
        items['nombre'] = producto.xpath('h4/text()').get().encode("utf-8")
        items['precio'] = producto.css('em.newPrice').get().split(' ', 1)
        
        yield  items
            

         