from agents.content_agent import generate_content
from agents.post_creator import create_post
from agents.reel_agent import create_reel
from agents.cloudinary_agent import upload_reel
from publisher import publish_reel


print("Generating new content...")
content = generate_content()


create_post()
create_reel()


video_url = upload_reel(
    "output/reels/final_reel.mp4"
)

publish_reel(
    video_url,
    content["caption"]
)

print("Pipeline Finished")