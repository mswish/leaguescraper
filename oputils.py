import bs4 as BeautifulSoup
from selenium import webdriver
import time


def get_op_html(summonerName):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
    # request string for op.gg
    reqString = f'https://na.op.gg/summoner/champions/userName={summonerName}'
    driver.get(reqString)
    tab_headers = driver.find_element_by_class_name("tabHeader")
    for tab_header in tab_headers:
        if tab_header.is_displayed():
            driver.execute_script("arguments[0].click()", tab_header)
            time.sleep(1)
            stats_table = driver.find_element_by_class_name("ChampionStatsTable")
            print(stats_table)

    driver.quit()
    driver.closer()
