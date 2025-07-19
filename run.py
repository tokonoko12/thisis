from fastapi import FastAPI
from mediaflow_proxy.main import app as mediaflow_app  # Import mediaflow app
from fastapi.middleware.cors import CORSMiddleware
import httpx
import re
import string

# Initialize the main FastAPI application
main_app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Manually add only non-static routes from mediaflow_app
for route in mediaflow_app.routes:
    if route.path != "/":  # Exclude the static file path
        main_app.router.routes.append(route)

# Run the main app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=8080)
