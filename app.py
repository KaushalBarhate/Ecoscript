# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from interpreter import EcoScriptInterpreter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow any origin
    allow_credentials=True,
    allow_methods=["*"], # Allow any method
    allow_headers=["*"], # Allow any header
)

class CodeRequest(BaseModel):
    code: str

@app.post("/compile/")
async def compile_ecoscript(request: CodeRequest):
    code = request.code
    interpreter = EcoScriptInterpreter()
    output = interpreter.interpret(code)
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
