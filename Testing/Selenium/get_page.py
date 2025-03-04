from bs4 import BeautifulSoup
from urllib3.util import Retry
from selenium import webdriver
from requests.adapters import HTTPAdapter
from requests import get, Session



URL = "https://www.wynikilotto.net.pl/lotto/wyniki/"
retries = 0
success = False

driver = webdriver.Chrome()
driver.implicitly_wait(30)

try:
    # checking if there is some response from the server
    resp = get(URL)
    html = resp.text
    # making beautiful response
    soup = BeautifulSoup(html, "html.parser")

    # Returning a copy of the html string with leading and trailing whitespace removed from the body
    print(soup.body.get_text().strip(), "\n")
    # Service Unavailable
    # 
    # The server is temporarily busy, try again later!

    # Managing server response code
    if resp.status_code == 200:
        print("Everything is ok", "\n")
        # Getting specified html address
        driver.get("https://www.wynikilotto.net.pl/lotto/wyniki/")
    else:
        try:
            # defining retry logic
            retry = Retry(
                total=5, # maximum number of retries to perform
                backoff_factor=2,
                status_forcelist=[429, 500, 502, 503, 504], # specifies which HTTP error codes should trigger request retries
            )
            # defining adapter
            adapter = HTTPAdapter(max_retries=retry)

            # Creating session object, which uses the same parameters and configurations for multiple requests
            session = Session()
            # Using mount method to attach the adapter for the 'https://' URL prefix
            session.mount('https://', adapter)
            # Running session with 'GET' method
            run = session.get("https://www.wynikilotto.net.pl/lotto/wyniki/", timeout=180)
            print(run.status_code, "\n") # 503
        except Exception as e:
            print(e)
            # HTTPSConnectionPool(host='www.wynikilotto.net.pl', port=443):
            # Max retries exceeded with url: /lotto/wyniki/ (Caused by ResponseError('too many 503 error responses'))
except:
    print("Bad URL")
