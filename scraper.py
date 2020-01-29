import scrapy
import time
import json


class ElixirLangSpider(scrapy.Spider):
    name = "elixir_spider"
    #start_urls = ['https://elixir-lang.org']
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    start_urls = [str(input('Insita url a ser crawleada >>>>'))]

    def __init__(self):
        self.document = []
        self.file_name = f'responses/{time.time()}.json'

    def parse(self, response):
        """=====================================================================
        Método que chama o parser de cada tela do site.
        ====================================================================="""
        # seletor de menu
        MENU_SELECTOR = 'a'
        for item in response.css(MENU_SELECTOR):
            # crio e envio urls para fazer requisição GET
            HREF_SELECTOR = '::attr(href)'
            yield self.get_secundary_page(response.urljoin(item.css(HREF_SELECTOR).extract_first()))

    def get_secundary_page(self, url):
        """=====================================================================
        Método que faz requisição GET em url.
        ====================================================================="""
        return scrapy.Request(url, callback=self.register)

    def register(self, response):
        """=====================================================================
        Método que parsea e registra informações estaticas de cada tela.
        ====================================================================="""
        # seletores
        title = response.css('title ::text').extract_first()
        css = response.xpath('//link[@rel="stylesheet"]').css('::attr(href)').getall()
        js = response.css('script::attr(src)').getall()
        img = response.css('img::attr(src)').getall()
        # adiciono registrom em resposta
        self.document.append(
            {
                "title": title,
                "css": css,
                "js": js,
                "img": img
            }
        )
        self.create_json()

    def create_json(self):
        """=====================================================================
        Método que cria json de resposta na pasta responses.
        ====================================================================="""
        arq = open(self.file_name, 'w')
        arq.write(json.dumps(self.document))
        arq.close()
