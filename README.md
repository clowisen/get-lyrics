![Image](https://github.com/user-attachments/assets/6d68fcc7-0286-4c3d-852e-e9251b6248bb)
# API Keys

### Spotify
1. To authorize Spotify to be able to display the currently playing song, click on the link below and create an application.<br>
<a href="https://developer.spotify.com/dashboard">Spotify for Developers</a>
2. Write the "CLIENT ID" and "CLIENT SECRET" keys to the .env file.
> CLIENT_ID = yourclientid<br>
> CLIENT_SECRET = yourclientsecret

### Genius
1. After registration, create an app and get token from the link below.<br>
<a href="https://genius.com/api-clients">Genius API</a>
2. Write your token in the "GENIUS_TOKEN" section in the .env file.
> GENIUS_TOKEN = yourtoken

# requirements
1. Open the cmd.
2. cd <project_path>
3. Enter the:
```
pip install -r requirements.txt
```
# Info
1. This application was made with python language.
2. Tkinter was used as GUI.
3. googletrans, lyricsgenius, pyperclip, spotipy libraries were used.

