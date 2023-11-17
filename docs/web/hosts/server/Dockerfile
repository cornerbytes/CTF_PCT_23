FROM alpine:latest
EXPOSE 80
RUN apk add --no-cache nginx \
	&& adduser -D -g 'www' www \
	&& mkdir /www && mkdir /secret
COPY index.html /www/index.html
COPY flag.txt /secret/flag.txt
COPY nginx.conf /etc/nginx/nginx.conf
RUN chown -R www:www /var/lib/nginx && chown -R www:www /www && chown -R www:www /secret
CMD ["nginx", "-g", "daemon off;"]
