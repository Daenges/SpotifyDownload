from SpotifyDownloader import SpotifyDownload
import os
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import filedialog, END


class GUI(object):

    def __init__(self, window_size="700x400", resizable_x=False, resizable_y=False):
        # Initialize GUI settings
        self.GUI_settings = {
            "window_size": window_size,
            "resizable_x": resizable_x,
            "resizable_y": resizable_y
        }

        # Get SpotifyDownloader object
        self.spotify_downloader = None

        # Create Window
        self.root_window = tk.Tk()

        # Adjust window settings
        self.root_window.title("Spotify Downloader")
        self.root_window.geometry(self.GUI_settings["window_size"])
        self.root_window.resizable(self.GUI_settings["resizable_x"], self.GUI_settings["resizable_y"])

        # Update the main window
        self.root_window.update()

        # Create Download button
        button_start_download = tk.Button(self.root_window, text="Download", command=self.new_download_instance)
        button_start_download.place(x=self.root_window.winfo_width() - 100, y=self.root_window.winfo_height() - 50,
                                    width=70, height=30)

        # Create Dialogue CVS path button
        button_open_dialogue_csv = tk.Button(self.root_window, text="Open", command=self.open_dialogue_csv)
        button_open_dialogue_csv.place(x=self.root_window.winfo_width() - 100, y=50,
                                       width=70, height=20)

        # Create dialogue youtube-dl button
        button_open_dialogue_yt_dl = tk.Button(self.root_window, text="Open", command=self.open_dialogue_yt_dl)
        button_open_dialogue_yt_dl.place(x=self.root_window.winfo_width() - 100, y=100,
                                         width=70, height=20)

        # Update the main window
        self.root_window.update()

        # Directory textbox
        self.textbox_cvs_path = tk.Text(self.root_window)
        self.textbox_cvs_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=50,
                                    width=180, height=20)

        # Directory textbox
        self.textbox_yt_dl_path = tk.Text(self.root_window)
        self.textbox_yt_dl_path.place(x=button_open_dialogue_csv.winfo_x() - 200, y=100,
                                      width=180, height=20)

        # Update the main window
        self.root_window.update()

        # Label over textbox
        self.label_cvs_path = tk.Label(self.root_window, text="Path of the CVS file:")
        self.label_cvs_path.place(x=self.textbox_cvs_path.winfo_x(), y=self.textbox_cvs_path.winfo_y() - 25)

        # Label over textbox
        self.label_cvs_path = tk.Label(self.root_window, text="Path of the Youtube-DL file:")
        self.label_cvs_path.place(x=self.textbox_yt_dl_path.winfo_x(), y=self.textbox_yt_dl_path.winfo_y() - 25)

        # Create Listbox
        self.listbox = tk.Listbox(self.root_window)
        self.listbox.place(x=10, y=10, width=300, height=200)

        # Start mainloop
        self.root_window.mainloop()

    def new_download_instance(self):
        settings_window = tk.Tk()
        settings_window.geometry("300x250")
        settings_window.title("Configure Download")
        label_list = []
        textbox_list = []
        settings = ["download_dest",
                    "thread_count",
                    "youtube_dl_path",
                    "additional_keywords",
                    "audio_format"]

        for num, setting in enumerate(settings):
            settings_window.update()
            label_list.append(tk.Label(settings_window, text=setting).place(x=20,
                                                                            y=40 * num + 20,
                                                                            width=130, height=15))
            textbox_list.append(tk.Text(settings_window).place(x=160,
                                                               y=40 * num + 20,
                                                               width=100, height=20))

        settings_window.mainloop()

    def open_dialogue_yt_dl(self):
        yt_dl_path = self.textbox_yt_dl_path.get(1.0, "end-1c")
        if yt_dl_path == "":
            self.textbox_yt_dl_path.insert('1.0', filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                                             filetypes=(
                                                                                 ("Text files", "*.txt*"),
                                                                                 ("all files", "*.*"))))

    def open_dialogue_csv(self):
        csv_path = self.textbox_cvs_path.get(1.0, "end-1c")
        if csv_path == "":
            self.textbox_cvs_path.insert('1.0', filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                                           filetypes=(
                                                                               ("Text files", "*.txt*"),
                                                                               ("all files", "*.*"))))
            # todo fill listbox with entries
        else:
            if os.path.isfile(csv_path):
                # todo fill listbox with entries
                pass
            else:
                tk.messagebox.showwarning("File Wizard", "Your files shall not pass!")

    def start_download(self):
        mb.showinfo("Du bist ein", "Esel!!!")


g = GUI()
