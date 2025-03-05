"""
getting table data using selenium:
You need:
----------
table_ID ( ***CTRL+SHIFT+I*** ---> find in 'Elements': '<table id="TABLE_ID" class="CLASS_NAME dataTAble" ...>' )
selenium (webdriver, common.by), pandas

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import read_html
from time import localtime, strftime


# using read_html() with html directly in it isn't available anymore ( example with html directly inside: 'pandas.read_html("https://example.com/")' ):
# ------------------------------------------------------------------------------------------------------------------------------------------------------
URL = "https://topforeignstocks.com/stock-lists/the-list-of-listed-companies-in-germany/"

# fse_collection = pd.read_html(StringIO(URL))

# if response is 'ValueError: No tables found':
# ----------------------------------------------
driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get(URL)
df = read_html(driver.find_element(By.ID, "tablepress-4608").get_attribute('outerHTML'))[0]
df

# Doing format of local time
PStimeData = localtime()
PScurrentDate = str(strftime("%Y-%m-%d", PStimeData))

# converting dataframe to CSV:
# -----------------------------
stockData_CSV = df.to_csv(PScurrentDate + "stock_data_FrankfurtStockExchange.csv", encoding='utf-8', index=False)
print("\n", "DataFrame from server saved to .csv", "\n")  # DataFrame from server saved to .csv for: TSLA

# converting dataframe to JSON:
# ------------------------------
stockData_JSON = df.to_json(PScurrentDate + "stock_data_FrankfurtStockExchange.json", indent=4)
print(" DataFrame from server saved to .json", "\n")  # DataFrame from server saved to .json for: TSLA
print("\n", df)
