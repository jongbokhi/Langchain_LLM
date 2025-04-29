from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def queryrewriter(model_name):
    # initialize LLM
    llm = ChatOpenAI(model=model_name, temperature=0)

    # set prompt
    system = """You a question re-writer that converts an input question to a better version that is optimized \n 
    for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""

    # Query Rewriter prompt template
    rewrite_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "Here is the initial question: \n\n {question} \n Formulate an improved question.",
            ),
        ]
    )

    # Build Query Rewriter
    question_rewriter = rewrite_prompt | llm | StrOutputParser()

    return question_rewriter