import os
from typing import override

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv(override=True)

llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_API_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0
        )