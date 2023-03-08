from bs4 import BeautifulSoup
import requests

url = 'https://phimmois.net/danh-sach/phim-chieu-rap'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movieDataDictionary = {}
for item in soup.find_all('a', class_="tip"):
    link_tag = item.get('href')
    title = item.get('title')

    # Get the HTML code of the link
    html_code = requests.get(link_tag).text
    link_soup = BeautifulSoup(html_code, 'html.parser')

    img = link_soup.find('img', class_="ts-post-image wp-post-image attachment-post-thumbnail size-post-thumbnail")
    movieDataDictionary[title] = "Link: " + str(link_tag) + "\n\t" + "Image: " + "https://phimmois.net" + str(img.get('src') + "\n")

idx = 1
for key, value in movieDataDictionary.items():
    print('Phim số {}: \n\t{} \n\t{}'.format(idx, key, movieDataDictionary[key]))
    idx += 1
