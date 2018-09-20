import pychromecast
import HC_SR04
import GH_speaking
import GSS_writing
import time

def main():
    # Beforehand connected to Google Home
    chromecasts = pychromecast.get_chromecasts()
    google_home = chromecasts[0]

    while True:
        dist = HC_SR04.measure(0)
        print("distance :", dist)
        if dist <= 50:
            GH_speaking.play_Mp3(google_home)
            time.sleep(3.0)
            GSS_writing.writeGoogleSpreadSheet()

if __name__ == "__main__":
    main()