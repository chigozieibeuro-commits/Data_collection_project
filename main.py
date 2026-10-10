from fastapi import  FastAPI
from database import  connection
from schema import Register

app=FastAPI()

@app.get("/get")
def get():
    return {
        'message':"registration fastapi running "


    }

@app.post('/')
def records(data:Register):
    con=connection()
    cursor=con.cursor()


    query="""" INSERT INTO students(first_name,second_name,mail,
    age,department,address,next_of_kin,next_of_kin_phone)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    RETURNING_id;
    """

    cursor.execute(
        query,(
            data.first_name,data.second_name,data.mail,data.age,data.department,data.address,data.next_of_kin,
            data.next_of_kin_phone
        )
    )
    student_id=cursor.fetchon()

    con.commit()
    cursor.close()
    con.close()


    return {
        "message":"successful",
        'student_id':student_id
    }