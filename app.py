from functools import wraps
import jwt
from flask import Flask, request, json, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash

from Model.model import User, Disaster, Addresses, Rescue, Forecast, DisasterType, Sos, Department, CoordinateRescue

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
    department_id = data.get('department_id')

    if current_user.role_id != 1:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    if not username or not password or not role_id or not department_id:
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
            'role': role_id,
            'department_id': department_id
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


@app.route('/list-forecast', methods=['GET'])
@token_required
def get_forecast(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    try:
        forecasts = Forecast.select(Forecast.id, Forecast.name, Forecast.full_address, Forecast.disaster_type,
                                    DisasterType.name.alias('disaster_name'), DisasterType.image.alias('image'),
                                    Forecast.forecast_start, Forecast.forecast_end, Forecast.reported_by). \
            join(DisasterType, on=(Forecast.disaster_type == DisasterType.id)).dicts()

        return jsonify({
            'success': True,
            'message': 'Get list forecasts successfully!',
            'data': list(forecasts)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get list forecasts!',
            'data': []
        })


@app.route('/list-alert-message', methods=['GET'])
@token_required
def list_alert_message(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    try:
        alert_messages = Sos.select().where(Sos.created_by == current_user.id).dicts()

        return jsonify({
            'success': True,
            'message': 'Get list alert message successfully!',
            'data': list(alert_messages)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get list alert message!',
            'data': []
        })


@app.route('/create-alert-message', methods=['POST'])
@token_required
def create_alert_message(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.json

    if not params.get('name') or not params.get('disaster_id') or not params.get('content') or not params.get(
            'message_type'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        data_save = {
            'name': params.get('name'),
            'disaster_id': params.get('disaster_id'),
            'content': params.get('content'),
            'message_type': params.get('message_type'),
            'created_by': current_user.id
        }
        Sos.create(**data_save)

        return json.jsonify({
            'success': True,
            'message': 'Create alert message successfully!',
            'data': []
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to create alert message!',
            'data': []
        })


@app.route('/get-sos-info', methods=['GET'])
@token_required
def get_sos_info(current_user):
    if current_user.role_id not in [1, 2, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args

    if not params.get('sos_id'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        sos = Sos.select().where(Sos.id == params.get('sos_id')).first()

        return json.jsonify({
            'success': True,
            'message': 'Get sos information successfully!',
            'data': {
                'name': sos.name,
                'time': sos.created_at,
                'lat': sos.lat,
                'lng': sos.lng,
                'content': sos.content,
                'status': sos.status
            }
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get sos information!',
            'data': []
        })


@app.route('/list-sos', methods=['GET'])
@token_required
def list_sos(current_user):
    if current_user.role_id not in [1, 2, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args

    if not params.get('disaster_id'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        sos = Sos.select(Sos.id, Sos.name, Sos.lat, Sos.lng, Sos.created_at, Sos.risk_level, Sos.content,
                         Sos.number_of_people, Sos.status). \
            join(Rescue, on=(Rescue.disaster_id == params.get('disaster_id'))).dicts()
        return json.jsonify({
            'success': True,
            'message': 'Get list sos successfully!',
            'data': list(sos)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get list sos!',
            'data': []
        })


@app.route('/get-near-rescue', methods=['GET'])
@token_required
def get_near_rescue(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args

    if not params.get('sos_id'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        rescue = Rescue.select(Rescue.id, Rescue.department_id, Department.phone, Department.member,
                               Department.available, Department.address_id). \
            join(Department, on=(Department.id == Rescue.department_id)). \
            where((Rescue.sos_id == params.get('sos_id')) and (Department.department_type == 'rescue')).first()

        address = Addresses.select(Addresses.full_address).where(Addresses.id == rescue.department.address_id).first()

        list_department = Department.select(Department.id, Department.phone, Department.member,
                                            Department.available, Addresses.full_address.alias('address')) \
            .join(Addresses, on=(Department.address_id == Addresses.id)). \
            where(Department.department_type == 'rescue').dicts()

        return json.jsonify({
            'success': True,
            'message': 'Get near rescue successfully!',
            'data': [
                {
                    'assigned_department': {
                        'id': rescue.id,
                        'phone': rescue.department.phone,
                        'member': rescue.department.member,
                        'available': rescue.department.available,
                        'full_address': address.full_address
                    },
                    'departments': list(list_department)
                }
            ]
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get list sos!',
            'data': []
        })


@app.route('/rescue-situation', methods=['GET'])
@token_required
def get_rescue_situation(current_user):
    if current_user.role_id not in [1, 2, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args

    if not params.get('department_id'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        rescue = Rescue.select(Rescue.id, Rescue.department_id, Sos.name, Sos.phone, Sos.created_at.alias('sos_time'),
                               Sos.content, Sos.status). \
            join(Department, on=(Department.id == Rescue.department_id)). \
            join(Sos, on=(Rescue.sos_id == Sos.id)). \
            where(Rescue.department_id == params.get('department_id')).dicts()

        return json.jsonify({
            'success': True,
            'message': 'Get rescue situation successfully!',
            'data': list(rescue)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get rescue situation!',
            'data': []
        })


@app.route('/create-coordinate-rescue', methods=['POST'])
@token_required
def create_coordinate_rescue(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.json
    coordinate_info = params.get('coordinate_infor')
    order_team = params.get('order_team')
    disaster_id = params.get('disaster_id')

    if not coordinate_info or not order_team or not disaster_id:
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        for order in coordinate_info:
            data_save = {
                'order_team': order_team,
                'receive_team': order.get('receive_team'),
                'num_of_people': order.get('num_of_people'),
                'disaster_id': disaster_id,
                'created_by': current_user.id
            }
            CoordinateRescue.create(**data_save)

        return json.jsonify({
            'success': True,
            'message': 'Create coordinate rescue successfully!',
            'data': []
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to create coordinate rescue!',
            'data': []
        })


@app.route('/list-coordinate-rescue', methods=['GET'])
@token_required
def list_coordinate_rescue(current_user):
    if current_user.role_id not in [1, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args
    order_team = params.get('order_team')
    disaster_id = params.get('disaster_id')

    if not order_team or not disaster_id:
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        coordinate_team = CoordinateRescue.select(CoordinateRescue.id, CoordinateRescue.receive_team,
                                                  CoordinateRescue.num_of_people, CoordinateRescue.status)\
            .where(CoordinateRescue.order_team == order_team and CoordinateRescue.disaster_id == disaster_id).dicts()
        return json.jsonify({
            'success': True,
            'message': 'List coordinate rescue successfully!',
            'data': list(coordinate_team)
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to list coordinate rescue!',
            'data': []
        })


@app.route('/get-detail-sos', methods=['GET'])
@token_required
def get_detail_sos(current_user):
    if current_user.role_id not in [1, 2, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args
    sos_id = params.get('sos_id')

    if not sos_id:
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        detail_sos = Sos.select(Sos.id, Sos.name, Sos.address_id, Sos.status, Sos.content, Sos.risk_level, Sos.lat,
                                Sos.lng, Sos.address_id).where(Sos.id == sos_id).first()
        return json.jsonify({
            'success': True,
            'message': 'Get detail sos successfully!',
            'data': {
                "address_id": detail_sos.address_id,
                "content": detail_sos.content,
                "id": detail_sos.id,
                "lat": detail_sos.lat,
                "lng": detail_sos.lng,
                "name": detail_sos.name,
                "risk_level": detail_sos.risk_level,
                "status": detail_sos.status
            }
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get detail sos!',
            'data': []
        })


@app.route('/get-rescue-team', methods=['GET'])
@token_required
def get_rescue_team(current_user):
    if current_user.role_id not in [1, 2, 3]:
        return json.jsonify({
            'success': False,
            'message': 'Do not have permission to access this function!!',
            'data': []
        })

    params = request.args
    team_id = params.get('team_id')

    if not team_id:
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    try:
        rescue_team = Department.select(Department.id, Department.name, Department.leader, Department.member,
                                        Department.address_id, Department.phone, Addresses.full_address). \
            join(Addresses, on=(Department.address_id == Addresses.id)). \
            where(Department.id == team_id and Department.department_type == 'rescue').first()

        leader_team = User.select(User.fullname).where(User.id == rescue_team.leader).first()
        members = User.select(User.fullname, User.phone, User.email).where(User.department_id == team_id).dicts()
        return json.jsonify({
            'success': True,
            'message': 'Get detail sos successfully!',
            'data': {
                "name": rescue_team.name,
                "leader_name": leader_team.fullname,
                "phone": rescue_team.phone,
                "num_of_member": rescue_team.member,
                "address": rescue_team.addresses.full_address,
                "members": list(members)
            }
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success': False,
            'message': 'Fail to get detail sos!',
            'data': []
        })


if __name__ == '__main__':
    app.debug = True
    app.run()
