# Boston_Housing_DataSet - MEDV predictor.

This repo contains files to code that deploys an API endpoint for a user to predict Median value of owner-occupied homes in $1000s (MEDV). The model was trained on the Boston Housing Dataset.

## ` Build and retrain the model.`

A notebook with steps about building, training and running the model is provided with steps shown.

```console
Boston_Housing_Model_Building.ipynb
```

Please open the notebook shown above and run through the steps.

## `Directory Structure`

The directory structure is provided below.

```console
.
├── Boston_Housing_Model_Building.ipynb
├── Dockerfile
├── HousingData_test.csv
├── HousingData_train.csv
├── LICENSE
├── README.md
├── knn_imputer.joblib
├── requirements.txt
├── server.py
├── templates
│   ├── base.html
│   ├── index.html
│   └── output.html
└── xg_regressor.joblib

```

## `Build steps:`

Listed below are different ways to build and run the system. There are a total of 3 ways to build and run the system. They are:

1. Build from the git repo.
2. Build using docker image.

---

## 1. Build from the git repo.

- Clone the project Git repo.
  ```console
  foo@bar:~$ git clone https://github.com/likith11/Boston-Housing-DataSet-Predictor.git
  ```
- Move into the project directory.
  ```console
  foo@bar:~$ cd Boston-Housing-DataSet-Predictor
  ```
- Create a virtual environment and activate it.

  ```console
  foo@bar:~$ python3 -m venv
  foo@bar:~$ source venv/bin/activate
  ```

- Install requirements from requirements.txt
  ```console
  (venv) foo@bar:~$ pip install -r requirements.txt
  ```
  &nbsp;

---

&nbsp;

## 2.) Pull from Docker Hub / Build Docker Image Locally:

### 2.1) Build using docker image.

&nbsp;

- Pull image from docker hub.
  ```console
  foo@bar:~$ docker pull likithponnanna/boston-housing-predictor
  ```
- Run the image that was pulled. Below port 5000 is mapped between the external and docker container.
  ```console
  foo@bar:~$ docker run -p 5000:5000 boston-housing-predictor
  ```

> - NOTE : To run the server follow the steps mentioned in section **1.2** API Call.

&nbsp;
&nbsp;

### 2.2 Build from docker hub locally using the DockerFile provided:

- To build the docker image using the dockerfile locally run the following command before initiating docker run.
  ```console
  foo@bar:~$ git clone https://github.com/likith11/Boston-Housing-DataSet-Predictor.git
  foo@bar:~$ cd Boston-Housing-DataSet-Predictor
  foo@bar:~$ docker build -t boston-housing-predictor .
  ```
- Run the docker image with port specified.
  ```console
  foo@bar:~$ docker run -p 5000:5000 boston-housing-predictor
  ```

---

&nbsp;
&nbsp;

### `Steps To RUN the web server:`

1. To run locally.
2. To run the docker image.

### 1.) To run locally using py file.

```console
(venv) foo@bar:~$ python server.py
```

### 2.) To run the docker image.

> Run the docker image with port specified.

```console
   foo@bar:~$ docker run -p 5000:5000 boston-housing-predictor
```

### `Navigate through the web deployment:`

> There are 2 ways of using the web deployment.

1. Using GUI
2. Using API call

> 1.) Using GUI:
>
> - Navigate to [http://0.0.0.0:5000/](http://0.0.0.0:5000/) or [http://localhost:5000/](http://localhost:5000/) (Replace port number if its a different port on your machine. The default port above is 5000).
> - Two text fields with pre-filled test data along with a blue _Process_ button is displayed.
> - Change the input field to the required test input.
> - Click on \_Process\_\_
> - A new screen with Translucent alert box is shown with the corresponding MEDV predicted.
> - Click on _Retry?_ button to go back to the main screen and repeat the process.

> 2.)Using API call:
>
> - API end point is deployed at [http://0.0.0.0:5000/api/predict](http://0.0.0.0:5000/api/predict) where POST request is accepted.
> - The API accepts text inputs in the JSON format shown below
>
> ```json
> {
>   "CRIM": 9.39063,
>   "ZN": 0.0,
>   "INDUS": 18.1,
>   "CHAS": 0,
>   "NOX": 0.74,
>   "RM": 5.627,
>   "AGE": 93.9,
>   "DIS": 1.8172,
>   "RAD": 24.0,
>   "TAX": 666.0,
>   "PTRATIO": 20.2,
>   "B": 396.9,
>   "LSTAT": 22.88
> }
> ```

> - An example _curl_ command is

```console
curl -d '{ "CRIM"  : 9.39063,  "ZN"    : 0.0,  "INDUS" : 18.1, "CHAS"  : 0, "NOX"    : 0.740,   "RM"    : 5.627,  "AGE"   : 93.9, "DIS"   : 1.8172, "RAD"   : 24.0, "TAX"  : 666.0, "PTRATIO":20.2, "B"     : 396.90, "LSTAT" : 22.880 }' -H 'Content-Type: application/json' http://0.0.0.0:5000/api/predict
```

- An API response json is returned with the the predicted MEDV value.

&nbsp;

---
