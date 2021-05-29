import csv
import subprocess
from threading import Thread


class SpotifyDownloader(object):

    def __init__(self, csv_path: str, download_dest: str,
                 thread_count: int, youtube_dl_path="", additional_keywords="", audio_format="mp3"):

        # Saves settings for the class
        self.settings = {
            "cvs_path": csv_path,
            "download_dest": download_dest,
            "thread_count": thread_count,
            "youtube_dl_path": youtube_dl_path,
            "additional_keywords": additional_keywords,
            "audio_format": audio_format,
            "errors": []
        }

        # Check a threadcount larger than 0
        if self.settings["thread_count"] < 1:
            raise Exception("You need to use at least one thread")

        # Check if youtube-dl is installed with environment variables
        if self.settings["youtube_dl_path"] == "":
            self.settings["youtube_dl_path"] = "youtube-dl"

        # Raise error if something was not given
        if self.settings["cvs_path"] == "" or \
                self.settings["download_dest"] == "" or \
                self.settings["audio_format"] == "":
            raise Exception("Invalid values were entered")

        # Takes a list and returns equally big chunks of it.

    @staticmethod
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    # Calls a chunk of commands.
    @staticmethod
    def start_thread_with_chunk(self, chunk, error_list):
        for command in chunk:
            try:
                subprocess.run(command)

            except Exception as e:
                error_list.append(f"Command: {command} | Error: {e}")

    def get_settings(self):
        return self.settings

    # Starts the download process.
    def start(self):
        print("Starting download...")
        self.distribute_download_tasks(self.get_download_commands())
        print("Download finished.")

    # Takes the csv file and extracts the name and Artist from every song, which is returned with a list of touples.
    def get_song_artist_and_name(self):
        with open(self.settings["cvs_path"], encoding='cp850', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            list_song_info = []
            for row in csv_reader:
                list_song_info.append((row["Track Name"], row["Artist Name(s)"]))
            return list_song_info

    # Generates Youtube-DL commands from the csv file.
    def get_download_commands(self):
        command_list = []
        song_list = self.get_song_artist_and_name()
        for song in song_list:
            command_list.append(
                [
                    self.settings["youtube_dl_path"],
                    "-x",
                    "--audio-format",
                    self.settings["audio_format"],
                    "-o",
                    "{download_dest}{filename}.%(ext)s".format(download_dest=self.settings["download_dest"],
                                                                   filename=(song[0] + " - " + song[1])
                                                                   .replace("/", " ")
                                                                   .replace("\\", " ")),
                    "ytsearch1: {song0} {song1} {additional_keywords}".format(song0=song[0],
                                                                                  song1=song[1],
                                                                                  additional_keywords=
                                                                                  self.settings["additional_keywords"])
                ]
            )

        return command_list

    # Takes a commandlist, generated by getDownloadCommands() and distributes them over the given amount of threads.
    def distribute_download_tasks(self, command_list):
        command_chunks = self.chunks(command_list, int(round(len(command_list) / self.settings["thread_count"], 0)))
        thread_list = []

        for commands in command_chunks:
            thread_list.append(Thread(target=self.start_thread_with_chunk, args=(commands, self.settings["errors"],)))

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

        if len(self.settings["errors"]) > 0:
            print("Some errors occured. error.txt was created in the local directory.")
            with open("./error.txt", "a") as log_file:
                for error in self.settings["errors"]:
                    log_file.write(f"{error}\n")


if __name__ == '__main__':
    print("Welcome to this script!")
    SD = SpotifyDownloader(
        input("Please enter the path to the downloaded csv file:"),
        input("Enter a path, where the music should be saved:"),
        int(input("Enter the amount of threads you want to use (number):")),
        input("Please enter the path to the 'youtube-dl.exe':"),
        input("Add additional keywords that should be added to the Youtube search:")
    )

    SD.start()
