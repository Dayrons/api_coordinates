from fastapi import FastAPI
import random

app = FastAPI()


@app.post("/coordinates")
async def root(data: dict):
  
    radio = 0.01
    lng = float(data.get('lng'))
    lat =float(data.get('lat'))

    items = []
    for _ in range(10):
        new_lng = random.uniform(lng - radio, lng + radio)
        new_lat = random.uniform(lat - radio, lat + radio)
        items.append({"lat":new_lat,"lng":new_lng, "index_icon":random.randint(0, 2)})
    
    return {"data":items}