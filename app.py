from functools import wraps
import jwt
from flask import Flask, request, json, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash

from Model.model import User, Disaster, Addresses, Rescue

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NoBaABRXyMcHvWnCTLtkpL0BX7iOONf9'


@app.route('/hello')
def hello_world():  # put application's code here
    return jsonify(oretrack="okeokeoke")


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return json.jsonify({
                'success': False,
                'message': 'Token is missing!!',
                'data': []
            })

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.select().where(User.password == data['password']).first()
        except Exception as e:
            print(e)
            return json.jsonify({
                'success': False,
                'message': 'Token is invalid!!',
                'data': []
            })
        return f(current_user, *args, **kwargs)
        # return current_user

    return decorated


# signup route
@app.route('/add-account', methods=['POST'])
@token_required
def addAccount(current_user):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role_id = data.get('role')

    if current_user.role_id != 1:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    if not username or not password or not role_id:
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })

    try:
        # checking for existing user
        user = User.select().where(User.username == username).first()

        if user:
            return json.jsonify({
                'success': False,
                'message': 'User already exists!',
                'data': []
            })

        # insert user
        data_save = {
            'username': username,
            'password': generate_password_hash(password),
            'role': role_id
        }
        User.create(**data_save)

        return json.jsonify({
            'success': True,
            'message': 'Successfully registered!',
            'data': []
        })
    except Exception as e:
        print(e)
        return json.jsonify({
            'success': False,
            'message': 'Fail registered!',
            'data': []
        })


# route for logging user in
@app.route('/login', methods=['POST'])
def login():
    auth = request.json

    if not auth or not auth.get('username') or not auth.get('password'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    user = User.select().where(User.username == auth.get('username')).first()

    if not user:
        return json.jsonify({
            'success': False,
            'message': 'User does not exist !!',
            'data': []
        })

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'password': user.password
        }, app.config['SECRET_KEY'])
        return json.jsonify({
            'success': True,
            'message': 'Login successful!!',
            'token': token
        })

    return json.jsonify({
        'success': False,
        'message': 'Wrong password!!',
        'data': []
    })


# Overview
@app.route('/get-disasters', methods=['GET'])
@token_required
def get_disasters(current_user):
    params = request.args
    name_param = params.get('name') or None
    time_param = params.get('start_time') or '2023-01-01 00:00:00'

    if current_user.role_id not in [1, 2]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })
    try:
        if name_param:
            disasters = Disaster.select(Disaster.id, Disaster.name, Disaster.risk_level, Disaster.start_at,
                                        Disaster.end_at, Addresses.full_address, Addresses.id) \
                .join(Addresses, on=(Disaster.address_id == Addresses.id)).where(
                Disaster.name.contains(name_param) | Disaster.start_at >= time_param).order_by(Disaster.start_at) \
                .dicts()
        else:
            disasters = Disaster.select(Disaster.id, Disaster.name, Disaster.risk_level, Disaster.start_at,
                                        Disaster.end_at, Addresses.full_address, Addresses.id) \
                .join(Addresses, on=(Disaster.address_id == Addresses.id)).where(Disaster.start_at >= time_param) \
                .order_by(Disaster.start_at).dicts()

        return jsonify({
            'success': True,
            'message': 'Get disasters successfully!',
            'data': list(disasters)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get disasters!',
            'data': []
        })


@app.route('/get-detail-disaster', methods=['GET'])
@token_required
def get_detail_disaster(current_user):
    if current_user.role_id not in [1, 2]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args
    if not params.get('disaster_id'):
        return jsonify({
            'success': False,
            'message': 'Missing id of disaster!',
            'data': []
        })
    disaster_id = params['disaster_id']
    try:

        disasters = Disaster.select(Disaster.id, Disaster.name, Disaster.risk_level, Disaster.address_id,
                                    Addresses.full_address, Addresses.lat, Addresses.province_name,
                                    Addresses.district_name, Addresses.corner_name, Addresses.lng). \
            join(Addresses, on=(Disaster.address_id == Addresses.id)).where(Disaster.id == disaster_id).first()

        total_sos = Rescue.select(Rescue.id, Rescue.sos_id).where(Rescue.disaster_id == disaster_id).count()

        return jsonify({
            'success': True,
            'message': 'Get disasters successfully!',
            'data': {
                'id': disasters.id,
                'name': disasters.name,
                'lat': disasters.addresses.lat,
                'lng': disasters.addresses.lng,
                'full_address': disasters.addresses.full_address,
                'province_name': disasters.addresses.province_name,
                'district_name': disasters.addresses.district_name,
                'street_name': disasters.addresses.street_name,
                'hamlet_name': disasters.addresses.hamlet_name,
                'corner_name': disasters.addresses.corner_name,
                'risk_level': disasters.risk_level,
                'total_sos': total_sos
            }
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get detail disasters!',
            'data': []
        })


if __name__ == '__main__':
    app.debug = True
    app.run()
