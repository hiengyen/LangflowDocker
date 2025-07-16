from langflow import load_flow_from_json
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Load LangFlow từ file JSON
flow = load_flow_from_json("Financial_Agent.json")

# Định nghĩa endpoint cơ bản


@app.get("/")
async def root():
    return {"message": "LangFlow is running!"}

# Chạy flow (tùy thuộc vào cách bạn muốn tích hợp flow)


@app.get("/run-flow")
async def run_flow():
    result = flow.run()  # Hàm này phụ thuộc vào cách LangFlow xử lý JSON
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
