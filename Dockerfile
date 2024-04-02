FROM python:3.12-slim-bullseye as libs

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends git gcc openssh-client libc6-dev \
    && update-ca-certificates

COPY requirements.txt .
RUN --mount=type=ssh pip install -r requirements.txt

FROM python:3.12-slim-bullseye

EXPOSE 5060
RUN useradd -d /app -u 1122 app \
    && mkdir -p /app/logs/core \
    && chown app: /app/logs/core \
    && apt-get -y update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=libs /usr/local /usr/local
COPY . .

USER app

CMD ["bash", "entrypoint.sh"]
