FROM ubuntu
# update and install redis server
RUN apt-get update -y
RUN apt-get install redis-server -y
RUN apt-get install python ruby -y

#install vim
RUN apt-get install vim -y

##copy main.py and compl1.rb files from host to container 
WORKDIR /data/
COPY main.py  /data/main.py
COPY compl1.rb  /data/compl1.rb
COPY get-pip.py /data/get-pip.py

## change settings for localhost to anywhere
##sed -e sed s/127.0.0.1/0.0.0.0/g

## Run pip and install redis
RUN python get-pip.py
RUN pip install redis

## install ruby gem redis
RUN gem install redis

# Run redis server
CMD ["redis-server", "/etc/redis/redis.conf"]

# Open redis port 
EXPOSE 6379



