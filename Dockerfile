FROM ubuntu
MAINTAINER Emmanuel Agbedejobi <emmanuelagbedejobi@gmail.com>
COPY time_counter /usr/local/bin/time_counter
RUN chmod +x /usr/local/bin/time_counter
CMD ["/usr/local/bin/time_counter"]
