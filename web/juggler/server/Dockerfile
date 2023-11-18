FROM alpine:latest
EXPOSE 80
RUN apk add --no-cache nginx supervisor php81-fpm \
	&& adduser -D -g 'www' www \
	&& mkdir /www
COPY supervisord.conf /etc/supervisord.conf
COPY index.php flag.php /www/
COPY flag.txt /flag.txt
COPY nginx.conf /etc/nginx/nginx.conf
RUN chown -R www:www /var/lib/nginx && chown -R www:www /www && chown www:www /flag.txt
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
