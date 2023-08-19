FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

WORKDIR /amazon_service

COPY requirements.txt requirements.txt

RUN pip --no-cache-dir install -r  requirements.txt

COPY . /amazon_service/

EXPOSE 1043

CMD make run_app


"""
sudo su
sudo apt update
sudo apt install nginx -y
systemctl status nginx
mkdir ccf_aws
cd ccf_aws/
wget https://github.com/RimmaVakhreeva/public_transport_visualization/archive/refs/heads/test.zip
apt install unzip
unzip test.zip
cd public_transport_visualization-test/
mv * /var/www/
cd /var/www/
rm -rf html/
sudo mkdir -p /var/www/pbvisualization.com/html
sudo chown -R $USER:$USER /var/www/pbvisualization.com/html
sudo chmod -R 755 /var/www/pbvisualization.com
mv map.html /var/www/pbvisualization.com/html/
mv pbvisualization /etc/nginx/sites-available/
mv fastapi_nginx /etc/nginx/sites-available/
cd /etc/nginx/sites-available/
rm default
cd /etc/nginx/sites-enabled/
rm default
sudo ln -s /etc/nginx/sites-available/pbvisualization /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/fastapi_nginx /etc/nginx/sites-enabled/


cd /home/ubuntu/
git clone https://github.com/lcalcagni/Deploying-FastAPI-using-Nginx.git
cd Deploying-FastAPI-using-Nginx/
apt-get update
sudo apt install python3-pip
pip3 install -r requirements.txt
cd /var/www/
pip3 install -r requirements.txt
python3 -m uvicorn main:app


snap version
apt policy snapd
apt install snapd
sudo snap install core
sudo snap refresh core
sudo apt-get remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --version
sudo certbot --nginx --test-cert
sudo certbot renew --dry-run

"""