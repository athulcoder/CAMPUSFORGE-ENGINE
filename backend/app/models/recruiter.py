# app/models/recruiter.py
from app.extensions import db
from passlib.hash import pbkdf2_sha256 as hasher
class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    resumes = db.relationship("Resume", backref="recruiter", lazy=True)


    def set_password(self, passw:str):
        self.password_hash = hasher.hash(passw);
        print(self.password_hash)

    def check_password(self,passw:str):
        return hasher.verify(passw,self.password_hash);
    def get_recruiter(self):
        return {
            "email":self.email,
            "name":self.name
        }