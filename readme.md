## Youtube Downloader

----

This youtube downloader use ffmpeg (you need to download it from its website - https://www.ffmpeg.org and put the binary file on the environment variables) and ``YT_DLP`` python library ``YT_DLP`` have updates, if the program failed maybe it will be fixed if you update the library.

You can download videos in all qualities and all formats and audio same as video **(ADDED DOWNLOAD PLAYLIST (MUST BE PUBLIC))**

> To use it, run **"install.bat"** on 'Windows' or **"install.sh"** 
If you wanna compile it for have a compiled file just run the **"compile.bat"** file (you need to have tkinter pyinstaller)

You can install everything you need with the following command:
```bash
pip install -r requirements.txt
```

If you wanna compile the program just run this two commands:
```bash
pip install pyinstaller
pyinstaller --name YouTubeDownloader --onefile --windowed main.py
```
----
