from Functions.Website import Websiter
from Functions.open import Opener
from Functions.search import Search
from Functions.youtube import youtube
from Functions.whatsapp import whatsapp

def ActionToQuery(Query):
    Query = Query.lower()
    if any(i in Query for i in ['visit', 'launch']):
        Websiter(Query.replace('visit', '').replace('launch', '').strip())
    elif any(i in Query for i in ['open', 'start']):
        Opener(Query.replace('open', '').replace('start', '').strip())
    elif any(i in Query for i in ['search', 'find']):
        Search(Query.replace('search', '').replace('find', '').strip())
    elif 'play' in Query:
        youtube(Query.replace('play', '').strip())
    elif any(i in Query for i in ['text', 'message']):
        whatsapp(Query)
