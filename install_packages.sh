conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python flask
conda install psycopg2
conda install flask-sqlalchemy
pip install flask-migrate
conda install gunicorn
