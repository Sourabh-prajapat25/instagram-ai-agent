from imageio_ffmpeg import get_ffmpeg_exe
import subprocess


def create_reel():

    image_path = "output/images/final_post.png"
    music_path = "assets/music/Montagem.mp3"
    grain_path = "assets/overlays/grain.mp4"

    output_path = "output/reels/final_reel.mp4"

    duration = 20
    fps = 60

    ffmpeg = get_ffmpeg_exe()

    filter_complex = (
    # Main image
    "[0:v]"
    "zoompan="
    "z='min(zoom+0.00010,1.06)':"
    "x='iw/2-(iw/zoom/2)':"
    "y='ih/2-(ih/zoom/2)':"
    f"d={duration * fps}:"
    f"s=1080x1920:fps={fps},"
    "boxblur=12:1:enable='lt(t,0.3)',"
    "fade=t=in:st=0:d=0.3"
    "[base];"

    # Grain
    "[1:v]"
    "crop=iw-50:ih:50:0,"
    "scale=1080:1920"
    "[grain];"

    # Overlay grain
    "[base][grain]"
    "blend=all_mode=softlight:all_opacity=0.90"
    "[v]"
    )

    cmd = [
        ffmpeg,
        "-y",

        # Main image
        "-loop", "1",
        "-i", image_path,

        # Grain loop
        "-stream_loop", "-1",
        "-i", grain_path,

        # Music
        "-i", music_path,

        "-filter_complex", filter_complex,

        "-map", "[v]",
        "-map", "2:a",

        "-t", str(duration),

        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",

        "-c:a", "aac",
        "-b:a", "192k",

        "-movflags", "+faststart",

        "-shortest",

        output_path
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr)
        raise Exception("FFmpeg failed")

    print("✅ Reel Created")
    return output_path
