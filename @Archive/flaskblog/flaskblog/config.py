import os


class Config:
    SECRET_KEY = "WKNXpBOtYpcvtWBOpjMPFOAe1IgGuWWm"
    SQLALCHEMY_DATABASE_URI = "postgresql://flaskbloguser:WKNXpBOtYpcvtWBOpjMPFOAe1IgGuWWm@dpg-chgr2367avjbbjpntevg-a.oregon-postgres.render.com/flaskblogdb"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'test@gmail.com'
    MAIL_PASSWORD = 'test123'
