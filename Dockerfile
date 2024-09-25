# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.11-slim

# RUN useradd -m -u 1000 user
# USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

RUN  apt update && apt install -y ffmpeg libsm6 libxext6

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
