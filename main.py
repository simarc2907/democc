from fastapi import FastAPI

app = FastAPI()

@app.get('/home')#if somebody goes to this url then the below fn is executed
def home():
    return "Hello World!"

@app.get('/about')
def about():
    return "This is the about page"
