from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('[data-test="search-query"]')
        self.search_button = page.locator('[data-test="search-submit"]')
        self.product_names = page.locator('[data-test="product-name"]')
        self.no_results = page.locator('[data-test="no-results"]')

    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

