from fastapi import FastAPI
import json

path = 'oui.json'
with open(path, mode='r') as json_f:
    oui_dict = json.load(json_f)
    app = FastAPI()

    @app.get('/{oui}')
    async def search_vendor(oui: str):
        return oui_dict[oui] 