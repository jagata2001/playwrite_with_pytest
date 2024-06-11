from playwright.sync_api import Page, expect
from time import sleep

class MoviePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.days = self.page.locator("//div/i[@style]/parent::div/div/div/div")
        self.cinema_list = self.page.locator("//div[contains(text(),'₾')]/parent::div")

    def wait_to_load(self) -> None:
        expect(self.days.nth(0)).to_be_visible()

    def get_available_cinema_list(self) -> set[str]:
        available_cinema_list = set()
        for day in self.days.all():
            day.click()
            [available_cinema_list.add(ticket.locator("//span[3]").inner_text()) for ticket in self.cinema_list.all()]
        return available_cinema_list

    def get_min_price_and_time_available(self) -> dict:
        ticket_data = { "cinema" : "NOT_FOUND", "time" : "NOT_FOUND", "price" : 999999999999999999 }
        for day in self.days.all():
            date = day.inner_text().replace("\n","")
            day.click()
            for ticket in self.cinema_list.all():
                cinema = ticket.locator("//span[3]").inner_text()
                time = ticket.locator("//span[1]").inner_text()
                price = float(ticket.locator("//div").inner_text().split(" ")[1])
                if(price < ticket_data["price"]):
                    ticket_data["cinema"] = cinema
                    ticket_data["time"] = f"{date} {time}"
                    ticket_data["price"] = price
        return ticket_data
   
            
