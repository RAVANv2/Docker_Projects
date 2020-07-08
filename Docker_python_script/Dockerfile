# Base Image
FROM python:3

#Add file into container
ADD script.py /

#Install dependencies
RUN pip install pystrich

#Running the python file
CMD ["python", "./script.py"]
