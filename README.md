numismaBack


##para subir el servidor

crear /etc/systemd/gunicorn.service
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=fabiana
Group=www-data
WorkingDirectory=/home/fabiana/numismaBack
ExecStart=/home/fabiana/numismaBack/bin/gunicorn --workers 3 --bind 0.0.0.0:8080 numismaBack.wsgi:application

sudo systemctl start gunicorn
sudo systemctl enable gunicorn


cambiar ip en /etc/nginx/sites-enabled/numismaBack
sudo systemctl restart nginx

cambiar ip en numismaFront src/app/services/config.ts
sudo ng build --env=prod --output-path=/var/www/html/