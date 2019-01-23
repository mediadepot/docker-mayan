FROM mayanedms/mayanedms:latest

#RUN pip install mayan-api_client

COPY /root /

# change mayan userid
RUN usermod -u 15000 mayan && \
    groupmod -g 15000 mayan
