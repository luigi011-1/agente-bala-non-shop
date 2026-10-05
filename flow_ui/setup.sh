#!/usr/bin/env bash
# Instalacao unica: bash flow_ui/setup.sh
set -e
python3 -m pip install --upgrade playwright
python3 -m playwright install chromium
echo "Pronto. Proximo passo: python3 flow_ui/flow_ui.py login"
