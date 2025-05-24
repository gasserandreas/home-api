from fastapi import APIRouter
from app.utils.postgres import get_db_connection
from datetime import date as _date

router = APIRouter()

@router.get("/")
def get_all_coffee(date: _date = None):
    if date is None:
        date = _date.today()
        
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM mystrom_coffee_report WHERE DATE(created_at) = %s ORDER BY created_at;",
            (date,)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close() 