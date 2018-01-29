import datetime
from hashlib import md5
from flask import Flask, session, flash, redirect, url_for, request, render_template, abort, g
from functools import wraps
from peewee import IntegrityError
from blog.util.database import Sqlite
from blog.models.user import UserModel, RelationshipModel
from blog.models.message import MessageModel


DEBUG = True
SECRET_KEY = 'hin6bab8ge25'


app = Flask(__name__)
app.config.from_object(__name__)


def create_tables():
    connection = Sqlite().get_connection()
    connection.connect()
    connection.create_tables([UserModel, MessageModel, RelationshipModel])


def seed_tables():
    user_pera = UserModel.create(username='pera', password=md5('pera'.encode('utf-8')).hexdigest(), email='pera@test.com', join_date=datetime.datetime.now())
    user_mika = UserModel.create(username='mika', password=md5('mika'.encode('utf-8')).hexdigest(), email='mika@test.com', join_date=datetime.datetime.now())
    RelationshipModel.create(from_user=user_pera, to_user=user_mika)
    RelationshipModel.create(from_user=user_mika, to_user=user_pera)
    MessageModel.create(user=user_mika, content='content mika', pub_date=datetime.datetime.now())
    MessageModel.create(user=user_pera, content='content pera', pub_date=datetime.datetime.now())


def auth_user(user):
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username
    flash('You are logged in as %s' % user.username)


def get_current_user():
    if session.get('logged_in'):
        return UserModel.get(UserModel.id ==session['logged_in'])


def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return inner


def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page=int(request.args.get('page', 1)),
        pages=qr.count() / 20 + 1
    )
    kwargs[var_name] = qr.paginate(kwargs['page'])
    return render_template(template_name, **kwargs)


def get_object_or_404(model, *expressions):
    try:
        return model.get(*expressions)
    except model.DoesNotExist:
        abort(404)


@app.template_filter('is_following')
def is_following(from_user, to_user):
    return from_user.is_following(to_user)


@app.before_request
def before_request():
    g.db = Sqlite().get_connection()
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def homepage():
    if session.get('logged_in'):
        return private_timeline()
    else:
        return public_timeline()


@app.route('/private/')
def private_timeline():
    user = get_current_user()
    messages = MessageModel.select().where(MessageModel.user << user.following())
    return object_list('private_messages.html', messages, 'message_list')


@app.route('/public/')
def public_timeline():
    messages = MessageModel.select()
    return object_list('public_messages.html', messages, 'message_list')


@app.route('/join/', methods=['GET', 'POST'])
def join():
    if request.method == 'POST' and request.form['username']:
        try:
            with Sqlite().get_connection().transaction():
                user = UserModel.create(
                    username=request.form['username'],
                    password=md5((request.form['password']).encode('utf-8')).hexdigest(),
                    email=request.form['email'],
                    join_date=datetime.datetime.now()
                )
                auth_user(user)
                return redirect(url_for('homepage'))

        except IntegrityError:
            flash('That username is already taken')

    return render_template('join.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username']:
        try:
            user = UserModel.get(
                username=request.form['username'],
                password=md5((request.form['password']).encode('utf-8')).hexdigest()
            )

        except UserModel.DoesNotExist:
            flash('The password entered is incorect')

        else:
            auth_user(user)
            return redirect(url_for('homepage'))

    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('homepage'))


@app.route('/following/')
@login_required
def following():
    user = get_current_user()
    return object_list('user_following.html', user.following(), 'user_list')


@app.route('/users/')
def user_list():
    users = UserModel.select()
    return object_list('user_list.html', users, 'user_list')


@app.route('/users/<username>/')
def user_detail(username):
    user = get_object_or_404(UserModel, UserModel.username == username)
    # messages = user.message_set
    messages = MessageModel.select().where(MessageModel.user == user).order_by('pub_date', 'desc')
    # messages = MessageModel.select().where(MessageModel.user << user).order_by(('pub_date', 'desc'))
    return object_list('user_detail.html', messages, 'message_list', user=user)


@app.route('/users/<username>/follow/')
@login_required
def user_follow(username):
    user = get_object_or_404(UserModel, UserModel.username == username)
    try:
        with Sqlite().get_connection().transaction():
            RelationshipModel.create(
                from_user=get_current_user(),
                to_user=user
            )

    except IntegrityError:
        pass

    flash('You are following %s' % user.username)
    return


@app.route('/users/<username>/unfollow/', methods=['POST'])
@login_required
def user_unfollow(username):
    user = get_object_or_404(UserModel, UserModel.username == username)
    RelationshipModel.delete().where(
        (RelationshipModel.from_user == get_current_user()) &
        (RelationshipModel.to_user == user)
    ).execute()
    flash('You are no longer following %s' % user.username)
    return redirect(url_for('user_detail', username=user.username))


@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    user = get_current_user()
    if request.method == 'POST' and request.form['content']:
        MessageModel.create(
            user=user,
            content=request.form['content'],
            pub_date=datetime.datetime.now()
        )
        flash('Your message has been created')
        return redirect(url_for('user_detail', username=user.username))

    return render_template('create.html')


@app.context_processor
def _inject_user():
    return {'current_user': get_current_user()}


if __name__ == '__main__':
    app.run()
