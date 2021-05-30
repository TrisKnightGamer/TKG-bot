@echo off
title Backup Bot
color 2
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
git init
git remote add bot https://github.com/TrisKnightGamer/TKG-bot.git
git lfs track '*'
git add .
git rm .env --cached
git commit -m "%mydate%:%mytime%"
git lfs push --all bot master
git push -f bot master
echo BACKUP DONE!
PAUSE