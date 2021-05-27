# ML-Deployment 📦
A simple example of deploying machine learning/deep learning applications. 



## Tech Stack
In this example, 
*  A **PyTorch**-based object detector is built
*  Served using **Flask** Endpoints
*  The tasks are queued and called asynchronous with **Celery**
*  The Job history and the results are saved in **MongoDB**
*  Deployed using **Docker** and **Docker-Compose**
## Requirements
* Docker
* docker-compose
* nvidia-docker2

## Installation
Build the docker image:
```
docker-compose build
```
Start and attach to the docker-compose services:
```
docker-compose up
```
## Endpoints
- Start a Job : `POST /api/v1/jobs`

      curl -X POST -H "Content-Type: application/json" -d '{"url":"http://ai.stanford.edu/~jkrause/cars/car2.jpg"}' http://127.0.0.1:5000/api/v1/jobs

    Response:
    ```json
    {
        "id": "60ad59866dc08443a331a030", 
        "result": [],
        "source": "http://ai.stanford.edu/~jkrause/cars/car2.jpg", 
        "state": "Initialized", 
        "time_created": "2021-05-25 20:09:42.542180"
    }

    ```

- Get all Jobs : `GET /api/v1/jobs`

      curl -X GET http://127.0.0.1:5000/api/v1/jobs

    Response:
    ```json
    [
         {
            "id": "60ac55a79d86cb024078a112", 
            "result": [
            {
                "box": {
                    "x1": 0.04, 
                    "x2": 0.54, 
                    "y1": 0.55, 
                    "y2": 0.96
                }, 
                "label": "cat", 
                "score": 0.91
            }, 
            {
                "box": {
                    "x1": 0.62, 
                    "x2": 0.82, 
                    "y1": 0.65, 
                    "y2": 0.99
                }, 
                "label": "person", 
                "score": 0.8
            }, 
            {
                "box": {
                    "x1": 0.09, 
                    "x2": 0.14, 
                    "y1": 0.14, 
                    "y2": 0.28
                }, 
                "label": "person", 
                "score": 0.8
            }, 
            {
                "box": {
                    "x1": 0.8, 
                    "x2": 0.95, 
                    "y1": 0.59, 
                    "y2": 0.99
                }, 
                "label": "person", 
                "score": 0.8
            }, 
            {
                "box": {
                    "x1": 0.14, 
                    "x2": 0.45, 
                    "y1": 0.16, 
                    "y2": 0.4
                }, 
                "label": "car", 
                "score": 0.72
            }, 
            {
                "box": {
                    "x1": 0.43, 
                    "x2": 0.52, 
                    "y1": 0.16, 
                    "y2": 0.25
                }, 
                "label": "truck", 
                "score": 0.65
            }, 
            {
                "box": {
                    "x1": 0.34, 
                    "x2": 0.38, 
                    "y1": 0.14, 
                    "y2": 0.23
                }, 
                "label": "person", 
                "score": 0.65
            }, 
            {
                "box": {
                    "x1": 0.3, 
                    "x2": 0.34, 
                    "y1": 0.15, 
                    "y2": 0.22
                }, 
                "label": "person", 
                "score": 0.62
            }, 
            {
                "box": {
                    "x1": 0.36, 
                    "x2": 0.43, 
                    "y1": 0.16, 
                    "y2": 0.24
                }, 
                "label": "car", 
                "score": 0.57
            }
            ], 
            "source": "https://1.bp.blogspot.com/-yuodfZa6gyM/XlbQfiAzbzI/AAAAAAAAFYA/QSTnuZksQII2PaRON2mqHntZBHL-saniACLcBGAsYHQ/s1600/Figure1.png", 
            "state": "Done", 
            "time_created": "2021-05-25 01:40:55.027000"
        }, 

        {
            "id": "60ad59866dc08443a331a030", 
            "result": [
            {
                "box": {
                    "x1": 0.19, 
                    "x2": 0.73, 
                    "y1": 0.48, 
                    "y2": 0.89
                }, 
                "label": "car", 
                "score": 0.88
            }, 
            {
                "box": {
                    "x1": 0.58, 
                    "x2": 0.62, 
                    "y1": 0.52, 
                    "y2": 0.59
                }, 
                "label": "person", 
                "score": 0.73
            }
            ], 
            "source": "http://ai.stanford.edu/~jkrause/cars/car2.jpg",
            "state": "Done", 
            "time_created": "2021-05-25 20:09:42.542000"
        }
    ]

    ```
- Get a single Job : `GET /api/v1/jobs/<job_id>`

      curl -X GET http://127.0.0.1:5000/api/v1/jobs/60ad413cc91fb4916a53315f

    ```json
    {
        "id": "60ad59866dc08443a331a030", 
        "result": [
        {
            "box": {
                "x1": 0.19, 
                "x2": 0.73, 
                "y1": 0.48, 
                "y2": 0.89
            }, 
            "label": "car", 
            "score": 0.88
        }, 
        {
            "box": {
                "x1": 0.58, 
                "x2": 0.62, 
                "y1": 0.52, 
                "y2": 0.59
            }, 
            "label": "person", 
            "score": 0.73
        }
        ], 
        "source": "http://ai.stanford.edu/~jkrause/cars/car2.jpg",
        "state": "Done", 
        "time_created": "2021-05-25 20:09:42.542000"
    }
    ```
