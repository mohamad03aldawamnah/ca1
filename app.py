from flask import Flask, render_template, session, redirect, url_for, g, request 
from database import get_db, close_db 
from flask_session import Session 
from werkzeug.security import generate_password_hash, check_password_hash 
from forms import RegistrationForm, LoginForm ,allergiesForm
from functools import wraps  
app = Flask (__name__) 
app.teardown_appcontext (close_db) 
app.config ["SECRET_KEY"] = "mo-the-bro" 
app.config ["SESSION_PERMANENT"] = False 
app.config ["SESSION_TYPE"] = "filesystem" 
Session(app) 





 
@app.before_request 
def logged_in_user(): 
    g.user = session.get("user_id", None) 

def login_required(view): 
    @wraps (view) 
    def wrapped_view(*args, **kwargs): 
        if g.user is None:  
            return redirect(url_for("login", next=request.url)) 
        return view(*args, **kwargs) 
    return wrapped_view 


@app.route("/")
def index(): 
    return render_template("index.html")  





@app.route("/main_menue")
def main_menue():
    db=get_db()
    main_menue = db.execute("""SELECT *
                            FROM meals;""").fetchall()
    return render_template("lunch.html",main_menue = main_menue)





@app.route("/register", methods=["GET", "POST"]) 
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit(): 
        user_id= form.user_id.data 
        password = form.password.data 
        password2 = form.password2.data 
        db = get_db() 
        possible_clashing_user = db.execute("""SELECT * FROM users 
                                            WHERE user_id = ?;""", (user_id,)).fetchone() 
        if possible_clashing_user is not None: 
            form.user_id.errors.append("User id already taken!") 
        else: 
            db.execute("""INSERT INTO users (user_id, password) 
                        VALUES (?, ?);""" ,(user_id, generate_password_hash(password)))
            db.commit() 
            return redirect(url_for("login")) 
    return render_template("register.html", form=form) 

@app.route("/login", methods=["GET", "POST"])
def login(): 
    form = LoginForm() 
    if form.validate_on_submit(): 
        user_id=form.user_id.data 
        password = form.password.data 
        db = get_db() 
        possible_clashing_user= db.execute("""SELECT * FROM users WHERE user_id = ?;""", (user_id,)).fetchone() 
        if possible_clashing_user is None: 
            form.user_id.errors.append("No such user!") 
        
        elif not check_password_hash (possible_clashing_user["password"],password):
            form.password.errors.append("incorrectpassword!")
        else:  
            session.clear() 
            session ["user_id"] = user_id 
            next_page= request.args.get("next") 
            if not next_page: 
                next_page = url_for("index") 
            return redirect (next_page) 
    return render_template("login.html", form=form) 

@app.route("/Logout") 
 
def logout(): 
    session.clear() 
    return redirect( url_for("index") ) 
 
@app.route("/meals") 
def meals(): 
    db = get_db() 
    meals = db.execute("""SELECT * FROM meals;""").fetchall() 
    return render_template("lunch.html", meals=meals) 

@app.route("/meal/<int:meal_id>") 
def meal (meal_id): 
    db = get_db() 
    meal = db.execute("""SELECT * FROM meals WHERE meal_id = ?; """, (meal_id,)).fetchone()  
    return render_template("lunch.html", meal=meal) 

@app.route("/cart") 
@login_required 
def cart(): 
    if "cart" not in session: 
        session ["cart"] = {} 
    names = {} 
    db = get_db()  
    for meal_id in session["cart"]: 
        meal = db.execute("""SELECT * FROM meals
                            WHERE meal_id = ?;""", (meal_id,)).fetchone() 
        name = meal["name"] 
        names [meal_id] = name 
    return render_template("cart.html", cart=session["cart"], names=names)


@app.route("/add_to_cart/<int:meal_id>")
@login_required 
def add_to_cart (meal_id): 
    if "cart" not in session:  
        session ["cart"] = {} 
    if meal_id not in session["cart"]: session ["cart"] [meal_id] = 1 
    else: session["cart"] [meal_id] = session ["cart"] [meal_id]+ 1  
    return redirect(url_for("cart") )


























@app.route("/allergy", methods=["GET", "POST"])
def allergy():
    form = allergiesForm()
    if form.validate_on_submit():
        chicken = form.chicken.data
        fish = form.fish.data
        dairy =  form.dairy.data
        wheat = form.wheat.data
        nuts= form.nuts.data
        eggs = form.eggs.data
        soy = form.soy.data
        print("arrived ")
        db = get_db()
        menue = []
        if chicken == True:
            #INSERT INTO meals (name, price, allergic_chicken) 
            #	('chicken beryani', 10.99, 'rise and chicken  ','lunch',100,1,0,0,0,0,1),
            # db.execute("""SELECT *
            #             FROM meals 
            #             WHERE "alergic_chicken" is 0;""")
            
            allergy_menue = db.execute("""SELECT * FROM meals WHERE alergic_chicken = 0;""").fetchall() 
            print("suii")
            return render_template("menue.html")  
        if nuts == False:
            allergy_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_nuts]==0;
                                        ; """)
            return render_template("menue.html") 
        if soy == False:
            allergy_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_soy]==0;
                                        ; """)
            return render_template("menue.html") 
        if eggs == False:
            allergy_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_eggs]==0;
                                        ; """)
            return render_template("menue.html") 
        if fish == False:
            allergy_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_fish]==0;
                                        ; """)
            return render_template("menue.html")   
        if dairy == False:
            allergy_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_dairy]==0;
                                        ; """)
            return render_template("menue.html")   
        if wheat == False:
            new_menue = db.execute("""
                                        INSERT INTO new_menue (name)
                                        SELECT name
                                        FROM meals
                                        WHERE [alergic_wheat]==0;
                                        ; """)
            return render_template("menue.html")  



    return render_template("allergy.html",form = form )
    
if __name__ == '__main__':
    app.run(debug=True)