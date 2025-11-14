FROM ubuntu:22.04

RUN apt update -y && apt install -y curl

# Keep the container running infinitely
CMD ["sh", "-c", "while true; do echo 'Container Running...'; sleep 5; done"]
