import os
from dotenv import load_dotenv
from openai import OpenAI
from persona import Persona

load_dotenv()

client = OpenAI()

prompt = '''Please answer SUCCINCTLY and DIRECTLY. You are INTERPRETER of:

cat | en-ja-trans --format \'{en.text} → {ja.text} ({ja.en_pronunciation})\'

Example output: hello → こんにちは (kon-ni-chi-wa)'''

persona = Persona(client, prompt)
persona.run(os.getenv('TOKEN'))
