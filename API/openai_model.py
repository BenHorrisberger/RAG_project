import json
import os
from openai import OpenAI
from dotenv import load_dotenv

from API.database import get_connection

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_query(text_input):

    LLM_prompt = f"""
        you are an assistant for an aircraft database,
        the user said: \"{text_input}\",
        extract filters in JSON with keys: total_seats, num_bags, fuel_stop_distance,
        fuel_stop_distance my be any number related to range or miles,
        only include keys you can infer,
        respond with only JSON.
    """

    extraction = client.chat.completions.create(
            model = "gpt-4o",
            messages=[{"role" : "user", "content" : LLM_prompt}],
            response_format={"type" : "json_object"}
    )
    
    try:
        fields = json.loads(extraction.choices[0].message.content)
    except json.JSONDecodeError:
        return {"error" : "Could not parse OpenAI output"}

    return fields
    

