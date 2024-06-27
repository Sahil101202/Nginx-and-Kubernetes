# nginx/Dockerfile
FROM sahil101202/nginx-frontend:latest

# Copy custom nginx config
COPY ./nginx.conf /etc/nginx/nginx.conf

# Copy static files
COPY ./html/ /usr/share/nginx/html/
