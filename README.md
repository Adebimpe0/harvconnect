# HarvConnect Matching API

A geolocation-based market matching API for HarvConnect — a farmer-to-buyer digital marketplace for Ghana's smallholder vegetable farmers.

Built for the GDSS-PSInno AgriTech Innovation Challenge 2026.

## Live API
https://harvconnect-production.up.railway.app

## Endpoints

### Health Check
GET /health
Response: {"status": "ok"}

### Get Available Commodities
GET /commodities
Response: {"commodities": ["Tomatoes (local)", "Peppers (fresh)", ...]}

### Find Nearest Markets
GET /match?lat={latitude}&lon={longitude}&commodity={commodity_name}&top_n=5

Parameters:
- lat: buyer latitude (float)
- lon: buyer longitude (float)
- commodity: produce name (string)
- top_n: number of results to return (int, default 5)

Example:
/match?lat=5.55&lon=-0.22&commodity=Tomatoes (local)

Response:
{"matches": [{"market": "Accra", "region": "GREATER ACCRA", "commodity": "Tomatoes (local)", "price_per_kg_ghs": 3.09, "distance_km": 0.0}]}

## Data Source
WFP Ghana Food Prices Dataset (2006-2023)
- 39,038 records
- 19 markets across Ghana
- 6 vegetable commodities: Tomatoes (local), Tomatoes (navrongo), Peppers (fresh), Peppers (dried), Eggplants, Onions

## Tech Stack
- Python
- FastAPI
- Pandas
- Deployed on Railway
