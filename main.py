#Note that as the writing of this, the OpenAI Python library does not support asynchronous operations
import openai
import os

#Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_summary_spanish(text: str) -> str:
    """
    Generates a summary in spanish of the given text using OpenAI API.
    """
    prompt = "translate into spanish and provide a summary of the following text: " + text
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            stop=None,
        )
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API request failed: {e}")
    
    return response.choices[0].text.strip()

def generate_summary_french(text: str) -> str:
    """
    Generates a summary in french of the given text using OpenAI API.
    """
    prompt = "translate into french and provide a summary of the following text: " + text
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            stop=None,
        )
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API request failed: {e}")
    
    return response.choices[0].text.strip()

def generate_summary_german(text: str) -> str:
    """
    Generates a summary in german of the given text using OpenAI API.
    """
    prompt = "translate into german and provide a summary of the following text: " + text
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            stop=None,
        )
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API request failed: {e}")
    
    return response.choices[0].text.strip()

def main():
    try:
        #Note that every run may provide different answers
        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename = "text.txt"
        file_path = os.path.join(current_directory, filename)
        with open(file_path, 'r') as file:
            text_to_summarize = file.read()
        print("Spanish summary")
        summary = generate_summary_spanish(text_to_summarize)
        print(summary)
        print("French summary")
        summary = generate_summary_french(text_to_summarize)
        print(summary)
        print("German summary")
        summary = generate_summary_german(text_to_summarize)
        print(summary)
    except Exception as e:
        print("Exception on main:")
        print(str(e))


if __name__ == "__main__":
    main()
