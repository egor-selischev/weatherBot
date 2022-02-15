FROM python:latest
COPY . .
RUN pip install -r ./requirements.txt --no-cache-dir
RUN chmod +x wbot.py
CMD python wbot.py