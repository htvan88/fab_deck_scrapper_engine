from datetime import datetime


def deck_url_creator(data:str) -> str:
    url = "https://fabtcg.com/decklists/" + data.replace(" ", "-").replace(".", "").lower()
    return url


def rank_as_int(rank:str) -> int:
    if rank != 'None':
        return int(rank[0])
    else: return ''

# format is embedded in the data, 
# check to see if keywords are present else return ''
def get_event_type(data:str) -> str:
    if data.find('proquest'):
        return 'proquest'
    elif data.find('armory'):
        return 'armory'
    else:
        return '' 

def string_to_date(date:str) -> datetime:
    return datetime.strptime(date, '%d %b %Y')