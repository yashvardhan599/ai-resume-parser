from langgraph.graph import StateGraph, END
from agent_graph.state import ResumeState
from agent_graph.nodes import resume_parser_node, jd_matcher_node, scorer_node, explanation_node


def build_resume_graph():
    graph = StateGraph(ResumeState)


    graph.add_node("resume_parser", resume_parser_node)
    graph.add_node("jd_matcher", jd_matcher_node)
    graph.add_node("scorer", scorer_node)
    graph.add_node("explanation", explanation_node)


    graph.set_entry_point("resume_parser")
    graph.add_edge("resume_parser", "jd_matcher")
    graph.add_edge("jd_matcher", "scorer")
    graph.add_edge("scorer", "explanation")
    graph.add_edge("explanation", END)


    return graph.compile()