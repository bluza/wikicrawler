"""

"""

from bs4 import BeautifulSoup
import requests
import re


def get_links_from_hub(hub):
    soup = BeautifulSoup(hub, 'html.parser')
    return [link_a for link_a in soup.find(id="mw-whatlinkshere-list")]


def extract_links(tag):
    extract_node_link_regex = '(?<=\<a href=\").*(?=\" title)'
    relative_url = re.search(extract_node_link_regex, str(tag))
    return str(relative_url[0])


def create_incoming_link_list(links):
    hub_outgoing_link_list = list()
    for list in links:
        text = str(list.next)
        if text != '\n' and text.startswith("<li>") is False:
            extractor = extract_links(text)
            hub_outgoing_link_list.append(extractor)
    return hub_outgoing_link_list


link_search_tag = '"<ul id="mw-whatlinkshere-list">"'
wiki = "https://de.wikipedia.org"
root_hub_page = "/wiki/Spezial:Linkliste/Adolf_Hitler"

root_hub_response = requests.get(wiki + root_hub_page)
html = root_hub_response.text
links = get_links_from_hub(html)



