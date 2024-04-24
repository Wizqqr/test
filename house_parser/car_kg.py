import httpx
from parsel import Selector
from bot import dp, types
from aiogram import Router
from aiogram.filters import Command

car_router = Router()
class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text

    def get_title(self):
        html = Selector(self.page)
        title = html.css("title::text").get()
        return title

    def get_car_links(self):
        html = Selector(self.page)
        links = html.css(".list-item a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:3]

@dp.message(Command("links"))
async def links(message: types.Message):
    crawler = HouseCrawler()
    crawler.get_page()
    crawler.get_car_links()
    await message.answer(crawler.get_car_links())
