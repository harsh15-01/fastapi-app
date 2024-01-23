from fastapi import FastAPI, Depends
from models import User
from database import Base, SessionLocal
# Initialize the app
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/id")
def read_user(user_id: int, db: SessionLocal = Depends(get_db)):
    user_obj = db.query(User).filter(User.id == user_id).first()
    print(user_obj.firstName)
    return user_obj

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Harsh@15",
#   database="zenarate_db"
# )
# # connection = mysql.connector.connect(**mydb)
# cursor = mydb.cursor()
#
#
# @app.get("/get_user_ids")
# def get_user_ids(user_id):
#     try:
#         query = "SELECT * FROM user where user_id = %s"
#         cursor.execute(query)
#         user_id = [result[0] for result in cursor.fetchall()]
#         return {"id": user_id}
#     finally:
#         cursor.close()
# # @app.get("/")
# # def index():
# #     return {"name":"data"}