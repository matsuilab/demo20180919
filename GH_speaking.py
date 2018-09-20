def play_Mp3(google_home):
    url = r"https://soundoftext.nyc3.digitaloceanspaces.com/80b5e5a0-bcbf-11e8-b6dd-13025afb1935.mp3"
    mc = google_home.media_controller
    mc.play_media(url, "audio/mp3")
    mc.block_until_active()