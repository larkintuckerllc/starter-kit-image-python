FROM tiangolo/meinheld-gunicorn-flask:python3.8
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app /app
EXPOSE 8080
USER 1000:1000
ENV PORT=8080
