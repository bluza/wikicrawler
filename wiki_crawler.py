"""

"""

from bs4 import BeautifulSoup
import requests
import re
from graph import Graph

def get_links_from_hub(hub):
    """
    fetch links from Hubpage
    :param hub: Link to a Wikipedia Hubpage
    :return: list of html <a> tags
    """
    soup = BeautifulSoup(hub, 'html.parser')
    return [link_a for link_a in soup.find(id="mw-whatlinkshere-list")]


def extract_links(tag):
    """
    extract the relative Wikipeda urls:
    e.g. /wiki/i_like_trains
    :param tag:
    :return: relative url as a string
    """
    extract_node_link_regex = '(?<=\<a href=\").*(?=\" title)'
    relative_url = re.search(extract_node_link_regex, str(tag))
    if type(relative_url) == re.Match:
        return str(relative_url[0])
    else: return ""



def create_incoming_link_list(links):
    """
    creates a list of relative URLS from the bs4 source
    :param links:
    :return:
    """
    hub_outgoing_link_list = []
    for list in links:
        text = str(list.next)
        if text != '\n' and text.startswith("<li>") is False:
            extractor = extract_links(text)
            hub_outgoing_link_list.append(extractor)
    return hub_outgoing_link_list

def create_connections(hub, hub_outgoing_links):
    hub_connection = []
    for outgoing_link in hub_outgoing_links:
        formater = "".join("('{0}','{1}')".format(hub, outgoing_link))
        #formater = "".join(hub, outgoing_link)
        #hub_connection.append(formater)
        hub_connection.append((hub,outgoing_link))
    return hub_connection

link_search_tag = '"<ul id="mw-whatlinkshere-list">"'
wiki = "https://de.wikipedia.org"
root_hub_page = "/wiki/Spezial:Linkliste/Adolf_Hitler"

root_hub_response = requests.get(wiki + root_hub_page)
html = root_hub_response.text
links = get_links_from_hub(html)

hub_link_list = create_incoming_link_list(links)
graphlist = create_connections("wiki/Adolf_Hitler", hub_link_list)

g = Graph(graphlist)

print(g)



