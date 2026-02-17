import os
import time
import logging
import sys
import psycopg2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,
)

logger = logging.getLogger(__name__)

def connect_to_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "secret"),
    )

logger.info("🚀 App container started")
logger.info("⏳ Trying to connect to database...")

while True:
    try:
        conn = connect_to_db()
        logger.info("✅ Database connection established")
        break
    except Exception as e:
        logger.warning(f"❌ Database not ready yet: {e}")
        time.sleep(2)

logger.info("🎉 Application is fully started and running")

while True:
    time.sleep(10)
