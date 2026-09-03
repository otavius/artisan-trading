from scraping.utils import get_soup_file, get_soup_from_url
from urllib.parse import urljoin


# def bloomberg_com():

#     #soup = get_soup_file("bloomberg")
#     soup = get_soup_from_url("https://www.reuters.com/business/finance/")

#     articles = []

#     #cards = soup.find_all("div", class_=lambda x: x and "media-story-card__body" in x)
#     cards = soup.select('[class^="media-story-card__body"]')

#     for card in cards:
#         #headline_link = card.select_one('a[data-testid="Heading"]')
#         headline_link = card.find("a", attrs={'data-testid': "Heading"})
#         if headline_link: 
#             articles.append(dict(
#                 headline=headline_link.text,
#                 link="https://www.reuters.com" + headline_link["href"]
#             ))
#     return articles

REUTERS_URL = "https://www.reuters.com/business/finance/"

def reuters_com():
    soup = get_soup_from_url(REUTERS_URL)
    print(soup.prettify()[:2000])  # or len(str(soup))
    if soup is None:
        print(f"Failed to fetch or parse: {REUTERS_URL}")
        return []

    articles = []
    cards = soup.select('[class^="media-story-card__body"]')

    if not cards:
        print("No article cards found — selector may be stale, check page structure")
        return []

    for card in cards:
        headline_link = card.select_one('a[data-testid="Heading"]')
        if headline_link and headline_link.get("href"):
            articles.append({
                "headline": headline_link.get_text(strip=True),
                "link": urljoin(REUTERS_URL, headline_link["href"]),
            })

    return articles

