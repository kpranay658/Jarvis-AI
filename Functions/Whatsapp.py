from pywhatkit import sendwhatmsg_instantly
CONTACTS = {"mom": "+919923671146", "dad": "+918888762005"}
def whatsapp(query):
    words = query.split()
    target = words[1].lower()
    msg = " ".join(words[2:])
    if target in CONTACTS: sendwhatmsg_instantly(CONTACTS[target], msg)
