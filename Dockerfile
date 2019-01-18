FROM mayanedms/mayanedms:2.7.3

RUN pip install mayan-api_client

COPY /root /
