#!/bin/bash
# file: clear-outputs.sh
# description: Clear outputs from jupyter notebooks.

find notebooks -name  "*.ipynb" -not -path "*.ipynb_checkpoints/*" -print0 | xargs -0 nbstripout