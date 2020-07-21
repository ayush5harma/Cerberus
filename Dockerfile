FROM elytra8/alpineapple:latest

RUN mkdir /TESLA && chmod 777 /TESLA
ENV PATH="/One4uBot/bin:$PATH"
WORKDIR /One4uBot

RUN git clone https://github.com/ElytrA8/TESLA -b TESLA /TESLA

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /TESLA/

#
# Finalization
#
CMD ["python3","-m","userbot"]