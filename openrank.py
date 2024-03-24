import requests


def api_hit_get(url):

    url = url

    response = requests.request("GET", url)

    return(response.json())

def api_hit_post(url, values):

    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    }

    json_data = values

    response = requests.post(url, headers=headers, json=json_data)
    return(response.json())



url_1 = "https://graph.cast.k3l.io/scores/global/following/fids"
url_2 = "https://graph.cast.k3l.io/scores/global/following/handles"
url_3 = "https://graph.cast.k3l.io/scores/global/engagement/fids"
url_4 = "https://graph.cast.k3l.io/scores/global/engagement/handles"
url_5 = "https://graph.cast.k3l.io/scores/personalized/following/fids"
url_6 = "https://graph.cast.k3l.io/scores/personalized/following/handles"
url_7 = "https://graph.cast.k3l.io/scores/personalized/engagement/fids"
url_8 = "https://graph.cast.k3l.io/scores/personalized/engagement/handles"
url_9 = f"https://graph.cast.k3l.io/scores/global/following/rankings?offset={offset}&limit={limit}"
url_10 = f"https://graph.cast.k3l.io/scores/global/engagement/rankings?offset={offset}&limit={limit}"
url_11 = f"https://graph.cast.k3l.io/frames/personalized/rankings/fids"
url_12 = "https://graph.cast.k3l.io/frames/personalized/rankings/handles"
url_13 = "https://graph.cast.k3l.io/frames/global/rankings"