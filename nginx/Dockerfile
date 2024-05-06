# Use the official NGINX image as a base
FROM nginx:latest

# Copy the NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Remove default NGINX website
RUN rm -rf /usr/share/nginx/html/*

# Copy the frontend files to the NGINX web server directory
COPY html/ /usr/share/nginx/html/
