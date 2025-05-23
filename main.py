from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import xiaomin_TTS
from myprompt import myprompt

load_dotenv()

llm = GoogleGenerativeAI(
    google_api_key = getenv("GOOGLE_API_KEY"),
    model = "gemini-2.0-flash",
    temperature = 0.8,
)

myprompt = myprompt()

prompt = ChatPromptTemplate([
    ("system","請在30個字內簡短回答任何我的問題，回覆就只要單純的句子就好不需要加上任何解釋或者額外的格式"),
    ("system",myprompt),
    ("user","{question}")
])
while True:
    q = input("請輸入問題")
    respond = llm.invoke(prompt.format_prompt(question=q))
    print(respond)
    xiaomin_TTS.ai_tts(respond)
