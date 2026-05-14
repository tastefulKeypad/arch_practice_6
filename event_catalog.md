# Каталог событий пользователей
EventAddUser
- Payload: userName, userSurname, userEmail, userIsAdmin, userPassword
- Event producer: clientService
- Event consumer: userNotificationService (отправляет сообщение об успешной регистрации на почту), analyticsService(обновляет метрики и статистику зарегистрированных пользователей, например, по стране)
- Delivery guarantee: At-Least-Once

<!--
# Каталог событий автопарка
EventAddCar
- Payload: carName, carPrice, carClass, carCapacity
- Event producer: autoParkService
- Event consumer: analyticsService (обновляет метрику и статистику автомобилей в автопарке)
- Delivery guarantee: At-Least-Once
-->

# Каталог событий аренд
EventAddRent
- Payload: userId, carId, dateStart, dateEnd, status
- Event producer: rentService
- Event consumer: userNotificationService (отправляет сообщение об успешном создании аренды на почту с информацией об автомобиле), analyticsService(обновляет метрики и статистику по арендованному автомобилю)
- Delivery guarantee: At-Least-Once

EventFinalizeRent
- Payload: userId, carId, dateStart, dateEnd,
- Event producer: rentService
- Event consumer: userNotificationService (отправляет сообщение об окончании аренды на почту)
- Delivery guarantee: At-Least-Once
