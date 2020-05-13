#!/bin/bash

GS_PATH="gs://${GS_BUCKET}/${VOICE_FILE}"

ffmpeg -i ./${MOVIE_FILE} ./${VOICE_FILE}

gsutil cp ./${VOICE_FILE} gs://${GS_BUCKET}/

python3 transcribe.py --gs_path ${GS_PATH} > /host_dir/transcribed_${VOICE_FILE}.txt
