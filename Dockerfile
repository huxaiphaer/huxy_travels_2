FROM python:3.7

RUN mkdir app

COPY . /app/

WORKDIR /app

RUN chmod +x entrypoint.sh


# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5005

CMD ["bash", "entrypoint.sh"]