from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Shop():

    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def add_item_to_cart_and_checkout(self, List_of_products):
        # Get WebElements, css:.card-title
        i = 1
        productTitles = self.selLib.get_webelements("css:.card-title")
        # Loop through the list of product titles
        for productTitles in productTitles:
            # Get the text of the product title if it is in the productsList
            if productTitles.text in List_of_products:
                # Click on the card-footer button
                self.selLib.click_button("xpath:(//*[@class='card-footer'])["+str(i)+"]/button")

            # Increment the counter
            i += 1

        # Click on the cart link
        self.selLib.click_link("css:li.active a")
