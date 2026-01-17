from core.llm import llm
from agent_graph.state import ResumeState

from agent_graph.prompts import RESUME_PARSER_PROMPT, JD_MATCH_PROMPT, SCORER_PROMPT, EXPLANATION_PROMPT
from agent_graph.runnable_schema import resume_parser_llm, jd_matcher_llm, scorer_llm


def resume_parser_node(state: ResumeState) -> ResumeState:
    result = resume_parser_llm.invoke(
        RESUME_PARSER_PROMPT.format(
            resume_text=state["resume_text"]
        )
    )
    return {"parsed_resume": result.model_dump()}

def jd_matcher_node(state: ResumeState) -> ResumeState:
    result = jd_matcher_llm.invoke(
        JD_MATCH_PROMPT.format(
            resume=state["parsed_resume"],
            jd=state["jd_text"]
        )
    )
    return {"jd_match": result.model_dump()}

def scorer_node(state: ResumeState) -> ResumeState:
    result = scorer_llm.invoke(
        SCORER_PROMPT.format(jd_match=state["jd_match"])
    )
    return {"score": result.model_dump()}

def explanation_node(state: ResumeState) -> ResumeState:
    response = llm.invoke(
        EXPLANATION_PROMPT.format(
            parsed_resume=state["parsed_resume"],
            jd_match=state["jd_match"],
            score=state["score"]
        )
    )
    return {"explanation": response.content}

