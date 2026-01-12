from fastapi import APIRouter, UploadFile, File, Form
from agent_graph.graph import build_resume_graph
from utils.file_parser import extract_resume_text

router = APIRouter()
workflow = build_resume_graph()


@router.post("/parse-and-score")
async def parse_and_score_resume(
    resume: UploadFile = File(...),
    jd_text: str = Form(...)
):
    file_bytes = await resume.read()
    resume_text = extract_resume_text(resume.filename, file_bytes)

    result = workflow.invoke({
        "resume_text": resume_text,
        "jd_text": jd_text
    })

    return result
