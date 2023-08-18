FROM python:3.6.1-alpine
RUN pip install --upgrade pip
RUN pip install flask
CMD ["python","main1.py"]
COPY main1.py /main1.py
