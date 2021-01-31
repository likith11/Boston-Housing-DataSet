FROM python:3.9.1-buster

WORKDIR /boston-housing-predictor

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy source code
COPY  . /boston-housing-predictor

# Application launch
CMD ["python", "server.py"]