from datetime import datetime

class DecklistMetadata:
    def __init__(self, deck_url:str, hero:str, ranking:int, format:str, player:str, event_type:str, date:datetime):
        self.deck_url = deck_url
        self.hero = hero
        self.ranking = ranking
        self.format = format
        self.player = player
        self.event_type = event_type
        self.data = date


    def print_str(self) -> str:
        return f'{self.deck_url}, {self.hero}, {self.ranking}, {self.format}, {self.player}, {self.event_type}, {self.data}'
