@echo off
echo Установка зависимостей... Подожди немного.
echo.

echo Установка зависимостей из requirements.txt...
pip install -r requirements.txt

echo.
echo Все зависимости установлены!
echo Можешь закрыть окно или нажать любую клавишу для выхода.
pause >nul