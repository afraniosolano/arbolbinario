""" import packages """
from connexion.resolver import RestyResolver
import connexion
from flask_cors import CORS
from healthcheck import HealthCheck, EnvironmentDump
import application.application_factory as application_factory
import config.default_config as config

v_config = config.DefaultConfig()

v_application = application_factory.ApplicationFactory.factory(v_config)

if v_config.get_string("rest", "host") != "":
    vhost = v_config.get_string("rest", "host")
    print("Using host " + vhost)
else:
    vhost = "0.0.0.0"
    print("Using default host " + vhost)

if v_config.get_string("rest", "port") != "":
    vport = v_config.get_string("rest", "port")
    print("Using port " + vport)
else:
    vport = "9224"
    print("Using default port " + vport)

if v_config.get("app", "debug") != "":
    vdebug = v_config.get("app", "debug")
    print("Using debug " + str(vdebug))
else:
    vdebug = False
    print("Using default debug " + str(vdebug))

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('arbolbinario.yml')
CORS(app.app)

health = HealthCheck()

envdump = EnvironmentDump()


def database_available():
    return True, "database ok"


health.add_check(database_available)

# Add a flask route to expose information
app.add_url_rule(
    "/arbolbinario/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule(
    "/arbolbinario/environment", "environment", view_func=lambda: envdump.run())


def run_rest_server():
    app.run(
        host=vhost,
        port=vport,
        debug=vdebug,
        threaded=True,
        use_reloader=False)


if __name__ == '__main__':
    run_rest_server()
