
from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.cartrade.com/').text
soup = BeautifulSoup(site, 'lxml')

# To know number of elements :
temp = soup.find_all('a', class_='ncpalink2 imaglinknew')
tot_len = len(temp)
# print(len(temp))

my_link = soup.findAll('a', class_='ncpalink2 imaglinknew')
with open('cars_n.txt','w', encoding="utf-8") as file1:

    for itr in range(0, tot_len):

        k = my_link[itr]
        k1 = k.get('href')
        print("-"*14 + "*"*9 + "-"*15)
        print(k1)
        s = 'https://www.cartrade.com/' + str(k1)

        site1 = requests.get(s).text
        soup = BeautifulSoup(site1, 'lxml')
        l1 = soup.find_all('a',class_='s')
        l2 = soup.find_all('div', class_='price_text')

        ls1 = []

        for ele1, ele2 in zip(l1,l2):
            ls1.append(ele1.text)
            ls1.append(ele2.span.text)
            # print(ele1.text,ele2.span.text)
            print(ls1)
            name_price = ls1[0] + "," + ls1[1] + "\n"
            file1.write(name_price)

            ls1 = []


