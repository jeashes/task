from fastapi import FastAPI, Request, Body, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
import os

from core.core import set_question

from models.models import MessageData

load_dotenv() 

API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-KEY-Token")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key == API_KEY:
        return True
    else:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.post("/api/send")
async def send_message(request: Request, data: MessageData = Body(...), is_valid_key: bool = Depends(verify_api_key)):
    
    message = data.message

    answer = 'Hello I am NiftyBridge AI assistant. How could I help you?'

    if message != 'Hello':
        answer = set_question(message) 
        
    response_data = {
        "message": answer
    }
    return JSONResponse(content=response_data)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
