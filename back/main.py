from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
db = SQLAlchemy(app)

CORS(app)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    note = db.Column(db.String)
    beer_price = db.Column(db.Float)
    bar_name = db.Column(db.String)
    reviewer = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = Review.query.all()
        reviews_list = [review.to_dict() for review in reviews]
        return jsonify(reviews_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    review = Review(latitude=data['latitude'], longitude=data['longitude'],
                    note=data['note'], beer_price=data['beer_price'], bar_name=data['bar_name'], reviewer=data['reviewer'], description=data['description'])

    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "review added successfully!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
