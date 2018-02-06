import requests
from bs4 import BeautifulSoup

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRA-Tgc9b4jXCEv49D0qX9gmbJpP5xv9TwLCGtgJWGxdA4sdvGclk_AwQeH0fD4VhGnyS8caeV6Os8G/pubhtml?gid=0&single=true'

def retrieve_data():
    try:

        full_html = requests.get(url)
        parsed_html = BeautifulSoup(full_html.content, 'lxml')

        table_html = parsed_html.find('table')

        table_html['class'] = 'table table-hover'
        table_html['style'] = "table-layout: fixed; width: 100%;"
        del table_html.contents[0]
        table = table_html.contents[0]

        del table.contents[1]

        for row in table.contents:
            del row.contents[0]
        

        return table_html


    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return "Page not found, error: {}".format(e)