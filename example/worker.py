import os
from pathlib import Path

from seeds import Seed

BASE_DIR = Path(__file__).resolve().parent

app = Seed(
    scripts_path=BASE_DIR / "seeds", database_url=os.getenv("DATABASE_URL")
)
