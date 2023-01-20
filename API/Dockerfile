# For more information, please refer to https://aka.ms/vscode-docker-python

FROM python:3-alpine3.11
EXPOSE 9001
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
#ENV AWS_ACCESS_KEY_ID=AKIA5TEEY4RPPQ4HD46H                                                                                                127 ✘  bin   13:58:48
#ENV AWS_SECRET_ACCESS_KEY=1NYMUizrYOQiz4gJF3ytZNW284u3bQTi4W/8p86Q
#ENV AWS_DEFAULT_REGION=eu-west-2


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD python ./application.py

