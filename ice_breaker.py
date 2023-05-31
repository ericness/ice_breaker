from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from agents import linkedin_lookup_agent
from third_parties import linkedin

if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        give the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_url = linkedin_lookup_agent.get_profile_url("Eric Ness")
    print(linkedin_url)
    linkedin_response = linkedin.script_linkedin_profile(linkedin_url)
    print(chain.run(information=linkedin_response))
