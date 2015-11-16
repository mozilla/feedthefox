#!/bin/sh

./bin/run-common.sh

# Update revision.txt with latest HEAD
echo $(git rev-parse HEAD) > static/revision.txt

gunicorn feedthefox.wsgi:application -b 0.0.0.0:${PORT:-8000} --log-file -
