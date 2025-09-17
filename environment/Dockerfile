# hash:sha256:17645084856fcc1b65b5a321aab589c53b5787652472d476dc0390d57bfe3d54
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/jupyterlab:3.6.1-miniconda4.12.0-python3.9-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    fastmcp \
    pandas \
    polars

COPY postInstall /
RUN --mount=type=secret,id=secrets . /run/secrets/secrets \
    && /postInstall
