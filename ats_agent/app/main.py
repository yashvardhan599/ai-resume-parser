from fastapi import FastAPI
from api.resume import router as resume_router


app = FastAPI(title="AI Resume Parser & Scorer")
app.include_router(resume_router, prefix="/resume")