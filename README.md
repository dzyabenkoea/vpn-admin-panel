## Запуск

Запускаем базу 
```
docker compose up -d
```


Выполняем миграции
```
alembic upgrade head
```

Стартуем бекенд
```
uvicorn src.main:app
```