# Overview
Transcription from video using Cloud Speech-to-Text.

# Preparation
- Prepare the video data. (ex: mp4)
- Create the Google Storage Bucket.
- Get the GOOGLE_APPLICATION_CREDENTIAL file from GCP.

# Transcription
```sh
$ cd /path/to/transcribe-from-video-data

$ cp /path/to/video.mp4 ./

$ cp /path/to/google_application_credential.json ./

$ gcloud auth login

$ cp .env.example .env
$ vi .env

$ docker build -t [tag_name] .

$ docker run -v /path/to/output_dir:/host_dir -v ~/.config/:/root/.config/ --env-file .env -it [tag_name]
```
