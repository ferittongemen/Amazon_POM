class SearchResultsLocators:
    SECOND_PAGE_LINK = "//a[@aria-label='Go to page 2']"
    SECOND_PAGE_LOADED_INDICATOR = "//span[contains(text(), 'results for')]"  # Sayfa yüklenmesini doğrulamak için bir gösterge
    THIRD_PRODUCT_LINK = "(//div[@data-component-type='s-search-result']//h2/a)[3]"
    LISTEYE_EKLE_BUTTON_DROPDOWN = "add-to-wishlist-button-submit"
    RESULTS_TEXT = "div.s-main-slot"