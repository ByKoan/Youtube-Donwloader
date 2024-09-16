import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
import yt_dlp

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Crear un Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de Descarga de Videos
        self.download_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.download_tab, text="Download Video")

        # Crear contenido de la pestaña de descarga de video
        self.create_download_tab()

        # Pestaña de Descarga de Audio
        self.audio_download_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.audio_download_tab, text="Download Audio")

        # Crear contenido de la pestaña de descarga de audio
        self.create_audio_download_tab()

        # Pestaña de Información del Creador
        self.creator_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.creator_tab, text="Creator Info")

        # Crear contenido de la pestaña de información del creador
        self.create_creator_tab()

    def create_download_tab(self):
        # Frame principal para la pestaña de descarga de video
        main_frame = ttk.Frame(self.download_tab, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de URL
        url_label = ttk.Label(main_frame, text="Enter YouTube video URL:")
        url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.url_entry = ttk.Entry(main_frame, width=70)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # Botón de obtener información
        info_button = ttk.Button(main_frame, text="Get Video Info", command=self.get_video_info)
        info_button.grid(row=1, column=0, pady=20)

        # Etiqueta de selección de calidad
        quality_label = ttk.Label(main_frame, text="Select video quality:")
        quality_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        # Combobox para seleccionar la calidad
        self.quality_combobox = ttk.Combobox(main_frame, state="readonly")
        self.quality_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta de selección de formato
        format_label = ttk.Label(main_frame, text="Select video format:")
        format_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Combobox para seleccionar el formato
        self.format_combobox = ttk.Combobox(main_frame, state="readonly")
        self.format_combobox.grid(row=3, column=1, padx=10, pady=10)

        # Botón para obtener subtítulos disponibles
        get_subtitles_button = ttk.Button(main_frame, text="Get Available Subtitles", command=self.get_available_subtitles)
        get_subtitles_button.grid(row=4, column=0, pady=20)

        # Combobox para seleccionar subtítulos
        self.subtitle_combobox = ttk.Combobox(main_frame, state="readonly")
        self.subtitle_combobox.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

        # Botón para seleccionar la ruta de descarga
        download_path_label = ttk.Label(main_frame, text="Select download path:")
        download_path_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        self.download_path_entry = ttk.Entry(main_frame, width=70)
        self.download_path_entry.grid(row=5, column=1, padx=10, pady=10)

        browse_button = ttk.Button(main_frame, text="Browse", command=self.browse_download_path)
        browse_button.grid(row=5, column=2, padx=10, pady=10)

        # Botón de descarga
        download_button = ttk.Button(main_frame, text="Download", command=self.download_video)
        download_button.grid(row=6, column=0, pady=20)

        # Área de mensajes
        self.message_text = tk.Text(main_frame, height=15, width=100)
        self.message_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)

        # Scrollbar para el área de mensajes
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.message_text.yview)
        scrollbar.grid(row=7, column=3, sticky=tk.NS)
        self.message_text.config(yscrollcommand=scrollbar.set)

    def create_audio_download_tab(self):
        # Frame principal para la pestaña de descarga de audio
        main_frame = ttk.Frame(self.audio_download_tab, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de URL
        url_label = ttk.Label(main_frame, text="Enter YouTube video URL:")
        url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.audio_url_entry = ttk.Entry(main_frame, width=70)
        self.audio_url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # Botón de obtener información
        info_button = ttk.Button(main_frame, text="Get Audio Info", command=self.get_audio_info)
        info_button.grid(row=1, column=0, pady=20)

        # Etiqueta de selección de calidad
        quality_label = ttk.Label(main_frame, text="Select audio quality:")
        quality_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        # Combobox para seleccionar la calidad
        self.audio_quality_combobox = ttk.Combobox(main_frame, state="readonly")
        self.audio_quality_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta de selección de formato
        format_label = ttk.Label(main_frame, text="Select audio format:")
        format_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Combobox para seleccionar el formato
        self.audio_format_combobox = ttk.Combobox(main_frame, state="readonly", values=["mp3", "m4a", "aac", "opus", "flac", "wav", "webm"])
        self.audio_format_combobox.grid(row=3, column=1, padx=10, pady=10)

        # Botón para seleccionar la ruta de descarga
        download_path_label = ttk.Label(main_frame, text="Select download path:")
        download_path_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.audio_download_path_entry = ttk.Entry(main_frame, width=70)
        self.audio_download_path_entry.grid(row=4, column=1, padx=10, pady=10)

        browse_button = ttk.Button(main_frame, text="Browse", command=self.browse_audio_download_path)
        browse_button.grid(row=4, column=2, padx=10, pady=10)

        # Botón de descarga
        download_button = ttk.Button(main_frame, text="Download", command=self.download_audio)
        download_button.grid(row=5, column=0, pady=20)

        # Área de mensajes
        self.audio_message_text = tk.Text(main_frame, height=15, width=100)
        self.audio_message_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)

        # Scrollbar para el área de mensajes
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.audio_message_text.yview)
        scrollbar.grid(row=6, column=3, sticky=tk.NS)
        self.audio_message_text.config(yscrollcommand=scrollbar.set)

    def browse_download_path(self):
        download_path = filedialog.askdirectory()
        if download_path:
            self.download_path_entry.delete(0, tk.END)
            self.download_path_entry.insert(0, download_path)

    def browse_audio_download_path(self):
        download_path = filedialog.askdirectory()
        if download_path:
            self.audio_download_path_entry.delete(0, tk.END)
            self.audio_download_path_entry.insert(0, download_path)

    def get_video_info(self):
        url = self.url_entry.get().strip()
        if url:
            self.message_text.config(state=tk.NORMAL)
            self.message_text.delete(1.0, tk.END)
            self.message_text.insert(tk.END, "Getting video information from {}\n".format(url))
            self.message_text.config(state=tk.DISABLED)

            ydl_opts = {
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info_dict = ydl.extract_info(url, download=False)
                    formats = info_dict.get('formats', [])
                    available_qualities = [f['format_note'] for f in formats if f.get('format_note')]
                    available_formats = list(set(f['ext'] for f in formats if f.get('ext')))
                    
                    self.quality_combobox['values'] = available_qualities
                    self.format_combobox['values'] = available_formats
                    
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "Available qualities: {}\n".format(", ".join(available_qualities)))
                    self.message_text.insert(tk.END, "Available formats: {}\n".format(", ".join(available_formats)))
                    self.message_text.config(state=tk.DISABLED)
                except yt_dlp.DownloadError as e:
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "Error: {}\n".format(str(e)))
                    self.message_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL.")

    def get_audio_info(self):
        url = self.audio_url_entry.get().strip()
        if url:
            self.audio_message_text.config(state=tk.NORMAL)
            self.audio_message_text.delete(1.0, tk.END)
            self.audio_message_text.insert(tk.END, "Getting audio information from {}\n".format(url))
            self.audio_message_text.config(state=tk.DISABLED)

            ydl_opts = {
                'format': 'bestaudio/best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info_dict = ydl.extract_info(url, download=False)
                    formats = info_dict.get('formats', [])
                    available_qualities = [f['abr'] for f in formats if f.get('abr')]
                    available_formats = list(set(f['ext'] for f in formats if f.get('ext') in ['mp3', 'm4a', 'aac', 'opus', 'flac', 'wav', 'webm']))
                    
                    self.audio_quality_combobox['values'] = available_qualities
                    self.audio_format_combobox['values'] = available_formats
                    
                    self.audio_message_text.config(state=tk.NORMAL)
                    self.audio_message_text.insert(tk.END, "Available qualities: {}\n".format(", ".join(map(str, available_qualities))))
                    self.audio_message_text.insert(tk.END, "Available formats: {}\n".format(", ".join(available_formats)))
                    self.audio_message_text.config(state=tk.DISABLED)
                except yt_dlp.DownloadError as e:
                    self.audio_message_text.config(state=tk.NORMAL)
                    self.audio_message_text.insert(tk.END, "Error: {}\n".format(str(e)))
                    self.audio_message_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL.")

    def get_available_subtitles(self):
        url = self.url_entry.get().strip()
        if url:
            self.message_text.config(state=tk.NORMAL)
            self.message_text.delete(1.0, tk.END)
            self.message_text.insert(tk.END, "Getting available subtitles from {}\n".format(url))
            self.message_text.config(state=tk.DISABLED)

            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info_dict = ydl.extract_info(url, download=False)
                    subtitles = info_dict.get('subtitles', {})
                    available_subtitles = [lang for lang in subtitles.keys()]

                    self.subtitle_combobox['values'] = ["all"] + available_subtitles
                    
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "Available subtitles: {}\n".format(", ".join(available_subtitles)))
                    self.message_text.config(state=tk.DISABLED)
                except yt_dlp.DownloadError as e:
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "Error: {}\n".format(str(e)))
                    self.message_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL.")

    def download_video(self):
        url = self.url_entry.get().strip()
        quality = self.quality_combobox.get()
        format = self.format_combobox.get()
        download_path = self.download_path_entry.get().strip()
        selected_subtitles = self.subtitle_combobox.get()

        if url and quality and format and download_path:
            self.message_text.config(state=tk.NORMAL)
            self.message_text.delete(1.0, tk.END)
            self.message_text.insert(tk.END, "Downloading video from {} with quality {} and format {}\n".format(url, quality, format))
            self.message_text.config(state=tk.DISABLED)

            ydl_opts = {
                'format': f'bestvideo[height<=1080]+bestaudio/best',
                'outtmpl': download_path + '/%(title)s.%(ext)s',
                'merge_output_format': format,
            }

            if selected_subtitles:
                ydl_opts['subtitlesformat'] = 'srt'
                ydl_opts['writesubtitles'] = True
                ydl_opts['subtitleslangs'] = [selected_subtitles] if selected_subtitles != "all" else []

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([url])
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "Download completed\n")
                    self.message_text.config(state=tk.DISABLED)
                except yt_dlp.DownloadError as e:
                    self.message_text.config(state=tk.NORMAL)
                    self.message_text.insert(tk.END, "DownloadError: {}\n".format(str(e)))
                    self.message_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL, select a quality, select a format, and choose a download path.")

    def download_audio(self):
        url = self.audio_url_entry.get().strip()
        quality = self.audio_quality_combobox.get()
        format = self.audio_format_combobox.get()
        download_path = self.audio_download_path_entry.get().strip()

        if url and quality and format and download_path:
            self.audio_message_text.config(state=tk.NORMAL)
            self.audio_message_text.delete(1.0, tk.END)
            self.audio_message_text.insert(tk.END, "Downloading audio from {} with quality {} and format {}\n".format(url, quality, format))
            self.audio_message_text.config(state=tk.DISABLED)

            ydl_opts = {
                'format': f'bestaudio[abr={quality}]/bestaudio',
                'outtmpl': download_path + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': format,
                    'preferredquality': '192',  # Puedes ajustar la calidad aquí
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([url])
                    self.audio_message_text.config(state=tk.NORMAL)
                    self.audio_message_text.insert(tk.END, "Download completed\n")
                    self.audio_message_text.config(state=tk.DISABLED)
                except yt_dlp.DownloadError as e:
                    self.audio_message_text.config(state=tk.NORMAL)
                    self.audio_message_text.insert(tk.END, "DownloadError: {}\n".format(str(e)))
                    self.audio_message_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL, select a quality, select a format, and choose a download path.")

    def create_creator_tab(self):
        main_frame = ttk.Frame(self.creator_tab, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        creator_name_label = ttk.Label(main_frame, text="Creator: Koan")
        creator_name_label.pack(pady=10)

        creator_description_label = ttk.Label(main_frame, text="Junior Dev Learning Python & C.")
        creator_description_label.pack(pady=10)

        github_button = ttk.Button(main_frame, text="GitHub Profile", command=lambda: webbrowser.open("https://github.com/bykoan"))
        github_button.pack(pady=10)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    app.run()
