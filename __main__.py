from flask import Flask, redirect, render_template, request, session, url_for

# create a Flask application with name "__main__"
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    """Role selection page"""
    # if user is logged in, render role selection page 
    if session.get("logged_in", False):
        return render_template("index.html",
                            user_rank=_USER_RANK,
                            user_name=_USER_NAME,
                            user_unit_number=_USER_UNIT_NUMBER)
    # if user *is not* logged in, redirect to login page
    else:
        print("Not logged in... redirecting to login")
        return redirect(url_for("login"))

@app.route("/login", methods=['POST', 'GET'])
def login():
    """Login page"""
    # if user is not logged in, render login page
    if not session.get("logged_in", False):
        return render_template("login.html")
    #if user *is* logged in, redirect to index (aka the role selection page)
    else:
        print("Logged in... redirecting to index")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()