#!/bin/bash

set -e

echo "🔧 Instalando dependencias base..."
sudo pacman -S --noconfirm --needed base-devel openssl zlib xz git

echo "🚀 Instalando pyenv..."
curl https://pyenv.run | bash

echo "📌 Agregando pyenv a tu shell..."
SHELL_RC="$HOME/.bashrc"
if [[ $SHELL == *zsh ]]; then
  SHELL_RC="$HOME/.zshrc"
fi

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> "$SHELL_RC"
echo 'eval "$(pyenv init -)"' >> "$SHELL_RC"
echo 'eval "$(pyenv virtualenv-init -)"' >> "$SHELL_RC"

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

echo "🐍 Instalando Python 3.11.9 con pyenv..."
pyenv install 3.11.9 || true  # Evita error si ya está instalado

echo "🌐 Creando entorno virtual 'venv' con Python 3.11.9..."
cd "$(dirname "$0")"
pyenv local 3.11.9
python -m venv venv

echo "✅ Entorno virtual creado en ./venv"
echo "ℹ️ Usa: source venv/bin/activate"
