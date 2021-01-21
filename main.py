import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def scraping(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    data = driver.find_elements_by_xpath('//div[@class="M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"]')
    data_list = data[0].text.split('\n')
    driver.close()

    new_list = list()
    new_list.append(data_list[0])
    lst1, lst2 =  data_list[1][:3], data_list[1][3:]
    new_list.append(lst1)
    new_list.extend([lst2[i:i + 10] for i in range(0, len(lst2), 10)])

    for i in range(2, len(data_list)):
        if i % 2 != 0:
            new_list.extend(data_list[i].split(" "))
        else:
            new_list.append(data_list[i])

    # Writing in the CSV file
    filename = './cash-flow.csv'

    with open(filename, 'a+', newline='') as file:
        f = csv.writer(file)
        for i in range(0, len(new_list) - 1, 5):
            f.writerow([new_list[i], new_list[i + 1], new_list[i + 2], new_list[i + 3], new_list[i + 4]])


if __name__ == "__main__":
    url = 'https://finance.yahoo.com/quote/GOOG/cash-flow?p=GOOG'
    scraping(url)
