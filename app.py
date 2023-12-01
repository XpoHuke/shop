from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'Запись: {self.title}'


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stra')
def stra():
    items = Item.query.all()
    return render_template('stra.html', items=items)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        text = request.form['text']
        price = request.form['price']


        item = Item(title=title, text=text, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR 404"
    else:
        return render_template('create.html')



if __name__ == '__main__':
    app.run(debug=True)