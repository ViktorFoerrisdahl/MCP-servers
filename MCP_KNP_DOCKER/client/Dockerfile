# Import python
FROM python:3

# The /app directory should act as the main application directory
WORKDIR /server

COPY ./src/client ./src

#install uv
RUN python -m pip install --no-cache-dir uv

# Instal dependendsies based on uv installs and saves them for future use
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-install-project

COPY ./src/client ./src
ENV PATH="/server/.venv/bin:$PATH"

# start server
CMD ["python", "src/server.py"]
