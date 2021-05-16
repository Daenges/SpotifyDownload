from GUI_SpotifyDownloader import GUI
from SpotifyDownloader import SpotifyDownloader

if __name__ == "__main__":
    if input("Do you want to start the GUI? (Y/n) > ").lower() == "n":
        print("Starting command prompt")
        print("Welcome to this script!")
        sd = SpotifyDownloader(
            input("Please enter the path to the downloaded csv file:"),
            input("Enter a path, where the music should be saved:"),
            int(input("Enter the amount of threads you want to use (number):")),
            input("Please enter the path to the 'youtube-dl.exe':"),
            input("Add additional keywords that should be added to the Youtube search:")
        )
        sd.Start()
    else:
        print("Starting GUI")
        g = GUI()
