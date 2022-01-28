# Como ejecutar esta aplicacion

# aca los pasos



python3 -m venv venv
. venv/bin/activate
pip install Flask


export FLASK_APP=main
flask run

If you want to run in all interfaces
flask run --host=0.0.0.0


For execute that in debug mode
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_ENV=production
