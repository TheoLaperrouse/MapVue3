from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///markers.db'
db = SQLAlchemy(app)


class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    note = db.Column(db.String)
    beer_price = db.Column(db.Float)


with app.app_context():
    db.create_all()


@app.route('/markers', methods=['GET'])
def get_markers():
    try:
        markers = Marker.query.all()
        marker_list = []
        for marker in markers:
            marker_data = {
                "latitude": marker.latitude,
                "longitude": marker.longitude,
                "note": marker.note,
                "beer_price": marker.beer_price
            }
            marker_list.append(marker_data)

        return jsonify(marker_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/markers', methods=['POST'])
def add_marker():
    try:
        data = request.get_json()
        latitude = data['latitude']
        longitude = data['longitude']
        note = data['note']
        beer_price = data['beer_price']

        marker = Marker(latitude=latitude, longitude=longitude,
                        note=note, beer_price=beer_price)
        db.session.add(marker)
        db.session.commit()
        return jsonify({"message": "Marker added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
