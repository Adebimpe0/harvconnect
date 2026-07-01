from fastapi import FastAPI
from math import radians, sin, cos, sqrt, atan2
import pandas as pd

app = FastAPI()

ref_prices = pd.read_csv("harvconnect_ref_prices.csv")

def haversine(lat1,lon1,lat2,lon2):
    R=6371
    lat1,lon1,lat2,lon2=map(radians,[lat1,lon1,lat2,lon2])
    dlat=lat2-lat1
    dlon=lon2-lon1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return R*2*atan2(sqrt(a),sqrt(1-a))

def find_nearest_markets(buyer_lat,buyer_lon,commodity,top_n=5):
    df=ref_prices[ref_prices["commodity"]==commodity].copy()
    if df.empty:
        return []
    df["distance_km"]=df.apply(lambda row:haversine(buyer_lat,buyer_lon,row["latitude"],row["longitude"]),axis=1)
    result=df.sort_values("distance_km").head(top_n)
    result["distance_km"]=result["distance_km"].round(1)
    return result[["market","region","commodity","price_per_kg_ghs","distance_km"]].reset_index(drop=True).to_dict(orient="records")

@app.get("/match")
def match(lat:float,lon:float,commodity:str,top_n:int=5):
    results=find_nearest_markets(lat,lon,commodity,top_n)
    if not results:
        return {"error":f"No data found for {commodity}"}
    return {"matches":results}

@app.get("/commodities")
def get_commodities():
    return {"commodities":ref_prices["commodity"].unique().tolist()}
