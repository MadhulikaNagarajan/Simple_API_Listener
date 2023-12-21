from flask import Flask,render_template,request
import database
import json

app = Flask(__name__)

# user_info = {
#     'username': 'Admin',
#     'Password': 'Admin@123'
# }


@app.route('/')
def home():
    return render_template('post.html')

@app.route('/save' , methods=['POST'])
def save_user():
    entered_username = request.form.get('Username')
    entered_Password = request.form.get('Password')
    if entered_username == '' or entered_Password == '':
        return 'Missing input'
    else:
        user_data = entered_username, entered_Password
        database.insert_user_data(user_data)
        return "User data saved successfully"

@app.route('/get_user', methods=['POST'])
def get_user():
    # pass
    user_data = database.get_user_data()
    return user_data


@app.route('/delete' , methods=['POST'])
def delete_user():
    entered_username = request.form.get('Username')
    user_data = entered_username
    result = database.delete_user_data(user_data)
    return result

@app.route('/update', methods=['POST'])
def update_user():
    entered_username = request.form.get('Username')
    entered_password = request.form.get('Password')
    # user_data = entered_username,entered_Password,entered_username
    result = database.update_user_data(entered_username, entered_password)
    return result

@app.route('/authorise', methods=['GET','POST'])
def check_user():
    entered_username = request.form.get('Username')
    entered_Password = request.form.get('Password')
    user_data = entered_username
    user_info = database.authorise_user_data(user_data)
    # return user_info
    if user_info == []:
        return 'Invalid input'
    elif entered_username == user_info[0][1] and entered_Password == user_info[0][2]:
        # render_template('hello.html')
        return 'you are authorised'

    else:
        return ' Invalid credenatials'

if __name__ == '__main__':
    app.run()