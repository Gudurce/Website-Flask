from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mail import Mail, Message
import secrets

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'branislavguduricns@gmail.com'
app.config['MAIL_PASSWORD'] = 'wiuq kkqw qsdw zkdb '
app.config['MAIL_DEFAULT_SENDER'] = 'branislavguduricns@gmail.com'
app.config['SECRET_KEY'] = secrets.token_hex(16)

mail = Mail(app)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/expertise")
def expertise():
    return render_template("expertise.html")

@app.route("/send_email", methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    subject = f"New Contact Form Submission from {name}"
    
    msg = Message(subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=['branislavguduricns@gmail.com'])
    
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    try:
        mail.send(msg)
        flash('Your message has been send successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        print(f'Failed to send email: {e}')
        flash('There was an issue sending your message. Please try again later.', 'danger')
        return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(host='68.183.222.38', port=80)