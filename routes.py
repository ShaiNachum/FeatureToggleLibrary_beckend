from controllers.feature_toggle import feature_toggle_blueprint

def initial_routes(app):
    app.register_blueprint(feature_toggle_blueprint)