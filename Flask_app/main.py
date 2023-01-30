from views import ArticleView, UserView, app


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users'),
                 methods=['GET', 'DELETE'])
app.add_url_rule('/users/', view_func=UserView.as_view('create_user'), methods=['POST'])

app.add_url_rule('/articles/<int:article_id>', view_func=ArticleView.as_view('articles'),
                 methods=['GET'])
app.add_url_rule('/articles/', view_func=ArticleView.as_view('crud_articles'),
                 methods=['POST', 'DELETE', 'PATCH'])


if __name__ == "__main__":
    app.run()
