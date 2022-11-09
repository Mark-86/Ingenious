FROM python:3.9

WORKDIR /gst

COPY ./requirements.txt /gst/requirements.txt

COPY ./.env /gst/.env

# COPY ./tests /gst/test/
 
RUN pip install --no-cache-dir --upgrade -r /gst/requirements.txt

COPY ./app /gst/app/

# RUN

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["tail","-f","/dev/null"]
