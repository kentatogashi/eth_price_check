from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db_uri = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (app.config["DB_USER"],app.config["DB_PASS"],app.config["DB_HOST"],app.config["DB_NAME"])
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Price(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer, nullable=False)
    ask = db.Column(db.Integer, nullable=False)
    exchange_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, id, bid, ask, created_at):
        self.id = id
        self.bid = bid
        self.ask = ask
        self.exchange_id = exchange_id
        self.created_at = created_at

    def __repr__(self):
        return '<Price %r>' % self.id

@app.route('/')
def index():
    rows = Price.query.all()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run()
