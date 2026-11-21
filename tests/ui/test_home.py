import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from config.settings import BASE_URL


@pytest.mark.smoke
def test_home_page_opens(page: Page):
    page.goto(BASE_URL)
    home_page = HomePage(page)

    expect(home_page.product_names.first).to_be_visible()


@pytest.mark.smoke
def test_search_product(page: Page):
    page.goto(BASE_URL)

    home_page = HomePage(page)
    home_page.search_product("hammer")

    product = home_page.product_names.filter(has_text="Hammer").first
    expect(product).to_be_visible()


@pytest.mark.smoke
def test_search_nonexistent_product(page: Page):
    page.goto(BASE_URL)
    
    home_page = HomePage(page)
    expect(home_page.product_names.first).to_be_visible()

    home_page.search_product("xyznonexistent12345")

    expect(home_page.no_results).to_have_text(
        "There are no products found."
    )
    expect(home_page.product_names).to_have_count(0)



