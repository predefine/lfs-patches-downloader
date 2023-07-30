"""BLFS Stable Patches Downloader"""
from functions import remove_directory, download_recursive

OUT_DIR = "out-blfs-stable"
DOWNLOAD_URL = "https://mirror.linuxfromscratch.ru/blfs/downloads/stable/patches/"

remove_directory(OUT_DIR)
download_recursive(DOWNLOAD_URL, OUT_DIR)
