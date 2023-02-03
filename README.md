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

We just get the dataset from our researcher and we are asked to display some charts in a web application.

1. The dataset is located in `dataset/canton.csv`
2. The backend should read the dataset and publish the data through a REST API using [FastAPI](https://fastapi.tiangolo.com/)
   1. Backend API documentation: http://127.0.0.1:8000/docs
   2. Some examples of API definition are in `backend/homework_fullstack/main.py`
3. The frontend should fetch the data from the API and draw a chart
   1. Use a chart library ([ECharts](https://echarts.apache.org/en/index.html) is recommanded)
   2. The user should be able to select a canton
   3. The chart should show proportion of women and men in the selected canton (with a [doughnut chart](https://echarts.apache.org/examples/en/editor.html?c=pie-doughnut) for instance)
   4. A component has already been bootstraped in `frontend/src/components/GenderChart.vue`
4. Bonus: Dockerize the application to be able to run everything using `docker-compose up`
