# ENAC-IT4R Homework Full Stack

## Setup

### Prerequisites

- [Make](https://www.gnu.org/software/make/)
- [Node.js](https://nodejs.org/) 18.x
- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/) 3.10

### Installation

```bash
make install
```

### Development Run

```bash
make dev-backend
# http://127.0.0.1:8000

make dev-frontend
# http://127.0.0.1:5173
```

## Exercise

### Context

Our researchers have just provided us with a dataset that consists of demographic information. The dataset can be found at the location `dataset/canton.csv`.

### Objectives

As the researchers are not proficient in IT development, they have tasked you with creating a web application to display a single chart.
Here are the initial requirements :

- Users should be able to select a canton.
- Chart should show proportion of women and men in the selected canton (with a [doughnut chart](https://echarts.apache.org/examples/en/editor.html?c=pie-doughnut) for instance).

### Tasks

1. The backend should read the dataset and publish the data through a REST API using [FastAPI](https://fastapi.tiangolo.com/)
   1. Backend API documentation: http://127.0.0.1:8000/docs
   2. Some examples of API definition are in `backend/homework_fullstack/main.py`
2. The frontend should fetch the data from the API and draw a chart
   1. Use a chart library ([ECharts](https://echarts.apache.org/en/index.html) is recommended)
   2. A component has already been bootstraped in `frontend/src/components/GenderChart.vue`
3. Bonus: Dockerize the application to be able to run everything using `docker-compose up`

### Delivery

1. Fork the repository
2. Do your commits
3. Create a pull request back to the original repository
