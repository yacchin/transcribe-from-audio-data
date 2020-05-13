# Overview
Transcription from video using Cloud Speech-to-Text. (Japanese)

# Preparation
- Create the Google Storage Bucket.

- Put the video file.
```sh
$ cd /path/to/transcribe-from-video-data
$ cp /path/to/video.mp4 ./
```

- Get the GOOGLE_APPLICATION_CREDENTIAL file from Google Cloud.
```sh
$ cp /path/to/google_application_credential.json ./
```

- Sign in to Google Cloud.
```sh
$ gcloud auth login
```

- Set environment variables.
```sh
$ cp .env.example .env
$ vi .env
```

- Build the container.
```sh
$ docker build -t [tag_name] .
```

# Transcription
```sh
$ docker run -v /path/to/output_dir:/host_dir -v ~/.config/:/root/.config/ --env-file .env -it [tag_name]
```

# Check the artifact
```sh
$ cat /path/to/output_dir/transcribed_${VOICE_FILE}.txt
```