FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install nano
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
#RUN pip3 install numpy
#RUN pip3 install flask
RUN mkdir -p /opt/myprojects

COPY document_summarizer /opt/myprojects
#COPY addarray.py /opt/myprojects
WORKDIR /opt/myprojects/document_summarizer

RUN pip3 install -r requirements.txt

CMD ["python3", "bin/gaservice.py"]
