from sqlite3 import IntegrityError
from flask import request
import flask

import json
from flask import views, jsonify
from models import Session, ADS, Owners

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


def get_smth(model, smth_id: int):
    ads = request.session.get(model, smth_id)
    if ads is None:
        raise HttpError(404, 'Not found')
    return ads


def add_smth(smth: ADS):
    try:
        request.session.add(smth)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "Already exists")


class ADSView(views.MethodView):
    @property
    def session(self) -> Session:
        return request.session

    def __init__(self):
        self.model = ADS

    def get(self, smth_id: int):
        values = get_smth(self.model, smth_id)
        return jsonify(values.dict)

    def post(self):
        values_data = request.json
        values = self.model(**values_data)
        add_smth(values)
        return jsonify({'id': values.id})

    def patch(self, smth_id: int):
        values = get_smth(self.model, smth_id)
        values_data = request.json
        for key, value in values_data.items:
            setattr(values, key, value)
            add_smth(values)
        return jsonify({'id': values})

    def delete(self, smth_id: int):
        value = get_smth(self.model, smth_id)
        self.session.delete(value)
        self.session.commit()
        return jsonify({'status': 'ok'})


adview = ADSView.as_view('adview')
app.add_url_rule("/ads/<int:smth_id>", view_func=adview, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule("/ads", view_func=adview, methods=['POST'])


class OwnerView(ADSView):
    @property
    def session(self) -> Session:
        return request.session

    def __init__(self):
        self.model = Owners


owners = OwnerView.as_view('owners')
app.add_url_rule("/owners/<int:smth_id>", view_func=owners, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule("/owners", view_func=owners, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, )
