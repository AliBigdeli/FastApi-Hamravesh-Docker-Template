from fastapi import FastAPI
from config import settings


app = FastAPI(
    title="Simple Template Api",
    description="a demonstration of fastapi template project",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ali Bigdeli",
        "url": "https://alibigdeli.github.io/",
        "email": "bigdeli.ali3@gmail.com",
    },
    license_info={"name": "MIT"},
    docs_url="/swagger",
)


@app.on_event("startup")
async def startup():
    print("startup")


@app.on_event("shutdown")
async def shutdown():
    print("shutdown")

@app.get("/")
def test():
    return {"message": "for testing"}
