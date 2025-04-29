from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt


def answerchain(model_name):
    # load prompt
    prompt = load_prompt("./prompt/prompt_esg.yml")
    # prompt = hub.pull("teddynote/rag-prompt")

    llm = ChatOpenAI(model_name=model_name, temperature=0)

    rag_chain = prompt | llm | StrOutputParser()

    return rag_chain
