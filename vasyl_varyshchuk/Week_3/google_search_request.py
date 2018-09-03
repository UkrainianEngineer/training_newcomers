"""
This module sends a request to google.com returning the response headers
and the specified number of searching results
"""
import requests
from pip import main
from pip.req import parse_requirements


def install_required_modules():
    """This function performs installation of required modules from requirements.txt file"""
    required_modules = parse_requirements('requirements.txt', session=False)
    requirements = [str(i.req) for i in required_modules]
    for requirement in requirements:
        main(['install', requirement])


try:
    from bs import BeautifulSoup
except ImportError:
    user_answer = None
    while user_answer not in ('y', 'n'):
        user_answer = raw_input('To run this module you need to install bs4 library. Would you like to install '
                                'bs4? [y/n]:')
        print(user_answer)
        if user_answer == 'y':
            print('Trying to install required module.')
            install_required_modules()
            from bs4 import BeautifulSoup
            break
        elif user_answer == 'n':
            print('Module bs4 was not installed')
            break


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
    and return list of these titles
    """
    soup = BeautifulSoup(response.text, 'lxml')
    search_titles = []
    for item in soup.select('h3.r'):
        search_titles.append(item.text)
        print(item.text)
        print('------------------------------------------')
    return search_titles


# Send searching request
search_response = google_search_request('Python', 5)
print(search_response.text)

# Print response headers
parse_headers(search_response)

# Display titles for searching results
show_search_result_titles(search_response)
