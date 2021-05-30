@echo off	
title StartUp
color 2
start cmd /k call minefc.bat
start cmd /k call ngrok.bat
timeout /t 40 /nobreak
start cmd /k call DiscordBot.bat
start cmd /k call DiscordBot_update.bat
start cmd /k call DiscordBot_Create_voice.bat
start cmd /k call DiscordBot_Delete_voice.bat
echo Done!