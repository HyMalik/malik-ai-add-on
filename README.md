# Scene Generation API

This API generates random 3D scenes based on a text prompt. It provides objects, lighting, and camera configurations.

## Running the API Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the FastAPI server:
    ```bash
    uvicorn scene_generator:app --reload
    ```

The API will be available at `http://127.0.0.1:8000/`.

## Deploying on Heroku

1. Create a Heroku app:
    ```bash
    heroku create your-app-name
    ```

2. Push the code to Heroku:
    ```bash
    git push heroku master
    ```

Your app will be available at `https://malik-ai-add-on.herokuapp.com/`.
