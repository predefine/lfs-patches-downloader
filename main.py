"""LFS Patches Downloader"""
from functions import remove_directory, download_recursive

OUT_DIR = "out"
DOWNLOAD_URL = "https://linuxfromscratch.org/patches/downloads/"

remove_directory(OUT_DIR)
download_recursive(DOWNLOAD_URL, OUT_DIR)
