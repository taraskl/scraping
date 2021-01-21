import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def scraping(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    data = driver.find_elements_by_xpath('//div[@class="M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"]')
    data_list = data[0].text.split('\n')
    driver.close()

    # Writing in the CSV file
    filename = './cash-flow.csv'

    with open(filename, 'a+', newline='') as file:
        f = csv.writer(file)
        for i in range(0, len(data_list) - 1, 2):
            f.writerow([data_list[i], data_list[i + 1]])


if __name__ == "__main__":
    url = 'https://finance.yahoo.com/quote/GOOG/cash-flow?p=GOOG'
    scraping(url)
