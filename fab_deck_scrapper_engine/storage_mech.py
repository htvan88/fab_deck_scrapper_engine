from decklist_metadata import DecklistMetadata

# temp storage to flat file until database is set up
def store_metadata(metadata_list:list):
    with open('data_store.txt', 'w') as file:
        file.write(DecklistMetadata.print_headers() + '\n')
        for decklist_metadata in metadata_list:
            file.write(decklist_metadata.print_str() + '\n')


