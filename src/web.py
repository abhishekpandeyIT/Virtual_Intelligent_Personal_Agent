import webbrowser
import os

def close_browser():
    os.system("taskkill /im chrome.exe /f")

def open_facebook():
    webbrowser.open('https://www.facebook.com/')

def open_instagram():
    webbrowser.open('https://www.instagram.com/')

def open_google():
    webbrowser.open('https://www.google.com/')

def open_browser():
    webbrowser.open('https://www.google.com/')

def open_youtube():
    webbrowser.open("https://www.youtube.com/")
