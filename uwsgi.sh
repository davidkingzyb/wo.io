nohup uwsgi --socket 127.0.0.1:3031 --wsgi-file ~/project/wo.io/woio_server.py --callable app --processes 2 --threads 2 --stats 127.0.0.1:9191 &
