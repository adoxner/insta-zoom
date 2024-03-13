# insta-zoom
Script to download the latest post image from an Instagram account and copy it to the Zoom custom background folder.

> [!CAUTION]
> This will overwrite your current custom background in Zoom. Make sure to back it up first.

## How to use
1. Install instaloader dependency: `pip3 install instaloader`
2. Run the script with the Instagram handle as an argument: `python3 insta-zoom.py <instagram_handle>`

## Pitfalls
For this script to work, you need exactly one custom background set. *It will be overwritten by this script.* If you have more than one custom background, you must delete the others. If you don't have a custom background, you must manually add one (that will be overwritten) first.
