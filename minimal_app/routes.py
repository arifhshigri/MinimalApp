"""Route declaration."""
from flask import Flask, jsonify,session, make_response, redirect, request, render_template,url_for
from minimal_app.app_service import UserService
from flask import current_app as app
import json

appService = UserService();

@app.route("/")
@app.route("/home")
def home():
    """Landing page route."""
    return render_template(
        "home.html",
        users=appService.get_users(),
    )
@app.route("/create")
def create():
    """Landing page route."""
    return render_template("form.html",user={})

@app.route("/update/<int:id>")
def update(id):
    """Landing page route."""
    return render_template(
        "form.html",
        user=appService.get_users_by_id(id),
    )


@app.route('/api/user',methods=['GET'])
def get():
    return json.dumps(appService.get_users()),200

@app.route('/api/user', methods=['POST'])
def create_user():
    request_data = request.json
    try:
        user = appService.create_user(request_data)
        return json.dumps(user), 200
    except Exception as e :
        return json.dumps({"Message": str(e)}),400

@app.route('/api/user', methods=['PUT'])
def update_user():
    request_data = request.json
    try:
        data=appService.update_user(request_data)
        return json.dumps(data),200
    except Exception as e:
        return json.dumps({"Message":str(e)}),400
