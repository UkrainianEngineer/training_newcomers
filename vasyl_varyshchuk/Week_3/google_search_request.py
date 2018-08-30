"""
This module sends a request to google.com returning the response headers
and the specified number of searching results
"""
import requests
from bs4 import BeautifulSoup

user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}


def google_search_request(search_query, number_of_results=10):
    """Returns results for search query from google.com page"""
    url = 'https://www.google.com.ua/search?q={}&num={}'.format(search_query, number_of_results)
    response = requests.get(url, headers=user_agent)
    return response


def parse_headers(response):
    """This function returns headers from response"""
    headers = response.headers
    for key, value in headers.items():
        print(key, value)
    return headers


def show_search_result_titles(response):
    """
    This function displays titles of search results
    """
    soup = BeautifulSoup(response.text, 'lxml')
    search_result_titles = soup.select('h3.r')

    for count, title in enumerate(search_result_titles, 1):
        print(count, title.text)
        print('------------------------------------------')


# Send searching request
search_response = google_search_request('Python', 5)

# Print response headers
parse_headers(search_response)

# Display titles for searching results
show_search_result_titles(search_response)

