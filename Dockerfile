# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.11

RUN apt-get update && apt-get install -y fakeroot &&     mv /usr/bin/apt-get /usr/bin/.apt-get &&     echo '#!/usr/bin/env sh\nfakeroot /usr/bin/.apt-get $@' > /usr/bin/apt-get &&     chmod +x /usr/bin/apt-get && 	rm -rf /var/lib/apt/lists/* && 	useradd -m -u 1000 user

COPY --chown=1000:1000 --from=root / /

WORKDIR /home/user/app

RUN apt-get update && apt-get install -y 	git 	git-lfs 	ffmpeg 	libsm6 	libxext6 	cmake 	rsync 	libgl1-mesa-glx 	&& rm -rf /var/lib/apt/lists/* 	&& git lfs install

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --link --chown=1000 ./ /home/user/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
