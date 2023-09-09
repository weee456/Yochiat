import requests
from tkinter import Tk
from bs4 import BeautifulSoup

a = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
class Client:
    def __init__(self, url: str):
        self.url = url
        
    
    def connect_for_get(self, target: str):
        self.req = requests.get(self.url)
        return BeautifulSoup.get()

client = Client("https://roblox.com")
client.connect_for_get(target="a")