"""LFS Patches Downloader"""
import os
import urllib.request

import requests
from bs4 import BeautifulSoup

files = []


def download_recursive(url: str, out_dir: str, download_after=True):
    """Download recursive"""
    if not out_dir.endswith("/"):
        out_dir += "/"
    try:
        os.listdir(out_dir)
    except FileNotFoundError:
        os.makedirs(out_dir)

    data = requests.get(url, timeout=25)

    if data.status_code != 200:
        print(f"error when requesting {url}, skip and continue")
        return
    soup = BeautifulSoup(data.text, "html.parser")
    for link in soup.find_all("a")[1:]:
        href = link.get("href")
        next_url: str = url+href
        new_out_dir = out_dir+href
        if next_url.endswith("/"):
            download_recursive(next_url, new_out_dir, False)
        else:
            print(f"New file: {next_url}")
            files.append([next_url, new_out_dir])

    if download_after:
        total_files = len(files)
        print(f"Count of files: {total_files}")
        for index, data in enumerate(files):
            print(
                f"{index+1}/{total_files} | Downloading {data[0]} to {data[1]}"
            )
            urllib.request.urlretrieve(*data)


download_recursive("https://linuxfromscratch.org/patches/downloads/", "out")
