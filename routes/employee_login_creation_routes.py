from flask import Blueprint, render_template, request

employee_login_creation_bp=Blueprint("employee_login_creation_bp",_name_)

@employee_login_creation_bp.route("/employee_login_creation.html",methods=['POST','GET'])
def create_employee():
    return render_template("employee_login_creation.html");