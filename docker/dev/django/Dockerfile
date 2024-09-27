FROM python:3.12.1

RUN groupadd -g 1000 robot \
&& useradd -m -u 1000 -g robot robot

USER robot

ENV PATH /home/robot/.local/bin:$PATH

ENV APP_HOME /app

WORKDIR $APP_HOME

ADD requirements/base.txt ./requirements/
ADD requirements/dev.txt ./requirements/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

COPY --chown=robot:robot ./docker/dev/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY . ./

EXPOSE 8000

ENTRYPOINT ["/entrypoint"]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]
