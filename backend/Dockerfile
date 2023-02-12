FROM python:3.10

RUN pip install poetry

COPY ./poetry* ./pyproject.toml ./README.md /app/
COPY ./homework_fullstack/ /app/homework_fullstack/

WORKDIR /app
RUN poetry install --no-interaction --no-root

ENV ORIGINS "*"
ENV DATA_DIR "/data"

COPY ./scripts/start.sh /app/
EXPOSE 8080
CMD ["/app/start.sh"]
