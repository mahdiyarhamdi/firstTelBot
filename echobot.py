import json
import requests
ه پ

TOKEN = "996900145:AAGsx_EoL1-D68sTLZGZWGm305wPhCMpep00" #token of my bot
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url): #simply downloads the content from a URL and gives us a string
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url): #gets the string response as above and parses this into a Python dictionary using json.loads()
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = "kos ngu ke "
    text = text + updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
while True :
    text, chat = get_last_chat_id_and_text(get_updates())
    send_message(text, chat)

