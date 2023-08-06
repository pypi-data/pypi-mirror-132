FROM python:3.7

# copy app
COPY . /project_name

# define working directory
WORKDIR /project_name

# install python dependencies
RUN pip install -e /project_name --index-url=https://pypi.python.org/simple/

# code obfuscation changes.
RUN python compile.py build_ext --inplace && rm -rf compile.py

# start the app
CMD ["project_name-cli", "gunicorn"]

# define volumes
VOLUME /logs

# expose ports
EXPOSE 5000
