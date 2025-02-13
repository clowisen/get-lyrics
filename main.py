import os
import tkinter as tk
import spotipy
import pyperclip
from spotipy.oauth2 import SpotifyOAuth
from lyricsgenius import Genius
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri=os.getenv('REDIRECT_URL'), scope="user-read-currently-playing"))

root = tk.Tk()
root.iconbitmap("C:\PR\GetLyrics\icon\icon.ico")
root.configure(bg="#4f4f4f")

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    }

translator = Translator()

lang_list = []
for key,value in LANGUAGES.items():
    lang_list.append(value)

def get_lyrics(artist, song):
    try:
        lyrics_textbox.configure(state="normal")
        lyrics_textbox.delete("1.0", END)
        genius = Genius(os.getenv("GENIUS_TOKEN"))
        song = genius.search_song(artist, song)
        lyrics_textbox.insert(END,song.lyrics)
        lyrics_textbox.configure(state="disabled")
    except:
        messagebox.showerror("Get Lyrics","No results found! (Make sure you are not connected to a VPN.)")

def manuel_get_lyrics():
    manuel = Toplevel(root)
    manuel.iconbitmap("C:\PR\GetLyrics\icon\icon.ico")
    manuel.grab_set()
    manuel.resizable(False,False)
    manuel.geometry("220x140")
    manuel.title("Get Lyrics")

    artist_label = tk.Label(manuel, text="Artist")
    artist_entry = tk.Entry(manuel, width=30)

    artist_label.pack()
    artist_entry.pack()

    song_name_label = tk.Label(manuel, text="Song Name")
    song_name_entry = tk.Entry(manuel, width=30)

    song_name_label.pack()
    song_name_entry.pack() 

    search_button = tk.Button(manuel, font=('Ebrima',10), padx=10, pady=10, text="Search", command= lambda: get_lyrics(artist_entry.get(), song_name_entry.get()))
    search_button.pack(pady=10)

def get_spotify_current_song():
    artist = sp.currently_playing()["item"]["album"]["artists"][0]["name"]
    song_name = sp.currently_playing()["item"]["name"]
    return artist, song_name

def get_spotify_lyrics():
    try:
        get_lyrics(get_spotify_current_song()[0], get_spotify_current_song()[1])
    except:
        messagebox.showerror("Get Lyrics","No results found! (Make sure you are not connected to a VPN.)")

def translate(lang):
    lyrics_translate.configure(state="normal")
    lyrics_translate.delete("1.0", END)
    for key, value in LANGUAGES.items():
        if lang == value:
            src = key
            break
    translated = translator.translate(lyrics_textbox.get("1.0",END), src=translator.detect(lyrics_textbox.get("1.0",END)).lang, dest=lang).text
    lyrics_translate.insert(END,translated)
    lyrics_translate.configure(state="disabled")

textbox_frame = Frame(root, bg="#4f4f4f", cursor="arrow black")
textbox_frame.pack()
lyrics_textbox = tk.Text(textbox_frame, width=50, padx=10, pady=20)
lyrics_textbox.configure(state="disabled", bg="#828282", fg="white", bd=0, font=('Consolas',15,'bold'))
lyrics_textbox.grid(row=0, column=0, padx=15, pady=25)


def copy_text(text):
    pyperclip.copy(text)

popup_lyrics = Menu(root, tearoff = 0)
popup_lyrics.add_command(label ="Copy", command= lambda: copy_text(lyrics_textbox.get("1.0",END)))

  
def do_popup_lyrics(event):
    try:
        popup_lyrics.tk_popup(event.x_root, event.y_root)
    finally:
        popup_lyrics.grab_release()

lyrics_textbox.bind("<Button-3>", do_popup_lyrics)

    
lyrics_translate = tk.Text(textbox_frame, width=50, padx=20, pady=20)
lyrics_translate.configure(state="disabled", bg="#828282", fg="white", bd=0, font=('Consolas',15,'bold'))
lyrics_translate.grid(row=0, column=1)


popup_translated = Menu(root, tearoff = 0)
popup_translated.add_command(label ="Copy", command= lambda: copy_text(lyrics_translate.get("1.0",END)))

  
def do_popup_translated(event):
    try:
        popup_translated.tk_popup(event.x_root, event.y_root)
    finally:
        popup_translated.grab_release()

lyrics_translate.bind("<Button-3>", do_popup_translated)

button_frame = Frame(root, bg="#4f4f4f")
button_frame.pack()


manuel_search = tk.Button(button_frame, bd=0, font=('Ebrima',10), padx=10, pady=10, text="Manuel Search", command=manuel_get_lyrics)
manuel_search.grid(row=1, column=0, padx=20)

get_spotify_song = tk.Button(button_frame, bd=0, font=('Ebrima',10), padx=10, pady=10, text="Get Spotify Song", command=get_spotify_lyrics)
get_spotify_song.grid(row=1, column=1)


translate_frame = Frame(root, pady=20, bg="#4f4f4f")
translate_frame.pack()

lang = ttk.Combobox(translate_frame, font=('Ebrima',10), values=lang_list, state="readonly")
lang.current(0)
lang.grid(row=2, column=0)

translate_button = tk.Button(translate_frame, font=('Ebrima',10), bd=0, padx=5, pady=7, text="Translate", command= lambda: translate(lang.get()))
translate_button.grid(row=3, column=0, pady=8)

root.geometry("1300x800")
root.title("Get Lyrics")
root.resizable(False,False)
root.mainloop()




