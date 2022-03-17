from decklist_metadata import DecklistMetadata
from pprint import pprint
import requests
import html_to_json
import util
import storage_mech


def scrap_decklist_metadata():
    base_url = 'https://fabtcg.com/decklists/?query='
    response = requests.get(base_url)

    if response:
        response.encoding = 'utf-8'

        # there is something malformed so trying to use panda and a xml tree produces odd results
        # html_to_json returns a list of lists so pulling off the outer layer right away
        table_info = html_to_json.convert_tables(response.text)[0]
        deck_metadata_list = []
        for row in table_info:
            decklist_metadata = DecklistMetadata(util.deck_url_creator(row['Decklist']),
                                                row['Hero'],
                                                util.rank_as_int(row['Result']),
                                                row['Format'],
                                                "tbd", #should be obtained in the next call to get the deck data, replacing the deck_url
                                                util.get_event_type(row['Decklist']),
                                                util.string_to_date(row['Date'])
            )
            deck_metadata_list.append(decklist_metadata)
        
        storage_mech.store_metadata(deck_metadata_list)


if __name__ == "__main__":
    scrap_decklist_metadata()
