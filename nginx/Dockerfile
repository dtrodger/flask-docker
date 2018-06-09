FROM nginx:latest
RUN rm /etc/nginx/nginx.conf && \
    rm /etc/nginx/conf.d/default.conf
COPY conf/nginx.conf /etc/nginx/
COPY conf/web_app.conf /etc/nginx/conf.d/
CMD ["nginx", "-g", "daemon off;"]
