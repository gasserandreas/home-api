from fastapi import APIRouter
from app.utils.postgres import get_db_connection
from datetime import date as _date, timedelta

router = APIRouter()

@router.get("/")
def get_all_coffee(date: _date = None):
    if date is None:
        date = _date.today()
        
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM mystrom_coffee_usage WHERE DATE(date) = %s ORDER BY date;",
            (date,)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

@router.get("/hourly")
def get_coffee_hourly(date: _date = None):
    if date is None:
        date = _date.today()
        
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM mystrom_coffee_usage_hourly WHERE DATE(date) = %s ORDER BY date;",
            (date,)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

@router.get("/daily")
def get_coffee_daily(start_date: _date = None, end_date: _date = None):
    if start_date is None:
        start_date = _date.today()
    if end_date is None:
        end_date = start_date + timedelta(days=7)
        
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM mystrom_coffee_usage_daily 
            WHERE DATE(date) >= %s 
            AND DATE(date) < %s
            ORDER BY date;
            """,
            (start_date, end_date)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

@router.get("/weekly")
def get_coffee_by_week(start_date: _date = None, end_date: _date = None):
    if start_date is None:
        # Get the start of the current month
        start_date = _date.today().replace(day=1)
    if end_date is None:
        # Get the start of next month
        if start_date.month == 12:
            end_date = _date(start_date.year + 1, 1, 1)
        else:
            end_date = _date(start_date.year, start_date.month + 1, 1)
        
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM mystrom_coffee_usage_weekly 
            WHERE week_start_date >= %s 
            AND week_end_date <= %s
            ORDER BY week_start_date;
            """,
            (start_date, end_date)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()
  
  