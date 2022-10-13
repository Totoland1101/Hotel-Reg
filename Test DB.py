
def register():
    #getting form data
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    gen1=gender.get()
    city1=city.get()
    state1=state.get()
    #applying empty validation
    if name1=='' or con1==''or email1=='' or gen1==''or city1==''or state1=='':
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO REG(NAME, CONTACT, EMAIL, GENDER, CITY, STATE)"
           "VALUES (%s, %s, %s, %s, %s, %s)"
       )
       if gen1==1:
        data = (name1, con1,email1,"Male",city1,state1)
       else:
        data = (name1, con1, email1, "Female", city1, state1)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Stored successfully")

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global  message;
    global name
    global contact
    global email
    global gender
    global city
    global state
    name = StringVar()
    contact = StringVar()
    email=StringVar()
    gender=IntVar()
    city=StringVar()
    state=StringVar()
    message=StringVar()