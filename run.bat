@echo off
powershell -Command "Start-Process python -ArgumentList '\"%~dp0circle_bot.py\"' -Verb RunAs"
