import requests
from bs4 import BeautifulSoup

#Amazon page for Seiko watches
url = "https://www.amazon.com/stores/Seiko/ALL+MENS/page/CA349E12-6492-4EA0-A90C-D636AEA66FC3"
section_dict = {}

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

# Which section do we chose for our selection of scraping
sections = soup.select(".style__itemInfo__3C9wg")

for section in sections:
    # Only for sections that have a headline
    if section.select(".style__title__3Z2Cu"):
        # Grab sections model name and price
        model_name = section.select(".style__title__3Z2Cu")[0].text.strip()

        model_price = section.select(".style__price__2Zrre")
        model_price = section.select(".style__price__2Zrre")[0].text.strip()


        # Add one product to our datastructure
        section_dict[model_name] = {"Price": model_price}

# And this is how we want our data structure to look like
for model_name, section_info in section_dict.items():
    print(model_name)
    print((section_info['Price']))
    print("########################")
    print("\n\n")