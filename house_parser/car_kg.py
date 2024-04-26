# import httpx
# from parsel import Selector
# from bot import dp, types
# from aiogram import Router
# from aiogram.filters import Command
#
# car_router = Router()
#
#
# class HouseCrawler:
#     MAIN_URL = "https://www.house.kg/snyat"
#     BASE_URL = "https://www.house.kg"
#
#
#     async def get_page(self):
#             async with httpx.AsyncClient() as client:
#                 response = await client.get(self.MAIN_URL)
#                 self.page_content = response.text
#                 return response
#     async def get_title(self):
#             html = Selector(self.page_content)
#             title = html.css("title::text").get()
#             return title
#
#     async def get_car_links(self):
#         html = Selector(self.page_content)
#         links = html.css('.property-list .property-item a::attr(href)').getall()
#         full_links = [self.BASE_URL + link for link in links]
#         print(full_links)
#         return full_links
#
#     @car_router.message(Command("links"))
#     async def links(message: types.Message):
#         crawler = HouseCrawler()
#         await crawler.get_page()
#         title = await crawler.get_title()
#         link = await crawler.get_car_links()
#         await message.answer(f"Имя: {title}, ссылка {link}")
#
import httpx
from parsel import Selector
from bot import dp, types
from aiogram import Router
from aiogram.filters import Command

car_router = Router()


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    async def get_page(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.MAIN_URL)
            self.page_content = response.text
            return response

    async def get_title(self):
        html = Selector(self.page_content)
        title = html.css("title::text").get()
        return title

    async def get_car_links(self):
        html = Selector(self.page_content)
        links = html.css('.property-list .property-item a::attr(href)').getall()
        full_links = [self.BASE_URL + link for link in links]
        print(full_links)
        return full_links

    @car_router.message(Command("links"))
    async def links(message: types.Message):
        crawler = HouseCrawler()
        await crawler.get_page()
        title = await crawler.get_title()
        link = await crawler.get_car_links()
        await message.answer(f"Имя: {title}, ссылка {link}")

