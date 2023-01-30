from flask.views import MethodView
from flask import request, jsonify
from flask import Flask
from models import UserModel, ArticleModel, Session
from errors import HttpException
from validator import validate, PatchArticleValidator, DeleteArticleValidator, PostArticleValidator

app = Flask('app')


@app.errorhandler(HttpException)
def error_hanler(error: HttpException):
    http_response = jsonify({
        'message': error.message
    })
    http_response.status_code = error.status_code
    return http_response


def get_user(user_id: int, session):
    user = session.query(UserModel).get(user_id)
    if user is None:
        raise HttpException(
            statu_code=404,
            message='Пользователь не найден'
        )
    return user


def get_article(article_id: int, session):
    article = session.query(ArticleModel).get(article_id)
    if article is None:
        raise HttpException(
            statu_code=404,
            message='Объявление не найдено'
        )
    return article


class UserView(MethodView):
    def get(self, user_id: int):
        with Session() as session:
            user = get_user(user_id, session)
            return jsonify({
                'id': user.id,
                'name': user.name,
                'email': user.email
            })

    def post(self):
        user_data = request.json
        with Session() as session:
            new_user = UserModel(**user_data)
            session.add(new_user)
            session.commit()
            return jsonify({'Статус': f'Пользователь {new_user.name} создан'})

    def delete(self):
        pass


class ArticleView(MethodView):
    def get(self, article_id: int):
        with Session() as session:
            article = get_article(article_id, session)
            return jsonify({
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'creation_time': article.creation_time.isoformat(),
                'id_user': article.id_user
            })

    def post(self):
        article_data = validate(request.json, PostArticleValidator)
        with Session() as session:
            get_user(article_data['id_user'], session)
            new_article = ArticleModel(**article_data)
            session.add(new_article)
            session.commit()
            return jsonify({'status': 'Объявление создано'})

    def patch(self):
        article_data = validate(request.json, PatchArticleValidator)
        with Session() as session:
            article = get_article(article_data['id'], session)
            if article_data['id_user'] == article.id_user:
                for field, value in article_data.items():
                    setattr(article, field, value)
                session.add(article)
                session.commit()
                return jsonify({
                    'status': 'Объявление измененно'
                })
            else:
                return jsonify({
                     'status': 'Вы не можете обновлять чужие объявления'
                })

    def delete(self):
        article_data = validate(request.json, DeleteArticleValidator)
        with Session() as session:
            article = get_article(article_data['id'], session)
            if article_data['id_user'] == article.id_user:
                session.delete(article)
                session.commit()
                return jsonify({
                    'status': 'Объявление удалено'
                })
            else:
                return jsonify({
                    'status': 'Вы не можете удалять чужие объявления'
                })
