FROM python:3.8

# add user
RUN useradd -r -s /bin/bash ross

# add project
ADD . /app
RUN chown -R ross:ross /app

USER ross

# set home & current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

# set app config option
ENV CONFIG=dev

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt --user

# start wsgi server
ENTRYPOINT ["uwsgi"]
CMD ["--socket", "0.0.0.0:5000", "--protocol", "http", "-w", "wsgi:app", "--processes", "1", "--threads", "8"]
