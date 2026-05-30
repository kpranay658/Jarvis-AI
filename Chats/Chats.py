import random
def ReplyToQuery(Query):
    if "hello" in Query: return random.choice(['Hii Sir', 'Hello'])
    if "how are you" in Query: return "I am fine"
    return None
