FROM alpine:latest

RUN apk add python3
WORKDIR /app/my-tree
COPY . ./
CMD ["python3" "tree.py" "/app"]