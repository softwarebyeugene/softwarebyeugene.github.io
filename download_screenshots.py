#!/usr/bin/env python3
import urllib.request
import urllib.error
import os

# App Store screenshot URLs
screenshots = {
    'snapjigsaw_main.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/6b/1f/da/6b1fda2a-401a-94be-a1a7-a1f51cf6c1e3/screenshot1_iphone.png/643x0w.jpg',
    'snapjigsaw_gallery.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/97/10/ef/9710efc3-7088-0797-011b-7e2aefe19ba7/screenshot4_iphone.png/643x0w.jpg',
    'clevercontacts_main.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/9a/20/6c/9a206cab-d1b9-e64b-218f-7837affe819a/screenshot1.png/643x0w.jpg',
    'clevercontacts_ai.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/ff/d1/8b/ffd18b46-e9e3-9c06-b59f-f7ef754f9b4c/screenshot2.png/643x0w.jpg',
    'mapcred_main.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ee/d9/b9/eed9b931-6d06-f917-f106-a6d6d8955ef0/f7b31ae0-fb1b-415a-a853-27b5092db645_zoomout.png/643x0w.jpg',
    'mapcred_closeup.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/80/1e/91/801e91f9-5136-04d4-ca86-0051ef240159/e8ef14a2-71ac-4552-baea-38bbf45cba4a_closeup.png/643x0w.jpg',
    'cardswithphones_main.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/Purple123/v4/ca/d3/42/cad342af-4dd4-3a8e-d1f1-b7cd081093ca/mzl.pmdidlkh.png/643x0w.jpg',
    'cardswithphones_game.jpg': 'https://is1-ssl.mzstatic.com/image/thumb/Purple123/v4/f0/cb/9a/f0cb9a13-dc86-ea56-68de-6a0ddd6d518e/pr_source.png/643x0w.jpg'
}

def download_image(url, filename):
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"✓ Successfully downloaded {filename}")
        return True
    except urllib.error.URLError as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    success_count = 0
    total_count = len(screenshots)
    
    for filename, url in screenshots.items():
        if download_image(url, filename):
            success_count += 1
    
    print(f"\nDownload complete: {success_count}/{total_count} files downloaded successfully")
    
    # List downloaded files
    print("\nDownloaded files:")
    for filename in screenshots.keys():
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  {filename} ({size:,} bytes)")

if __name__ == "__main__":
    main()