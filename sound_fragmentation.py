import re
import sys
import wave

USAGE="usage: [soundfile][start_time][end_time]"
HELP = f"{USAGE}\nThis script takes 3 arguments:\nsoundfile: the name of the wav file that needs to be fragmented\nstart_time: The time in seconds were the fragment should start\nend_time: The time in seconds when the fragment should end"
if len(sys.argv) > 1 and re.match(r"^(help|h|usage)$", sys.argv[1]) != None:
	print(HELP)
	exit()

if len(sys.argv) < 4:
	print(f"[ERROR] {USAGE}")
	exit()

media_filename=sys.argv[1]
media_filename_without_extension = re.sub("\\..*", "", media_filename)
if re.match(r".*\.(wav)$", media_filename) == None:
	print("[ERROR] file extension not accepted")
	exit()
start_time_arg=sys.argv[2]
if re.match(r"[0-9]+(\\.[0-9]+)?$", start_time_arg) == None:
	print("[ERROR] invalid start time format. Please ensure the start time is a value in seconds. e.g. 4.23")
	exit()
start_time=float(start_time_arg)

end_time_arg=sys.argv[3]
if re.match(r"[0-9]+(\\.[0-9]+)?$", end_time_arg) == None:
	print("[ERROR] invalid end time format. Please ensure the end time is a value in seconds. e.g. 10.59")
	exit()
end_time=float(end_time_arg)

if end_time < start_time:
	print("[ERROR] end time should happen AFTER start time. Please make sure start time is smaller than end time")
	exit()

wave_file = wave.open(media_filename,'r')
print(f"Number of channels: {wave_file.getnchannels()}")
print(f"Sample width: {wave_file.getsampwidth()}")
print(f"Frame rate: {wave_file.getframerate()}")
print(f"Number of frames: {wave_file.getnframes()}")
print(f"parameters: {wave_file.getparams()}")

frame_rate = wave_file.getframerate()
start_frame = int(start_time*frame_rate);
end_frame = int(end_time*frame_rate);
wave_file.setpos(start_frame)
frames = wave_file.readframes(end_frame-start_frame)

wave_file_fragment = wave.open(f"{media_filename_without_extension}_fragment_{int(start_time)}-{int(end_time)}.wav", "w")
wave_file_fragment.setnchannels(wave_file.getnchannels())
wave_file_fragment.setsampwidth(wave_file.getsampwidth())
wave_file_fragment.setframerate(wave_file.getframerate())
wave_file_fragment.writeframesraw(frames)
wave_file.close()
wave_file_fragment.close()
print("Fragment of file written")