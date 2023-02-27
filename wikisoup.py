import sys

import requests
from bs4 import BeautifulSoup

def obtain_summary(soup):
    title = soup.select(".mw-page-title-main")[0]
    description = soup.select(".shortdescription")[0]
    summary = [title.string, description.string]
    for sibling in soup.find("h2").previous_siblings:
        if sibling.name == "p":
            summary.insert(2, sibling.get_text())
    return summary

def get_soup(search):
    res = requests.get(f"https://wikipedia.org/wiki/{search}", timeout=1)
    soup = BeautifulSoup(res.text, "html.parser")
    soup = soup.main
    return soup

def main(search):
    soup = get_soup(search)
    summary = obtain_summary(soup)
    return summary


if __name__ == "__main__":
    concat_search = "_".join(sys.argv[1:])
    summary = main(concat_search)
    for item in summary:
        print(item)
