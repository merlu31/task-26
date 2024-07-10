import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.explicit_wait(10)
    yield driver
    driver.close()
    driver.quit()


paths = r"C:\Users\Merlin Archana\chromedriver-win64\chromedriver-win64"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(500, 500);")
time.sleep(20)
# Open the filmography section
credits = driver.find_element(By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label').click()
time.sleep(2)

# Find the credit input element
credit = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit, "Holiday")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()

# Confirmation
print("Search performed successfully.")
