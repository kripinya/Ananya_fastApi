from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Ananya",
        "sapid": "500125205",
        "Location": "Dehradun"
    }

@app.get("/{data}")
def read_data(data):
    return {"hi": data}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)