import requests
from pprint import pprint
import html_to_json
import util as util


def scrap_decklist_metadata():
    base_url = 'https://fabtcg.com/decklists/?query='
    response = requests.get(base_url)


    if response:
        response.encoding = 'utf-8'

        # there is something malformed so trying to use panda and a xml tree produce odd results
        # html_to_json returns it in a list of lists so pulling off the outer layer 
        table_info = html_to_json.convert_tables(response.text)[0]
        
        for row in table_info:
    
            pprint(util.deck_url_creator(row['Decklist']))



if __name__ == "__main__":
    scrap_decklist_metadata()
