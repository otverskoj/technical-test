#echo "Run alembic migrations"
#alembic upgrade head

echo "Run app"
uvicorn src.app:app --host 0.0.0.0 --port 8000