arbolbinario
===

Pasos para instalar arbolbinario
===

1. git clone https://github.com/afraniosolano/arbolbinario.git arbolbinario
2. python3.6 -m venv arbolbinario
3. cd arbolbinario
4. source bin/activate
5. pip install -r requirements.txt
6. python setup.py sdist
7. python setup.py install
8. python app.py

===
# Instalación en ubuntu 18 - para desarrolladores
# Antes instalar:
sudo apt-get install python3.6
sudo apt-get install python3.6-venv

1. git clone https://github.com/afraniosolano/arbolbinario.git arbolbinario
2. python3.6 -m venv arbolbinario
3. cd arbolbinario
4. source bin/activate
5. pip install -r requirements.txt
6. pip install nosexcover
7. pip install pylint
8. python setup.py develop
#  Ejecutar el server
9. bin/serve
===
# Instalación en windows - para desarrolladores

1. git clone https://github.com/afraniosolano/arbolbinario.git arbolbinario
2. python -m venv arbolbinario
3. cd arbolbinario
4. scripts\activate
5. pip install -r requirements.txt
6. pip install nosexcover
7. pip install pylint
8. python setup.py develop
#  Ejecutar el server
9. scripts\serve

===
#Ejecución en servidores

1. sudo ps -fea | grep arbolbinario

2. kill -9

3. source bin/activate

4. gunicorn --config ./gunicorn_conf.py rest.app:app

===
#Ruta de instalación

1. /opt/environments/arbolbinario
2. /var/log/arbolbinario/
