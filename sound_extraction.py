
import moviepy.editor
import re
import sys

USAGE="usage: [mediafile]"
HELP = f"{USAGE}\nThis script takes one argument:\nmediafile: the name of the movie that that we need to extract sound from"

if len(sys.argv) > 1 and re.match(r"^(help|h|usage)$", sys.argv[1]) != None:
	print(HELP)
	exit()

if len(sys.argv) < 2:
	print(f"[ERROR] {USAGE}")
	exit()

media_filename=sys.argv[1]
if re.match(r".*\.(mov|mp4|avi)$", media_filename) == None:
	print("[ERROR] file extension not accepted")
	exit()

media_filename_without_extension = re.sub("\\..*", "", media_filename)
video = moviepy.editor.VideoFileClip(media_filename)
video.audio.write_audiofile(f"{media_filename_without_extension}.wav")

print("Audio extracted.")