from decklist_metadata import DecklistMetadata
import json

def store_metadata(metadata_list:list):
    with open('data_store.txt', 'w') as file:
        for decklist_metadata in metadata_list:
            file.write(decklist_metadata.print_str() + '\n')
