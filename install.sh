@echo off
echo Установка зависимостей...
python3 -m pip install --upgrade pip
pip install -r requirements.txt
read -p "Нажми Enter, чтобы выйти..."