FROM python:3.9.1-buster

WORKDIR /boston_housing

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy source code
COPY  . /boston_housing

# Application launch
CMD ["python", "server.py"]