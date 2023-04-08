import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.schema import Document
from langchain.document_loaders import HNLoader
from langchain.llms import OpenAI
from langchain import PromptTemplate

chat = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))
loader = HNLoader("https://news.ycombinator.com/item?id=35484594")
data = loader.load()
# TODO: Find out how to use this

# Seems that selectors are like table driven tests

def travel_prompt(location):
    prompt = PromptTemplate(
        input_variables=["location"],
        template="""
        I really want to travel to {location}. What should I do there?

        Respond in one short sentence
        """,
    )
    return prompt.format(location=location)


def main():
    llm = OpenAI(
        model_name="text-davinci-003", openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    final_prompt = travel_prompt("New York")
    print(f"Final Prompt: {final_prompt}")
    print("-----------")
    print(f"LLM Output: {llm(final_prompt)}")
    exit()

    print(chat([HumanMessage(content="Hello")]))
    print(chat([HumanMessage(content="How are you?")]))
    print(chat([HumanMessage(content="What's your name?")]))
    print(chat([HumanMessage(content="Heads or tails?")]))
    print(
        chat(
            [
                HumanMessage(
                    content="Translate this sentence from English to French. I love programming."
                )
            ]
        )
    )
    print(
        chat(
            [
                SystemMessage(
                    content="You are an unhelpful AI bot that makes a joke at whatever the user says"
                ),
                HumanMessage(
                    content="I would like to go to New York, how should I do this?"
                ),
            ]
        )
    )

    Document(
        page_content="This is my document. It is full of text that I've gathered from other places",
        metadata={
            "my_document_id": 234234,
            "my_document_source": "The LangChain Papers",
            "my_document_create_time": 1680013019,
        },
    )


if __name__ == "__main__":
    main()
