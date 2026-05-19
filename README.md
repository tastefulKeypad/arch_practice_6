# Домашнее задание 06: Проектирование Event-Driven архитектуры

Цель работы: Получить навыки проектирования событийно-ориентированной архитектуры, работы с брокерами сообщений и применения паттерна CQRS.

Вариант 21: Система управления арендой автомобилей https://www.hertz.com/

# Запуск проекта
```
git clone https://github.com/tastefulKeypad/arch_practice_6.git
cd arch_practice_6
docker-compose up -d --build
```

# Полная очистка проекта
```
docker-compose down -v 
docker rmi arch_practice_6_api_image
```

# Примеры использования
После запуска на `localhost:15672` будет доступен UI RabbitMQ, логин: guest, пароль: guest

Каждые 5 секунд обновляются логи передачи событий. Чтобы их посмотреть через docker-CLI: `docker logs arch_practice_6_api`.
