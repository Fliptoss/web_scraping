import scrapy
from bs4 import BeautifulSoup

class BlogSpider(scrapy.Spider):
    name = 'naturospider'
    start_urls = ['https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu']

    def parse(self, response):

        for href in response.css('.smw-columnlist-container a::attr(href)').getall():
            yield scrapy.Request(url="https://naruto.fandom.com" + href, callback=self.parse_jutsu)

   
        next_page = response.css('a.mw-nextlink::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_jutsu(self, response):

        jutsu_name = response.css("span.mw-page-title-main::text").get()
        if jutsu_name:
            jutsu_name = jutsu_name.strip()
        else:
            jutsu_name = "Unknown"

   
        div_selector = response.css("div.mw-parser-output").get()
        soup = BeautifulSoup(div_selector, "html.parser")

        jutsu_type = ""
        aside = soup.find('aside')
        if aside:
            for cell in aside.find_all('div', {'class': 'pi-data'}):
                header = cell.find('h3')
                if header and header.text.strip() == "Classification":
                    jutsu_type = cell.find('div').text.strip()

  
            aside.decompose()

        jutsu_description = soup.get_text(strip=True)
        jutsu_description = jutsu_description.split('Trivia')[0].strip()


        yield {
            "jutsu_name": jutsu_name,
            "jutsu_type": jutsu_type,
            "jutsu_description": jutsu_description
        }
