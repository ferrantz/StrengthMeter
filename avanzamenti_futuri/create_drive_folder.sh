#!/bin/bash

if [ -z "$1" ]; then
  echo "Uso: $0 <nome_cartella>"
  exit 1
fi

python3 create_folder.py "$1"
