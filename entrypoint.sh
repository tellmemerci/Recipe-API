   #!/bin/bash
   set -e

   # Выполнить миграции
   python manage.py migrate

   # Выполнить команду, переданную в контейнер
   exec "$@"
