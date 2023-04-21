from fastapi import FastAPI
from config import settings
from fastapi.middleware.cors import CORSMiddleware


if settings.ENABLE_SENTRY:
    import sentry_sdk
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
    )

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("startup")


@app.on_event("shutdown")
async def shutdown():
    print("shutdown")

@app.get("/")
async def test():
    return {"message": "for testing"}


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0