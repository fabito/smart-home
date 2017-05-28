FROM hypriot/rpi-alpine-scratch:v3.4

RUN apk --no-cache add --update \
        mosquitto \
    && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

RUN mkdir -p /config /data && chown -R mosquitto:mosquitto /config /data

VOLUME ["/config", "/data"]

EXPOSE 1883 9001

CMD ["/usr/sbin/mosquitto", "-c", "/config/mosquitto.conf"]
