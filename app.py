from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'tajna123'  # ključ za sesiju (čuva korisnika ulogovanim)

USERS = {}  # username -> password
PROGRESS = {}  # username -> poslednji level



@app.route('/')
def index():
    if 'user' in session:
        username = session['user']
        current_level = PROGRESS.get(username, 1)
        return render_template("index.html", user=username, current_level=current_level)
    return render_template("index.html", user=None)

@app.route('/level/<int:level_id>', methods=['GET', 'POST'])
def level(level_id):
    level_data = LEVELS.get(level_id)
    if not level_data:
        return "Nivo ne postoji."

    message = ""
    if request.method == 'POST':
        user_code = request.form['answer']
        message = user_code
        if 'user' in session:
            username = session['user']
            # Otključavanje sledećeg levela ako je korisnik stigao do ovog ili dalje
            if level_id >= PROGRESS.get(username, 1):
                PROGRESS[username] = level_id + 1

    return render_template("level.html",
                           level_id=level_id,
                           title=level_data["title"],
                           question=level_data["question"],
                           message=message)
def level(level_number):
    user = session.get("user")
    if not user:
        return redirect("/login")

    level_data = LEVELS.get(level_number)
    submitted_code = ""
    is_correct = False

    if request.method == "POST":
        submitted_code = request.form["code"].strip()
        correct_answer = level_data.get("expected_answer")

        # Poređenje odgovora
        if submitted_code == correct_answer.strip():
            is_correct = True
            # Ovde možeš da povećavaš level korisniku ako hoćeš

    return render_template("level.html", level=level_data,
                           submitted_code=submitted_code,
                           is_correct=is_correct)







@app.route('/levels/<int:page>')
def levels(page):
    levels_per_page = 10
    start = (page - 1) * levels_per_page + 1
    end = start + levels_per_page
    visible_levels = {k: v for k, v in LEVELS.items() if start <= k < end}

    total_pages = (len(LEVELS) + levels_per_page - 1) // levels_per_page

    return render_template(
        "levels.html",
        levels=visible_levels,
        page=page,
        total_pages=total_pages
    )
LEVELS = {
    1: {
        "title": "Prvi zadatak: Ispis imena",
        "question": "Napiši kod koji ispisuje tvoje ime na ekranu.",
        "hint": "Koristi funkciju `print()`.",
        "starter_code": "# Ovde napiši svoj kod\n",
        "expected_answer": "print(\"Alex\")"
    },
2: {
        "title": "Drugi  zadatak: Sabiranje",
        "question": "Napiši kod koji ispisuje zbir broja 5 i 10.",
        "hint": "Koristi funkciju `print()`.",
        "starter_code": "# Ovde napiši svoj kod\n"
    },
3: {
        "title": "3 zadatak: mnozenje",
        "question": "Napiši kod koji ispisuje kolicnik brojeva 100 i 10.",
        "hint": "Koristi funkciju `print()`.",
        "starter_code": "# Ovde napiši svoj kod\n"
    },
4:{
    "title":"4 zadatak :opis",
    "question":"",
    "hint":"",
    "starer_code":"# ovde napisi kod\n"
},
 5: {
    "title": "5 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  6: {
    "title": "6 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  7: {
    "title": "7 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  8: {
    "title": "8 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  9: {
    "title": "9 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  10: {
    "title": "10 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  11: {
    "title": "11 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  12: {
    "title": "12 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  13: {
    "title": "13 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  14: {
    "title": "14 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  15: {
    "title": "15 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  16: {
    "title": "16 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  17: {
    "title": "17 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  18: {
    "title": "18 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  19: {
    "title": "19 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  },
  20: {
    "title": "20 zadatak :opis",
    "question": "",
    "hint": "",
    "starer_code": "# ovde napisi kod\n"
  }

}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS:
            return "Korisnik već postoji."
        USERS[username] = password
        PROGRESS[username] = 1  # kreće od levela 1
        return redirect('/login')
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['user'] = username
            return redirect('/')
        else:
            return "Pogrešan username ili password."
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
