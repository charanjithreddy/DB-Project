from flask import Blueprint, render_template, request
login_bp=Blueprint("login_bp",_name_)

@login_bp.route("/login.html", methods=['POST','GET'])
def submit():
    #print("Entered login.html");
    return render_template("login.html")