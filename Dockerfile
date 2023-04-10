FROM python:2.7.18-stretch
ARG CONSUMER_KEY
ARG CONSUMER_SECRET
ARG ACCESS_KEY
ARG ACCESS_SECRET
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.sh .
COPY gameideabot ./gameideabot
RUN echo "{\"consumer_key\": \"${CONSUMER_KEY}\", \"consumer_secret\": \"${CONSUMER_SECRET}\", \"access_key\": \"${ACCESS_KEY}\", \"access_secret\": \"${ACCESS_SECRET}\"}" > gameideabot/config.json
CMD ./run.sh
