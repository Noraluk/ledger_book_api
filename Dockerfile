# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y fakeroot ffmpeg libsm6 libxext6 &&     mv /usr/bin/apt-get /usr/bin/.apt-get &&     echo '#!/usr/bin/env sh\nfakeroot /usr/bin/.apt-get $@' > /usr/bin/apt-get &&     chmod +x /usr/bin/apt-get && 	rm -rf /var/lib/apt/lists/* && 	useradd -m -u 1000 user

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# COPY --from=pipfreeze --link --chown=1000 /tmp/freeze.txt /tmp/freeze.txt
COPY . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]