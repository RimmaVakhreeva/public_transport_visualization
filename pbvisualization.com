server {

        root   /var/www/pbvisualization.com/html;
        index  map.html;

        server_name pbvisualization.com www.pbvisualization.com;


        location / {
                try_files $uri $uri/ =404;
        }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/pbvisualization.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/pbvisualization.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = www.pbvisualization.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    if ($host = pbvisualization.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
        listen 80;
        server_name pbvisualization.com www.pbvisualization.com;
    return 404; # managed by Certbot
