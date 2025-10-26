from flask import Blueprint,render_template

password_reset_bp=Blueprint("password_reset_bp",_name_)

@password_reset_bp.route("/password_reset.html",methods=['POST','GET'])
def password_reset():
    return render_template("password_reset.html");