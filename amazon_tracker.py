import requests
import bs4
import lxml


URL = "https://www.amazon.ca/Sunny-Health-Fitness-Hyperextension-Station/dp/B08NV3K3Z4?ref_=ast_sto_dp&th=1&psc=1"

headers = {
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/16.1 Safari/605.1.15 "
}
response = requests.get(URL, headers=headers)
website_html = response.text

soup = bs4.BeautifulSoup(website_html, "lxml")

price = soup.find(name="span", class_="a-offscreen")
print(price.get_text()[1:])
