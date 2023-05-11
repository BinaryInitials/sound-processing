#!/bin/bash

tic=$(date +%s)
project_name=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(json.load(sys.stdin)['project_name'])")
echo "Starting workflow for ${project_name}"

echo "1. Sound extraction from media file"
media_filename=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(json.load(sys.stdin)['media_filename'])")
python3 sound_extraction.py $media_filename

echo "2. Sound fragmentation from sound file extracted"
filename_without_extension=$(echo $media_filename | perl -pe 's/\.[^.]+$//g')
wav_filename="${filename_without_extension}.wav"

number_of_fragments=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(len(json.load(sys.stdin)['data']))" | awk '{print $1-1}')
for i in $(seq 0 $number_of_fragments); do 
	name_of_fragment=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(json.load(sys.stdin)['data'][${i}]['fragment_name'])")
	start_time=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(json.load(sys.stdin)['data'][${i}]['start_time'])")
	end_time=$(cat config.json  | perl -pe 's/\n//g' | python3 -c "import sys, json; print(json.load(sys.stdin)['data'][${i}]['end_time'])")
	python3 sound_fragmentation.py $wav_filename $start_time $end_time
	echo "2.${i}. Starting sound processing from fragment"
	python3 sound_processing.py "${filename_without_extension}_fragment_${start_time}-${end_time}.wav"
done
toc=$(date +%s)
dt=$(echo $toc $tic | awk '{print $1-$2}')
echo "dt=${dt} seconds"
