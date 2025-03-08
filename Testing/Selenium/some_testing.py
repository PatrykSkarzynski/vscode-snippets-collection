# from selenium.webdriver.common.keys import Keys
from requests.adapters import HTTPAdapter
from requests import get, Session
from urllib3.util import Retry
from bs4 import BeautifulSoup



def ServerRes():
    """
    | from requests_ip_rotator import ApiGateway, EXTRA_REGIONS
    |
    | Creation of gateway with 'start' and 'end' method:
    | ---------------------------------------------------
    | | gateway = ApiGateway("https://www.wynikilotto.net.pl")
    | | gateway.start()
    | |
    | | session = Session()
    | | session.mount("https://www.wynikilotto.net.pl", gateway)
    | | Only run this line if you are no longer going to run the script, as it takes longer to boot up again next time.
    | | gateway.shutdown()
    | |
    |
    |
    |
    |
    | Creation of gateway which will automatically start and end:
    | ------------------------------------------------------------
    | | with ApiGateway("https://www.wynikilotto.net.pl") as g:
    | | # creating session object which gives information that request is from webbrowser
    | | session = Session()
    | | # mounting gateway to the address
    | | session.mount("https://www.wynikilotto.net.pl", g)
    | | 
    | | # # creating session request which gives information that request is from webbrowser
    | | req = session.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
    | | print(req.status_code) # 504
    | |
    |
    """

    URL = "https://www.wynikilotto.net.pl/lotto/wyniki/"

    # creating session object which gives information that request is from webbrowser
    req = get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})

    # printing html
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    print(soup.body.get_text().strip())

    if req.status_code == 200:
        print("Everything is ok") # Everything is ok
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
            r = session.get('https://www.wynikilotto.net.pl/lotto/wyniki/', timeout=180)
            print(r.status_code) # 503
        except Exception as e:
            print(e)
            # HTTPSConnectionPool(host='www.wynikilotto.net.pl', port=443):
            # # Max retries exceeded with url: /lotto/wyniki/ (Caused by ResponseError('too many 503 error responses'))


class LottoResults:

    def ClickFcButtonAndIleLottoResults():
        from pandas import read_html
        from selenium import webdriver
        from json import dumps, JSONDecodeError
        from time import sleep, localtime, strftime
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import WebDriverException
        from selenium.webdriver.support import expected_conditions as EC

        driver = webdriver.Chrome()
        driver.implicitly_wait(30)

        URL = "https://www.wynikilotto.net.pl/lotto/wyniki/"
        
        websiteData = []

        # Getting specified html address
        driver.get(URL)

        # Printing driver title
        print(driver.title, "\n") # "Wyniki Lotto: aktualne i archiwalne\n"

        # Scrapping page source code
        # print("Page source: ", driver.page_source)

        try:
            '''
            |
            | Handling Acceptance on web page
            |
            '''
            # Find element by text in element
            element_agree = driver.find_element(By.CLASS_NAME, "fc-button-label")
            
            # Making 'click' action for element 'Zgadzam się' on the web page
            element_agree.click()
            
            '''
            |
            | Handling Dropdown list on web page
            |
            '''
            print("Acceptance on web page finished, program  now going to Handling dropdown list part\n")
            
            # Making program wait 10 seconds until the specified element 'ile' is located
            element_ile = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "ile"))
            )

            # Handling dropdown list on the web page
            dropdown = Select(element_ile); # selecting element
            dropdown.select_by_value("max") # selecting by value from elements dropdown
            
            # Making 'click' action on element 'ile' on the web page
            element_ile.click()

            '''
            |
            | Handling OK button without <class> or <id> on the web page
            |
            '''
            print("Handling dropdown list finished, program now going to Handling OK button part\n")
            
            # Clicking the specified BUTTON element 'OK', located by it's XPath and getting it attribute 'innerHTML'
            element_ok = driver.find_element(By.XPATH, '//*[@id="mainl"]/section/form[2]/fieldset/button')

            # Clicking on a button element
            element_ok.click()

            # Finding table by it's XPath and getting it attribute 'outerHTML'
            lotto_df = read_html(driver.find_element(By.XPATH, '//*[@id="mainl"]/section/div[2]/table').get_attribute('outerHTML'))
            # df = read_html(driver.find_element(By.CLASS_NAME, "naglowek").get_attribute('outerHTML'))[0]
            print(lotto_df)

            # Formatting local time
            PStimeData = localtime()
            PScurrentDate = str(strftime("%Y-%m-%d", PStimeData))

            try:
                # Adding data as dictionary to list 
                for d in lotto_df:
                    d = d.to_dict()
                    websiteData.append(d)
                print("Response data:", websiteData)
                # converting list with dictionaries to JSON
                lotto_data_jsn = dumps(websiteData, indent=4)
                # saving .json file with data from web page
                with open(PScurrentDate + "-lotto-response-all-results.json", "w") as f:
                    f.write(lotto_data_jsn)
            except JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                driver.quit()
        except WebDriverException as e:
            # Printing information about error
            print(f"Error: {e}\n")
            driver.quit()
        else:
            # Printing information about success
            print("ClickFcButtonAndIleLottoResults() finished without any error\n")
        finally:
            # Ending driver script
            driver.quit()
            # Handling end message
            if WebDriverException == True:
                print("\nWebDriverException occurred")
            else:
                print("\nNo error occurred")
        
    def PresenceOfElement():
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver = webdriver.Chrome()
        driver.implicitly_wait(30)

        URL = "https://www.wynikilotto.net.pl/lotto/wyniki/"
        websiteData = []

        # Getting specified html address
        driver.get(URL)

        # Printing driver title
        print(driver.title) # "Wyniki Lotto: aktualne i archiwalne\n"

        # Scrapping page source code
        # print("Page source: ", driver.page_source)

        try:
            # Making program wait 10 seconds until the specified element 'ile' is located
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "ile"))
            )
            # Printing specified element as text 
            print(element.text)
            ## 5
            ## 10
            ## 20
            ## 50
            ## 100
            ## 200
            ## 500
            ## Wszystkie
        except KeyError:
            # Printing information about error
            print("Something went wrong with key value")
        else:
            # Printing information about success
            print("PresenceOfElement() finished without any error")
        finally:
            driver.quit()

# ServerRes()
LottoResults.ClickFcButtonAndIleLottoResults()
# LottoResults.PresenceOfElement()