from sqlite3 import IntegrityError

import flask
from flask import request
import request
import json
from flask import views, jsonify
from models import Session, ADS

app = flask.Flask("app")


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response: flask.Response):
    request.session.close()
    return response


class HttpError(Exception):
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


@app.errorhandler(HttpError)
def error_handler(error):
    response = jsonify({'error': error.description})
    response.status_code = error.status_code
    return response


def get_ads(ads_id: int):
    ads = request.session.get(ADS, ads_id)
    if ads is None:
        raise HttpError(404, 'ADS not found')
    return ads


class ADSView(views.MethodView):
    @property
    def session(self) -> Session:
        return request.session

    def get(self, ads_id: int):
        ads = get_ads(ads_id)
        return jsonify(ads.dict)

    def post(self):
        ads_data = request.json()
        ads = ADS(**ads_data)
        try:
            request.session.add(ads)
            request.session.commit()
        except IntegrityError as err:
            raise HttpError(409, "ADS already exist")
        return jsonify({'id': ads.id})

    def patch(self, ADS_id: int):
        ads = get_ads(ADS_id)
        ads_data = request.json
        for key, value in ads_data.items():
            setattr(ads, key, value)
            try:
                request.session.add(ads)
                request.sessiom.commit()
            except IntegrityError as err:
                raise HttpError(409, "ADS already exist")
        return jsonify({'id': ads.id})

    def delete(self, ADS_id: int):
        ads = get_ads(ADS_id)
        self.session.delete(ads)
        self.session.commit()
        return jsonify({'status': 'ok'})


adswiev = ADSView.as_view('adswiev')
app.add_url_rule("/ads/<int:ads_id>", view_func=adswiev, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule("/ads", view_func=adswiev, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, )
