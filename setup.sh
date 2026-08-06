#!/bin/bash
# setup.sh - Aprovisionamiento del entorno del proyecto
set -e

echo ">>> Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

echo ">>> Instalando utilidades base..."
sudo apt install -y curl git ca-certificates nano python3-venv python3-pip

echo ">>> Instalando Ollama..."
if ! command -v ollama &>/dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Ollama ya estaba instalado."
fi

echo ">>> Entorno listo."
