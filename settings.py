"""
Base configuration setup
"""
import os


CONFIG = {
    "DB": {
        "drivername": "postgres",
        "host": os.environ.get("DATABASE_HOST", "localhost"),
        "port": int(os.environ.get("DATABASE_PORT", 5432)),
        "username": os.environ.get("DATABASE_USERNAME", ""),
        "password": os.environ.get("DATABASE_PASSWORD", ""),
        "database": os.environ.get("DATABASE_NAME", ""),
    }
}
