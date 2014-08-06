#!/bin/bash

echo $ROOT_PATH
export PYTHONPATH=${ROOT_PATH}
${ROOT_PATH}/debian/nikola/usr/bin/nikola $@
