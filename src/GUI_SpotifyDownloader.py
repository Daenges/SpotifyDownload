import csv
import threading
import time
import tkinter as tk
import tkinter.messagebox as mb
import webbrowser
from tkinter import filedialog, END
from tkinter.ttk import Progressbar

from SpotifyDownloader import SpotifyDownloader


class GUI(object):

    def __init__(self, window_size="750x400", resizable_x=False, resizable_y=False):
        # Initialize GUI settings
        self.GUI_settings = {
            "window_size": window_size,
            "resizable_x": resizable_x,
            "resizable_y": resizable_y
        }

        # Create Window
        self.root_window = tk.Tk()

        # Get SpotifyDownloader object
        self.spotify_downloader = None

        # gray background
        self.root_window["background"] = '#42576B'

        # check if downloadsettings are open
        self.downloadsettings_open = False

        # Adjust window settings
        self.root_window.title("Spotify Downloader")
        self.root_window.geometry(self.GUI_settings["window_size"])
        self.root_window.resizable(self.GUI_settings["resizable_x"], self.GUI_settings["resizable_y"])
        self.root_window.iconbitmap("./ressources/SpotifyDownload_icon.ico")

        # Create Listbox
        self.listbox = tk.Listbox(self.root_window)
        self.listbox["background"] = "#7A8997"
        self.listbox.place(x=20, y=20, width=350, height=360)
        scrollbar = tk.Scrollbar(self.root_window, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="left", fill="y")

        # Update the main window
        self.root_window.update()

        # Create Download button
        photo = tk.PhotoImage(file=r"./ressources/SpotifyDownload_256.png").subsample(4, 4)
        button_start_download = tk.Button(self.root_window, text="Download", command=self.open_download_settings,
                                          image=photo)
        button_start_download["background"] = "#7A8997"
        button_start_download.place(x=self.root_window.winfo_width() - 80, y=self.root_window.winfo_height() - 80,
                                    width=65, height=65)

        # Create Dialogue csv path button
        button_open_dialogue_csv = tk.Button(self.root_window, text="Open", command=self.open_dialogue_csv)
        button_open_dialogue_csv.config(bg="lightgray")
        button_open_dialogue_csv.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=50,
                                       width=70, height=20)

        # Create dialogue youtube-dl button
        button_open_dialogue_yt_dl = tk.Button(self.root_window, text="Open", command=self.open_dialogue_yt_dl)
        button_open_dialogue_yt_dl.config(bg="lightgray")
        button_open_dialogue_yt_dl.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=100,
                                         width=70, height=20)

        # Create dialogue save download
        button_open_dialogue_save = tk.Button(self.root_window, text="Location", command=self.open_save_dialogue)
        button_open_dialogue_save.config(bg="lightgray")
        button_open_dialogue_save.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=150,
                                        width=70, height=20)

        # Update the main window
        self.root_window.update()

        # Open Youtube-DL site
        button_open_browser_yt_dl = tk.Button(self.root_window, text="⤴", command=self.open_browser_yt_dl)
        button_open_browser_yt_dl.config(bg="lightgray")
        button_open_browser_yt_dl.place(x=button_open_dialogue_yt_dl.winfo_x() + 80,
                                        y=button_open_dialogue_yt_dl.winfo_y(),
                                        width=20, height=20)

        # Open Exportify site
        button_open_browser_exportify = tk.Button(self.root_window, text="⤴", command=self.open_browser_exportify)
        button_open_browser_exportify.config(bg="lightgray")
        button_open_browser_exportify.place(x=button_open_dialogue_csv.winfo_x() + 80,
                                            y=button_open_dialogue_csv.winfo_y(),
                                            width=20, height=20)

        # Update the main window
        self.root_window.update()

        # Directory textbox
        self.textbox_csv_path = tk.Text(self.root_window)
        self.textbox_csv_path["background"] = "#7A8997"
        self.textbox_csv_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=button_open_dialogue_csv.winfo_y(),
                                    width=180, height=20)

        # Directory textbox
        self.textbox_yt_dl_path = tk.Text(self.root_window)
        self.textbox_yt_dl_path["background"] = "#7A8997"
        self.textbox_yt_dl_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=button_open_browser_yt_dl.winfo_y(),
                                      width=180, height=20)

        # Directory textbox
        self.textbox_download_dest = tk.Text(self.root_window)
        self.textbox_download_dest["background"] = "#7A8997"
        self.textbox_download_dest.place(x=button_open_dialogue_save.winfo_x() - 200,
                                         y=button_open_dialogue_save.winfo_y(),
                                         width=180, height=20)

        # Update the main window
        self.root_window.update()

        # Label over textbox csv
        label_csv_path = tk.Label(self.root_window, text="Path of the csv file:")
        label_csv_path["background"] = '#42576B'
        label_csv_path.place(x=self.textbox_csv_path.winfo_x(), y=self.textbox_csv_path.winfo_y() - 25)

        # Label over textbox Youtube-DL
        label_youtube_dl_path = tk.Label(self.root_window, text="Path of the Youtube-DL file:")
        label_youtube_dl_path["background"] = '#42576B'
        label_youtube_dl_path.place(x=self.textbox_yt_dl_path.winfo_x(), y=self.textbox_yt_dl_path.winfo_y() - 25)

        # Label over textbox Location
        label_download_dest = tk.Label(self.root_window, text="Destination for the music:")
        label_download_dest["background"] = '#42576B'
        label_download_dest.place(x=self.textbox_download_dest.winfo_x(), y=self.textbox_download_dest.winfo_y() - 25)

        # Start mainloop
        self.root_window.mainloop()

    @staticmethod
    def open_browser_yt_dl():
        webbrowser.open_new_tab("https://youtube-dl.org/")

    @staticmethod
    def open_browser_exportify():
        webbrowser.open_new_tab("https://watsonbox.github.io/exportify/")

    def open_download_settings(self):
        # Initialize window
        self.settings_window = tk.Toplevel(self.root_window)  # Create on top of main window
        self.settings_window.geometry("300x250" + "+{}+{}".format(self.root_window.winfo_x() +
                                                                  self.root_window.winfo_width() // 2 - 150,
                                                                  self.root_window.winfo_y()))
        self.settings_window.title("Configure Download")
        self.settings_window.iconbitmap("./ressources/SpotifyDownload_icon.ico")
        self.settings_window["background"] = '#42576B'
        self.settings_window.resizable(False, False)
        self.settings_window.focus_force()

        settings = ["thread_count",
                    "additional_keywords",
                    "audio_format"]

        option_list = ['aac', 'best', 'flac', 'm4a', 'mp3', 'opus', 'vorbis', 'wav']

        for num, setting in enumerate(settings):
            self.settings_window.update()
            temp = tk.Label(self.settings_window, text=setting)
            temp["background"] = '#42576B'
            temp.place(x=20,
                       y=40 * num + 20,
                       width=130, height=15)

        # Create Textbox for Threadcount
        self.textbox_threadcount = tk.Text(self.settings_window)
        self.textbox_threadcount["background"] = "#7A8997"
        self.textbox_threadcount.place(x=160,
                                       y=20,
                                       width=100, height=20)
        self.textbox_threadcount.insert("1.0", "5")

        # Create Textbox for additional keywords
        self.textbox_additionaly_keywords = tk.Text(self.settings_window)
        self.textbox_additionaly_keywords["background"] = "#7A8997"
        self.textbox_additionaly_keywords.place(x=160,
                                                y=60,
                                                width=100, height=20)

        # Create Textbox for audioformat
        self.drop_down_menu_entry = tk.StringVar(self.settings_window)
        self.drop_down_menu_entry.set(option_list[0])

        self.drop_down_menu = tk.OptionMenu(self.settings_window, self.drop_down_menu_entry, *option_list)
        self.drop_down_menu["background"] = "#7A8997"
        self.drop_down_menu.place(x=160,
                                  y=100,
                                  width=100, height=20)

        # Create button to start download
        self.button_start_download = tk.Button(self.settings_window, text="Start Download",
                                               command=self.start_download_instance)
        self.button_start_download.config(bg="lightgray")
        self.button_start_download.place(x=self.settings_window.winfo_width() // 2 - 50,
                                         y=self.settings_window.winfo_height() - 30,
                                         width=100, height=20)

        # Restrict user action on new window to prevent creating several of it.
        self.settings_window.transient(self.root_window)
        self.settings_window.grab_set()
        self.root_window.wait_window(self.settings_window)

    def start_download_instance(self):
        # Try to initialize download object through user given parameters
        try:
            sd = SpotifyDownloader(csv_path=str(self.textbox_csv_path.get(1.0, END)).replace("\n", ""),
                                   download_dest=str(self.textbox_download_dest.get(1.0, END)).replace("\n", ""),
                                   thread_count=int(self.textbox_threadcount.get(5.0, END)),
                                   youtube_dl_path=str(self.textbox_yt_dl_path.get(1.0, END)).replace("\n", ""),
                                   additional_keywords=str(self.textbox_additionaly_keywords.get(1.0, END))
                                   .replace("\n", "") + " ",
                                   audio_format=self.drop_down_menu_entry.get()
                                   )

            # Close the settings window
            self.settings_window.destroy()

            self.pb_main = Progressbar(self.root_window, length='200', mode="indeterminate",
                                       orient=tk.HORIZONTAL)
            self.pb_main.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 20,
                               y=self.root_window.winfo_height() - 80)
            self.pb_main.start(5)

            # Uptdate the root window
            self.root_window.update()

            # Download label
            self.label_downloading = tk.Label(text="Downloading")
            self.label_downloading["background"] = '#42576B'
            self.label_downloading.place(x=self.pb_main.winfo_x(), y=self.pb_main.winfo_y() + 30)

            # Create thread to handle the work to avoid locking the main program
            self.work_thread = threading.Thread(target=sd.start, args=())
            self.work_thread.daemon = True
            self.work_thread.start()

            # Temp thread to cancel the progressbar
            temp_thread = threading.Thread(target=self.check_thread_work, args=())
            temp_thread.daemon = True
            temp_thread.start()

        # Message the user if something went wrong
        except Exception as e:
            tk.messagebox.showerror(title="Download Wizard", message="Error: " + str(e))

    def open_save_dialogue(self):
        # Clear Box
        self.textbox_download_dest.delete('1.0', END)
        # Insert path from dialogue
        self.textbox_download_dest.insert('1.0', tk.filedialog.askdirectory() + "/")

    def check_thread_work(self):
        while self.work_thread.is_alive():
            time.sleep(1)

        self.pb_main.place_forget()
        self.label_downloading.place_forget()

    def open_dialogue_yt_dl(self):
        # Clear Box
        self.textbox_yt_dl_path.delete('1.0', END)
        # Insert path from dialogue
        self.textbox_yt_dl_path.insert('1.0', filedialog.askopenfilename(initialdir="/",
                                                                         title="Select the Youtube-Dl file"))

    def open_dialogue_csv(self):
        # Clear Box
        self.textbox_csv_path.delete('1.0', END)
        # Insert path from dialogue
        self.textbox_csv_path.insert('1.0', filedialog.askopenfilename(initialdir="/", title="Select a CSV File",
                                                                       filetypes=(
                                                                           ("Text files", "*.csv*"),
                                                                           ("all files", "*.*"))))

        try:
            # Open the file and extract its contents. Add them to the listbox
            with open(str(self.textbox_csv_path.get(1.0, END)).replace("\n", ""), encoding='cp850',
                      mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.listbox.insert(END, "{} || Artist: {}".format(row["Track Name"], row["Artist Name(s)"]))

        # Message the user if something went wrong
        except Exception as e:
            self.textbox_csv_path.delete('1.0', END)
            tk.messagebox.showerror(title="File Wizard", message="Invalid file: " + str(e))


if __name__ == "__main__":
    g = GUI()
