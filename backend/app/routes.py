from flask import request, jsonify, url_for, make_response
from . import app, bcrypt
import uuid, jwt, datetime
from functools import wraps
from .models import RegisterForm, LoginForm, ProfileImage, Users, db, userSchema, usersSchema
from flask_uploads import UploadSet, configure_uploads, IMAGES

app.config['UPLOADED_PHOTOS_DEST'] = "images"
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            var = request.headers['token']
        else:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(var, app.config['SECRET_KEY'])
            current_user = Users.query.filter_by(publicId = data['publicId']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/users/register', methods=['POST'])
def register():
    form = RegisterForm(csrf_enabled=False)
    user = Users.query.filter_by(email=form.email.data).first()
    if user:
        return jsonify({'ok': 'False', 'error': 'Email Id already exists. Try sign in'})
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
        new_user = Users(publicId = str(uuid.uuid4()), firstName = form.firstName.data, lastName = form.lastName.data, email= form.email.data, password= hashed_password)
        db.session.add(new_user)
        db.session.commit()
        result = {'email': form.email.data + ' registered'}
        return jsonify({'ok': 'True','result': result})
    return jsonify({'ok': 'False', 'error': form.errors})


@app.route('/users/login', methods=['POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    result=''
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                token = jwt.encode({'publicId' : user.publicId,
                                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                    app.config['SECRET_KEY'])
                result = jsonify({"ok": "True","token": token.decode('UTF-8')})
            else:
                result = jsonify({"ok": "False", "error": "Invalid password"})
        else:
            result = jsonify({"ok": "False","error": "invalid user"})
    else:
        result = jsonify({"ok": "False", "error": form.errors})
    return result


@app.route('/users/getProfileInformation')
@token_required
def getProfileInformation(current_user):
    try:
        result = Users.query.filter_by(publicId = current_user.publicId).first()
        if not result:
            return jsonify({"message":"no user found"})
        return userSchema.jsonify(result)
    except:
        return jsonify({'message': 'Server was unable to handle the request'}), 500


@app.route('/users/getallusers')
@token_required
def getallusers(current_user):
    try:
        all_users=Users.query.all()
        result = usersSchema.dump(all_users)
        return usersSchema.jsonify(result)
    except:
        return jsonify({'message': 'Server was unable to handle the request'}), 500


@app.route('/users/profileImage/upload', methods=['GET', 'POST'])
@token_required
def upload(current_user):
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            imageLocation = ProfileImage(publicId = current_user.publicId, imageLocation = filename)
            db.session.add(imageLocation)
            db.session.commit()
            return jsonify({'ok' :'True', 'filename' : filename})
        return jsonify({'ok' :'False'})
    except:
        return jsonify({'message': 'Server was unable to handle the request'}), 500


'''
@app.route('/users/updateProfile', methods=['POST'])
def updateProfile():
    users = mongo.db.users2
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'email': request.form.get('username'), 'profile_image_name': profile_image.filename})

    return "Done!"

    user_id = users.insert({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'created': created
    })
'''
# new_user = users.find_one({'_id': user_id})
# result = {'email': new_user['email'] + ' registered'}
# return jsonify({'result' : result})
'''
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    user = mongo.db.users3.find_one_or_404({'username': username})
    return f
            <h1>{username}</h1>
            <image src="{url_for('file', filename=user['profile_image_name'])}">
           


@app.route('/profile/upload')
def upload():
    return 
            <form method="POST" action="/create" enctype="multipart/form-data" >
            <input type="text" name="username">
            <input type="file" name="profile_image">
            <input type="submit">
           
           
@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users3.insert({'username': request.form.get('username'), 'profile_image_name': profile_image.filename})

    return "Done!"



@app.route('/verify-token', methods=['POST'])
@jwt_required
def verify_token():
    return jsonify({'success': True}), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
'''
