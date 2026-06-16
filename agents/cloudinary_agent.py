import os
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)


def upload_reel(video_path):

    result = cloudinary.uploader.upload(
        video_path,
        resource_type="video",
        folder="instagram_reels"
    )

    return result["secure_url"]
