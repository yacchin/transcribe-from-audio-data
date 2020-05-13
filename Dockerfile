FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y ffmpeg curl

RUN curl https://sdk.cloud.google.com | bash
ENV CONFIG /root/.config/gcloud
ENV PATH /root/google-cloud-sdk/bin:$PATH

RUN mkdir -p $CONFIG

RUN mkdir /host_dir

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt

CMD bash transcribe.sh