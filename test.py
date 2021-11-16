from urllib import request
from bs4 import BeautifulSoup

url = 'https://amaryllis1204.github.io/Date.io/'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
text = soup.find_all('p')
response.close()

# with open('test.txt', 'w') as f:
#     f.write(text)

print(text)