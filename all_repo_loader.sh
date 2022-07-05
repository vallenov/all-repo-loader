#!/usr/bin/sh

WORK_DIR=/home/vladimir/prog/python/projects/all-repo-loader

cd $WORK_DIR || echo "No directory" || exit
if [ ! -d .venv ]
then
  python -m venv .venv
fi

. .venv/bin/activate && echo activate venv

pip install -r requirements.txt

./.venv/bin/python loader.py -u $1 -p $2
