# Como ejecutar esta aplicacion

# aca los pasos




python3 -m venv venv
. venv/bin/activate
pip install Flask

pip freeze > requirements.txt


export FLASK_APP=main
flask run

If you want to run in all interfaces
flask run --host=0.0.0.0


For execute that in debug mode
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_ENV=production


pip install opentelemetry-api
pip install opentelemetry-sdk
pip install opentelemetry-exporter-jaeger
pip install opentelemetry-propagator-jaeger
pip install scalene


scalene main.py

# Referencia
https://pythonexamples.org/
https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
https://www.ietf.org/rfc/rfc2068.txt
https://pythonbasics.org/flask-tutorial-routes/



curl -X GET 'http://localhost:5000/' \
  -H 'User-Agent: Mozilla/5.0' \
  --compressed


curl -X GET 'http://localhost:5000/producto/1' \
  -H 'User-Agent: Mozilla/5.0' \
  --compressed


curl -X DELETE 'http://localhost:5000/producto/1' \
  -H 'User-Agent: Mozilla/5.0' \
  --compressed


curl -X POST 'http://localhost:5000/producto/5/Panela/250' \
   -H 'User-Agent: Mozilla/5.0' \
   --compressed
