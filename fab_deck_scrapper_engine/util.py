
def deck_url_creator(data:str) -> str:
    url = "https://fabtcg.com/decklists/" + data.replace(" ", "-").replace(".", "").lower()
    return url