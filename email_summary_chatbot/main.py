import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain_teddynote.prompts import load_prompt

# API KEY
os.environ["SERPAPI_API_KEY"] = "PUT YOUR SERP API KEY"


class EmailSummary(BaseModel):
    person: str = Field(description="Email sender")
    company: str = Field(description="The sender's company information")
    email: str = Field(description="The sender's email address")
    subject: str = Field(description="Email subject")
    summary: str = Field(description="Summarized text of the email body")
    date: str = Field(
        description="The meeting date and time mentioned in the email body"
    )


# API KEY 정보로드
load_dotenv()

st.title("Email Summary 💬")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.sidebar:
    clear_btn = st.button("Initialize chat")


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_email_parsing_chain():

    output_parser = PydanticOutputParser(pydantic_object=EmailSummary)

    prompt = PromptTemplate.from_template(
        """
        You are a helpful assistant. Please answer the following questions in English.

        #QUESTION:
        Please extract the key takeaways from the following email content.

        #EMAIL CONVERSATION:
        {email_conversation}
        
        #FORMAT:
        {format}
        """
    )

    prompt = prompt.partial(format=output_parser.get_format_instructions())

    chain = prompt | ChatOpenAI(model="gpt-4-turbo") | output_parser

    return chain


def create_report_chain():
    prompt = load_prompt("prompts/email_prompt.yaml", encoding="utf-8")

    output_parser = StrOutputParser()

    chain = prompt | ChatOpenAI(model="gpt-4-turbo") | output_parser

    return chain


if clear_btn:
    st.session_state["messages"] = []

print_messages()

user_input = st.chat_input("Ask questions!")

if user_input:
    st.chat_message("user").write(user_input)

    email_chain = create_email_parsing_chain()

    answer = email_chain.invoke({"email_conversation": user_input})

    params = {"engine": "google", "gl": "us", "hl": "en", "num": "3"}
    search = SerpAPIWrapper(params=params)
    search_query = f"{answer.person} {answer.company} {answer.email}"
    search_result = search.run(search_query)
    search_result = eval(search_result)
    search_result_string = "\n".join(search_result)

    report_chain = create_report_chain()
    report_chain_input = {
        "sender": answer.person,
        "additional_information": search_result_string,
        "company": answer.company,
        "email": answer.email,
        "subject": answer.subject,
        "summary": answer.summary,
        "date": answer.date,
    }

    response = report_chain.stream(report_chain_input)

    with st.chat_message("assistant"):
        container = st.empty()
        ai_answer = ""

        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

    add_message("user", user_input)
    add_message("assistant", ai_answer)
