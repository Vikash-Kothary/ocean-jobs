#!/bin/bash
# file: clear-outputs.sh
# description: Clear outputs from jupyter notebooks.

find notebooks -name  "*.ipynb" -print0 | xargs -0 nbstripout