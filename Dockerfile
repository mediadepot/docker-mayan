FROM mayanedms/mayanedms:latest

# install s6overlay so that we can run cron inside this container as well.
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.8.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \
    && mkdir /config

COPY /rootfs /

VOLUME ["/config"]

ENTRYPOINT ["/init"]
