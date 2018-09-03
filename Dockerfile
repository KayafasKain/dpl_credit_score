FROM python:3.5

COPY . /data/backend/
WORKDIR /data/backend/

RUN pip install -r requirements.txt --no-cache-dir
RUN chmod +x ./start.sh

EXPOSE 8000

ENTRYPOINT ["./start.sh"]