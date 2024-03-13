## Script to download the latest post image from an Instagram account and copy it to the Zoom custom background folder.
## ⚠️ WARNING: This will overwrite your current custom background in Zoom. Make sure to back it up first.
##
## Author: @adoxner
## Date: March 12 2024
##
## To use:
## 1. Install instaloader: pip3 install instaloader
## 2. Run the script with the Instagram handle as an argument: python3 insta-zoom.py <instagram_handle>

import instaloader
import shutil
import os
import argparse

def copy_latest_post_to_path(username, new_path):
  # Create an instance of Instaloader
  loader = instaloader.Instaloader(quiet=True)

  # Load the profile of the given username
  print(f"(1/4) Loading profile of {username}...")
  profile = instaloader.Profile.from_username(loader.context, username)

  # Get the latest post
  print(f"(2/4) Getting the latest post of {username}...")
  posts = profile.get_posts()
  post = next(posts)  # Access the first element of the iterator

  # Download the image of the latest post
  print(f"(3/4) Downloading the image of the latest post of {username}...")
  folder_name = "tmp"
  loader.download_post(post, target=folder_name)

  # Copy the image to the new path
  print(f"(4/4) Copying the image to {new_path}...")
  image_name = f"{folder_name}/{post.date_utc}_UTC.jpg".replace(' ', '_').replace(':', '-')
  shutil.copy(image_name, new_path)

  # Delete tmp folder
  shutil.rmtree(folder_name)

def find_zoom_background_file_path():
  local_username = os.getenv('USER')
  zoom_background_folder_path = f'/Users/{local_username}/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom'

  # If there's only one file in there, we can replace it. Otherwise user needs to set it up
  files = [f for f in os.listdir(zoom_background_folder_path) if f != '.DS_Store']  
  if len(files) == 0:
    raise Exception("There are no files in the custom background folder. Add a custom background to Zoom manually first then re-run this script. WARNING: This script will overwrite the current custom background in Zoom.")
  if len(files) == 1:
    return f'{zoom_background_folder_path}/{files[0]}'
  else:
    raise Exception("There is more than one file in the VirtualBkgnd_Custom folder. Remove all but one custom background and try again. WARNING: This script will overwrite the current custom background in Zoom.")


parser = argparse.ArgumentParser(description="Set the latest Instagram post from a given account as your custom Zoom background.")
parser.add_argument('instagram_handle', type=str, help='The Instagram handle to fetch the latest post from.')
args = parser.parse_args()
instagram_handle = args.instagram_handle

zoom_background_file_path = find_zoom_background_file_path()
if zoom_background_file_path:
  copy_latest_post_to_path(instagram_handle, zoom_background_file_path)
  print(f"✅ Latest post from @{instagram_handle} set as custom Zoom background. You may need to re-select the custom background in Zoom.")
