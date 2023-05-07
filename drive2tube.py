#! /bin/env python

import json, sys, os, collections, itertools
from pathlib import Path
from time import sleep
from youtube_video_upload.upload_video import upload_video
from youtube_video_upload.get_credentials import get_credentials

# consts
CLIENT_SECRET_JSON = "client_secret.json"
VIDEOS_DIR = "vids"

# get the credentials store ready
with open(CLIENT_SECRET_JSON, 'r') as f:
    yt_creds = get_credentials(json.load(f))

# init the videos dir 
vids_dir = Path(os.getcwd() + "/" + VIDEOS_DIR)
vids = itertools.chain(vids_dir.rglob("*.mp4"), vids_dir.rglob("*.mkv"))

# to avoid later episodes are uploaded but not previous ones are failed due to 
# API rate limiting or any other errors
vids = sorted(vids) 

# upload 
for v in vids:
    fname = str(v)
    print("processing: " + fname)
    basename = fname.split('.')[0]

    try:
        url = upload_video(
            yt_creds, 
            fname, 
            title=basename,
            description=basename,
            privacy="private",
            category="27"
        )
        print(url)
    except:
        print("error @ " + fname)

