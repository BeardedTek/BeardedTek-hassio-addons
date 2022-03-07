ARG BUILD_ARCH
# hadolint ignore=DL3006
FROM ghcr.io/hassio-addons/debian-base/${BUILD_ARCH}:5.1.0

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Setup base
# hadolint ignore=DL3003
RUN apt-get -qq update \
    && apt-get -qq install -y python3 python3-pip python-is-python3 apache2 git\
    && (apt-get autoremove -y; apt-get autoclean -y) \
    && apt-get install pip \
    && apt

# Install python dependencies
RUN pip install pytz && \
    pip install python-dateutil && \
    pip install requests && \
    pip install Pillow

# Copy root filesystem
COPY rootfs /
RUN chown -R 33:1000 /var/www \
&& chmod -R 0755 /var/www \
&& a2enmod cgid \
&& service apache2 restart
# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="The Bearded Tek <kenny@beardedtek.com>" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="BeardedTek Addons" \
    org.opencontainers.image.authors="The Bearded Tek <kenny@beardedtek.com>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.source="https://github.com/BeardedTek-com/fEVR/" \
    org.opencontainers.image.documentation="https://github.com/BeardedTek-com/fEVR/" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}
