FROM ubuntu:22.04

RUN apt update -y && apt install -y curl

CMD ["echo", "Docker image build successful!"]
