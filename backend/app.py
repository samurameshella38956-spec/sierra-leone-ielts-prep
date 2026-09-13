from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@db:5432/ielts"
app.config["JWT_SECRET_KEY"] = "super-secret-key"

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register routes
from routes import auth, exam, payment, scholarship
app.register_blueprint(auth.bp)
app.register_blueprint(exam.bp)
app.register_blueprint(payment.bp)
app.register_blueprint(scholarship.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
