# Use an official PHP image as the base image
FROM php:7.4-fpm

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Set the working directory to /var/www/html
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html

COPY ./nginx.conf /etc/nginx/sites-available/default
COPY ./index.php /var/www/html

# make folder
RUN mkdir -p /var/www/html/
RUN mkdir -p /var/www/html/admin/
RUN mkdir -p /var/www/html/uploads/

COPY admin/index.php /var/www/html/admin/


RUN chown -R www-data:www-data uploads/
RUN chown -R www-data:www-data admin/
RUN chmod 777 uploads/

# Configure Nginx

# Expose port 80
EXPOSE 80

# Start Nginx and PHP-FPM
CMD service nginx start && php-fpm
