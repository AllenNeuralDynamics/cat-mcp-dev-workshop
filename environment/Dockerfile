# hash:sha256:7a058687abd3242b35adb36ee10d229fe5087e0fac5e9df8f409c2145c81c876
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:24.5.0-0-python3.12.4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    fastmcp==2.12.3 \
    pandas==2.3.2 \
    polars==1.33.1

COPY postInstall /
RUN --mount=type=secret,id=secrets . /run/secrets/secrets \
    && /postInstall
