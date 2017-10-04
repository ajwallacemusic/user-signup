from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG']=True




@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    #variables
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']
    errornames = []
    errors = []
    redirect_url = "/?"

    #populate error variables
    if not username:
        usernameerror = "Please enter a username."
        errornames.append("usernameerror")
        errors.append(usernameerror)
    elif len(username) < 3 or len(username) > 20 or " " in username:
        usernameerror = "Not a valid username Username. must be more than 3 characters long, less than 20 characters long, and not contain spaces."
        errornames.append("usernameerror")
        errors.append(usernameerror)
    if not password:
        passworderror = "Please enter a password."
        errornames.append("passworderror")
        errors.append(passworderror)
    elif len(password) < 3 or len(password) > 20 or " " in password:
        passworderror = "Not a valid password. Password must be more than 3 characters long, less than 20 characters long, and not contain spaces."
        errornames.append("passworderror")
        errors.append(passworderror)
    if password != verify_password:
        verify_pass_error = "Passwords don't match."
        errornames.append("verify_pass_error")
        errors.append(verify_pass_error)
    if " " in email or "@" not in email or "." not in email:
        emailerror = "Not a valid email."
        errornames.append("emailerror")
        errors.append(emailerror)
    
    if len(errornames) == 0:
        return render_template('welcome.html', username=username, password=password, email=email)
    else:
        for i in range(len(errornames)):
            redirect_url += errornames[i] + "=" + errors[i] + "&"
        print(errornames)
        return redirect(redirect_url)

    


@app.route("/", methods=['GET', 'POST'])
def index():
    usernameerror = request.args.get("usernameerror")
    password_error = request.args.get("passworderror")
    verify_pass_error = request.args.get("verify_pass_error")
    email_error = request.args.get("emailerror")
    return render_template('signup.html', title='User Signup', usernameerror=usernameerror, password_error=password_error, verify_pass_error=verify_pass_error, email_error=email_error)


#run app
app.run()