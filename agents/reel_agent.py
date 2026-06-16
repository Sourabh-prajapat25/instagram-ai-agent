from moviepy import (
    ImageClip,
    AudioFileClip
)


def create_reel():

    image_path = "output/images/final_post.png"

    music_path = "assets/music/chubina.mp3"

    output_path = "output/reels/final_reel.mp4"

    # Create image clip
    clip = ImageClip(image_path)

    # Reel duration
    duration = 8

    clip = clip.with_duration(duration)

    # Slow zoom effect


    # Load music
    audio = AudioFileClip(music_path)

    audio = audio.subclipped(
        0,
        min(duration, audio.duration)
    )

    clip = clip.with_audio(audio)

    # Export
    clip.write_videofile(
        output_path,
        fps=60,
        codec="libx264",
        audio_codec="aac"
    )


    print("✅ Reel Created")
    return output_path