import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import yt_dlp
import threading
import os
import subprocess

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return

    downloading_label.config(text="Downloading...")
    download_button.config(state=tk.DISABLED)

    def download():
        try:
            desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
            youtube_videos_folder = os.path.join(desktop_folder, "Youtube Videos")
            
            if not os.path.exists(youtube_videos_folder):
                os.makedirs(youtube_videos_folder)

            outtmpl = os.path.join(youtube_videos_folder, '%(title)s.%(ext)s')

            with yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': outtmpl}) as ydl:
                ydl.download([url])

            downloading_label.config(text="Download complete!")

            
            subprocess.run(f'explorer "{youtube_videos_folder}"')

        except Exception as e:
            downloading_label.config(text="Error occurred.")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            download_button.config(state=tk.NORMAL)
            root.after(2000, lambda: downloading_label.config(text=""))

    threading.Thread(target=download, daemon=True).start()

root = tk.Tk()
root.title("Ovi's Video Downloader")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

try:
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(root, image=logo, bg="#1e1e1e")
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo not found:", e)

title_label = tk.Label(root, text="YouTube/Instagram Video Downloader", font=("Arial", 18, "bold"), fg="#ff5733", bg="#1e1e1e")
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter the video URL to download:", font=("Arial", 12), fg="#ffffff", bg="#1e1e1e")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50, font=("Arial", 12), relief="solid", bd=2)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download", font=("Arial", 12), bg="#4CAF50", fg="white", command=download_video)
download_button.pack(pady=20)

downloading_label = tk.Label(root, text="", font=("Arial", 12), fg="yellow", bg="#1e1e1e")
downloading_label.pack(pady=10)

root.mainloop()
