import csv
import threading
import tkinter as tk
import tkinter.messagebox as mb
import webbrowser
from tkinter import filedialog, END
from tkinter.ttk import Progressbar

from SpotifyDownloader import SpotifyDownload


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

        # check if downloadsettings are open
        self.downloadsettings_open = False

        # Adjust window settings
        self.root_window.title("Spotify Downloader")
        self.root_window.geometry(self.GUI_settings["window_size"])
        self.root_window.resizable(self.GUI_settings["resizable_x"], self.GUI_settings["resizable_y"])
        self.root_window.iconbitmap("./ressources/SpotifyDownload_icon.ico")

        # Create Listbox
        self.listbox = tk.Listbox(self.root_window)
        self.listbox.place(x=20, y=20, width=350, height=360)
        scrollbar = tk.Scrollbar(self.root_window, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")

        # Update the main window
        self.root_window.update()

        # Create Download button
        photo = tk.PhotoImage(file=r"./ressources/SpotifyDownload_256.png").subsample(4, 4)
        button_start_download = tk.Button(self.root_window, text="Download", command=self.open_download_settings,
                                          image=photo)
        button_start_download.place(x=self.root_window.winfo_width() - 80, y=self.root_window.winfo_height() - 70,
                                    width=65, height=65)

        # Create Dialogue csv path button
        button_open_dialogue_csv = tk.Button(self.root_window, text="Open", command=self.open_dialogue_csv)
        button_open_dialogue_csv.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=50,
                                       width=70, height=20)

        # Create dialogue youtube-dl button
        button_open_dialogue_yt_dl = tk.Button(self.root_window, text="Open", command=self.open_dialogue_yt_dl)
        button_open_dialogue_yt_dl.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=100,
                                         width=70, height=20)

        # Create dialogue save download
        button_open_dialogue_save = tk.Button(self.root_window, text="Location", command=self.open_save_dialogue)
        button_open_dialogue_save.place(x=self.listbox.winfo_x() + self.listbox.winfo_width() + 250, y=150,
                                        width=70, height=20)

        # Update the main window
        self.root_window.update()

        # Open Youtube-DL site
        button_open_browser_yt_dl = tk.Button(self.root_window, text="⤴", command=self.open_browser_yt_dl)
        button_open_browser_yt_dl.place(x=button_open_dialogue_yt_dl.winfo_x() + 80,
                                        y=button_open_dialogue_yt_dl.winfo_y(),
                                        width=20, height=20)

        # Open Exportify site
        button_open_browser_exportify = tk.Button(self.root_window, text="⤴", command=self.open_browser_exportify)
        button_open_browser_exportify.place(x=button_open_dialogue_csv.winfo_x() + 80,
                                            y=button_open_dialogue_csv.winfo_y(),
                                            width=20, height=20)

        # Update the main window
        self.root_window.update()

        # Directory textbox
        self.textbox_csv_path = tk.Text(self.root_window)
        self.textbox_csv_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=button_open_dialogue_csv.winfo_y(),
                                    width=180, height=20)

        # Directory textbox
        self.textbox_yt_dl_path = tk.Text(self.root_window)
        self.textbox_yt_dl_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=button_open_browser_yt_dl.winfo_y(),
                                      width=180, height=20)

        # Directory textbox
        self.textbox_download_dest = tk.Text(self.root_window)
        self.textbox_download_dest.place(x=button_open_dialogue_save.winfo_x() - 200,
                                         y=button_open_dialogue_save.winfo_y(),
                                         width=180, height=20)

        # Update the main window
        self.root_window.update()

        # Label over textbox csv
        label_csv_path = tk.Label(self.root_window, text="Path of the csv file:")
        label_csv_path.place(x=self.textbox_csv_path.winfo_x(), y=self.textbox_csv_path.winfo_y() - 25)

        # Label over textbox Youtube-DL
        label_csv_path = tk.Label(self.root_window, text="Path of the Youtube-DL file:")
        label_csv_path.place(x=self.textbox_yt_dl_path.winfo_x(), y=self.textbox_yt_dl_path.winfo_y() - 25)

        # Label over textbox Location
        label_download_dest = tk.Label(self.root_window, text="Destination for the music:")
        label_download_dest.place(x=self.textbox_download_dest.winfo_x(), y=self.textbox_download_dest.winfo_y() - 25)

        # Start mainloop
        self.root_window.mainloop()

    def open_browser_yt_dl(self):
        webbrowser.open_new_tab("https://youtube-dl.org/")

    def open_browser_exportify(self):
        webbrowser.open_new_tab("https://watsonbox.github.io/exportify/")

    def open_download_settings(self):
        # Initialize window
        self.settings_window = tk.Tk()
        self.settings_window.geometry("300x250")
        self.settings_window.title("Configure Download")
        self.settings_window.iconbitmap("./ressources/SpotifyDownload_icon.ico")
        self.settings_window.resizable(False, False)

        settings = ["thread_count",
                    "additional_keywords",
                    "audio_format"]

        for num, setting in enumerate(settings):
            self.settings_window.update()
            tk.Label(self.settings_window, text=setting).place(x=20,
                                                               y=40 * num + 20,
                                                               width=130, height=15)

        self.textbox_threadcount = tk.Text(self.settings_window)
        self.textbox_threadcount.place(x=160,
                                       y=20,
                                       width=100, height=20)
        self.textbox_threadcount.insert("1.0", "1")

        self.textbox_additionaly_keywords = tk.Text(self.settings_window)
        self.textbox_additionaly_keywords.place(x=160,
                                                y=60,
                                                width=100, height=20)
        self.textbox_additionaly_keywords.insert("1.0", " ")

        self.textbox_audioformat = tk.Text(self.settings_window)
        self.textbox_audioformat.place(x=160,
                                       y=100,
                                       width=100, height=20)
        self.textbox_audioformat.insert("1.0", "mp3")

        self.button_start_download = tk.Button(self.settings_window, text="Start Download",
                                               command=self.start_download_instance)
        self.button_start_download.place(x=self.settings_window.winfo_width() // 2 - 50,
                                         y=self.settings_window.winfo_height() - 30,
                                         width=100, height=20)

        self.settings_window.mainloop()

    def start_download_instance(self):
        try:
            sd = SpotifyDownload(csv_path=str(self.textbox_csv_path.get(1.0, END)).replace("\n", ""),
                                 download_dest=str(self.textbox_download_dest.get(1.0, END)).replace("\n", ""),
                                 thread_count=int(self.textbox_threadcount.get(1.0, END)),
                                 youtube_dl_path=str(self.textbox_yt_dl_path.get(1.0, END)).replace("\n", ""),
                                 additional_keywords=str(self.textbox_additionaly_keywords.get(1.0, END)).replace("\n", ""),
                                 audio_format=str(self.textbox_audioformat.get(1.0, END)).replace("\n", "")
                                 )

            pb = Progressbar(self.settings_window, length='200', mode="indeterminate",
                             orient=tk.HORIZONTAL)
            pb.place(x=self.button_start_download.winfo_x() // 2, y=self.button_start_download.winfo_y() - 30)
            pb.start(5)

            self.work_thread = threading.Thread(target=sd.Start, args=())
            self.work_thread.daemon = True
            self.work_thread.start()

        except Exception as e:
            tk.messagebox.showerror(title="Download Wizard", message="Error: " + str(e))

    def open_save_dialogue(self):
        # Clear Box
        self.textbox_download_dest.delete('1.0', END)
        # Insert path from dialogue
        self.textbox_download_dest.insert('1.0', tk.filedialog.askdirectory() + "/")

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
            with open(str(self.textbox_csv_path.get(1.0, END)).replace("\n", ""), encoding='cp850', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.listbox.insert(END, "{} {}".format(row["Track Name"], row["Artist Name(s)"]))
        except Exception as e:
            self.textbox_csv_path.delete('1.0', END)
            tk.messagebox.showerror(title="File Wizard", message="Invalid file: " + str(e))


g = GUI()
