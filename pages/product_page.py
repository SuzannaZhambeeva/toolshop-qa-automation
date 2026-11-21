from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator('[data-test="product-name"]')
        self.product_price = page.locator('[data-test="unit-price"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.cart_quantity=page.locator('[data-test="cart-quantity"]')

    def add_to_cart(self):
        self.add_to_cart_button.click()