FROM python:3.14.7-slim

WORKDIR /workspace

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    git \
    curl \
    wget \
    tree \
    htop \
    build-essential \
    ca-certificates \
    sudo \
    tk \
    && rm -rf /var/lib/apt/lists/*

# Requirements
COPY .devcontainer/requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt

# Crear usuario vscode
RUN useradd -m -s /bin/bash vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# RUN chown -R vscode:vscode /workspace

USER vscode

# Instalar OpenCode para vscode
RUN curl -fsSL https://opencode.ai/install | bash \
    && /home/vscode/.opencode/bin/opencode --version

ENV PATH="/home/vscode/.opencode/bin:${PATH}"

CMD ["bash"]
