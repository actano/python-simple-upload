FROM python:3.4
ADD . /code/
WORKDIR /code
RUN pip install -r requirements.txt
ENV PORT 9090
ENV TARGET /tmp
CMD python upload.py --port=$PORT --target=$TARGET
