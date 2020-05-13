# -*- coding: utf-8 -*-

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io


def long_running_recognize(gs_path):
    """
    Transcribe a long audio file using asynchronous speech recognition
    Args:
      gs_path Path to google strage audio file path, e.g. gs://bucket_name/audio.wav
    """

    client = speech_v1.SpeechClient()

    language_code = "ja-JP"

    sample_rate_hertz = 16000

    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }

    audio = {"uri": gs_path}

    operation = client.long_running_recognize(config, audio)

    response = operation.result()

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"Transcript: {}\n".format(alternative.transcript))


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--gs_path", type=str)
    args = parser.parse_args()

    long_running_recognize(args.gs_path)


if __name__ == "__main__":
    main()
