# SpotifyDownload

Download your Spotify playlist from Youtube through Youtube-DL.

## Disclaimer
Technically speaking, this program is only an automation tool for [Youtube-DL](https://youtube-dl.org/).<br />
Therefore, all rules concidering the download of copyright affected content can be applied here.
___
## Requirements:
[FFMPEG](https://ffmpeg.org/) to convert videos into other formats. (As [Environment Variable](https://windowsloop.com/add-environment-variable-in-windows-10/) in Windows 10) <br />
[Youtube-DL](https://youtube-dl.org/) to download videos. <br />
[Exportify](https://watsonbox.github.io/exportify/) to download your playlist in a .csv format. <br />

## Instructions

**Open [start.py](https://github.com/Daenges/SpotifyDownload/blob/main/src/start.py) and choose whether to start with a GUI:**

### Commandline
- Start [SpotifyDownloader.py](https://github.com/Daenges/SpotifyDownload/blob/main/src/SpotifyDownloader.py)
- Answer the questions:
- Please enter the path to the downloaded csv file: ```[location of the downloaded file]```
- Enter a path, where the music should be saved: ```[path where the music should be saved]```
- Enter the amount of threads you want to use: ```[Number of threads that should be used]```
- Please enter the path to the 'youtube-dl.exe': ```[Path to Youtube-DL]```
- Add additional keywords that should be added to the Youtube search: ```[e.g. 'lyrics' which improves search results]```

![SD_Commandline_screenshot](https://user-images.githubusercontent.com/57369924/118376340-c5685300-b5c7-11eb-9fa4-87e3c0e98385.png)

---
### GUI

- Start [GUI_SpotifyDownloader.py](https://github.com/Daenges/SpotifyDownload/blob/main/src/GUI_SpotifyDownloader.py):
- Enter the path of everything in the textboxes or open a dialogue with the button. (1)
- [Optional] Click on the arrows to open the downloadpage for the [CSV](https://watsonbox.github.io/exportify/) or [Youtube-DL](https://youtube-dl.org/) file. (2)
- If you did it correctly, you should see results in (3).
- Press the download button. (4)
- Leave standard settings, or change them in the appearing window. (Settings explained in Commandline)
- Start download by pressing the button. (5)

![GUI_start](https://user-images.githubusercontent.com/57369924/118376384-f052a700-b5c7-11eb-8a6f-8377eab960a4.png)
![Download_settings](https://user-images.githubusercontent.com/57369924/118376363-d9ac5000-b5c7-11eb-9885-e66a8ce73f34.png)
