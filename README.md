# FastAPI-Text-Summarizer
This is a simple FastApi application to summarize text


## SETUP
###1. Create a virtual environment:
  - python -m venv env
  - source env/bin/activate  # On Windows use `env\Scripts\activate`

###2.Install dependencies:
  - pip install -r requirements.txt

###3.Run the application:
  - uvicorn main:app --reload

###4.Test the endpoint:
  - Open http://127.0.0.1:8000/notes. 
  - Here we can send post requests to the /summarize endpoint for testing. 
  - The post requests should look like this:
    --{"text" : "text to summarize"}
