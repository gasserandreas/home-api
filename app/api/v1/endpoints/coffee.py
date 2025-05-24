from fastapi import APIRouter
from app.models.coffee import CoffeeModel
from app.utils.postgres import get_db_connection

router = APIRouter()

@router.get("/")
def get_all_coffee():
    obj = { "message": "Hello World" }
    return obj
    # conn = get_db_connection()
    # cur = conn.cursor()
    # try:
    #     cur.execute("SELECT * FROM coffee")
    #     result = cur.fetchall()
    #     return result
    # finally:
    #     cur.close()
    #     conn.close() 