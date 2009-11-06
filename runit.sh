#!/bin/sh
git pull
./post.py
git commit -m "Posted hint on $(date +%d.%m.%Y)" tip_of_the_day.txt
git push
