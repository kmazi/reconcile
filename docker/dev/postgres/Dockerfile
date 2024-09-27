FROM postgres:14.8

COPY docker/dev/postgres/init_script.sh /docker-entrypoint-initdb.d
RUN chmod +x /docker-entrypoint-initdb.d/*