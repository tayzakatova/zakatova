ls ~/.ssh - проверка наличия ключей
ssh-keygen -t ed25519 -C "taisiyazakatovaaa" - создание нового ключа(пары)
cat ~/.ssh/id_ed25519.pub - вывести значение ключа на экран
eval "$(ssh-agent -s)" - для запуска ssh-agent
shh-add ~/.ssh/id_ed25519 - добавление ключа в агента
добавить публичный ключ в свой гит в настройках
shh -T git@github.com - проверка на правильность

