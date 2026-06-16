import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
IG_USER_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")


def publish_reel(video_url, caption):

    # STEP 1: Create Media Container
    container_url = f"https://graph.facebook.com/v23.0/{IG_USER_ID}/media"

    payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(container_url, data=payload)
    response_json = response.json()

    print("Container Response:")
    print(response_json)

    if "id" not in response_json:
        print("❌ Failed to create media container")
        return

    creation_id = response_json["id"]

    # STEP 2: Wait for Instagram Processing
    print("\n⏳ Waiting for Instagram to process reel...\n")

    status_url = f"https://graph.facebook.com/v23.0/{creation_id}"

    for _ in range(20):

        status_response = requests.get(
            status_url,
            params={
                "fields": "status_code",
                "access_token": ACCESS_TOKEN
            }
        )

        status_json = status_response.json()

        print(status_json)

        status = status_json.get("status_code")

        if status == "FINISHED":
            print("\n✅ Reel processing complete\n")
            break

        elif status == "ERROR":
            print("❌ Instagram processing failed")
            return

        time.sleep(15)

    else:
        print("❌ Timeout waiting for Instagram processing")
        return

    # STEP 3: Publish Reel
    publish_url = f"https://graph.facebook.com/v23.0/{IG_USER_ID}/media_publish"

    publish_payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN
    }

    publish_response = requests.post(
        publish_url,
        data=publish_payload
    )

    publish_json = publish_response.json()

    print("\nPublish Response:")
    print(publish_json)

    if "id" in publish_json:
        print("\n🎉 Reel Published Successfully!")
    else:
        print("\n❌ Reel Publish Failed")