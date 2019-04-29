FROM archlinux/base
MAINTAINER José Ricardo C. B.
COPY . /var/Ingresse_API_Test
WORKDIR /var/Ingresse_API_Test
RUN pacman -Syyu --noconfirm
RUN pacman -Sy sqlite python python-pipenv python-pip --noconfirm
RUN pip install -r dev-requirements.txt
RUN flask db init 
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT flask run
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000