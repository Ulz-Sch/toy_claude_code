import os
import sys
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import SYSTEM_PROMPT
from call_function import available_functions,call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    check_verbose = "--verbose" in sys.argv
    argsys = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    input = " ".join(argsys)
    messages = [
        types.Content(role="user", parts=[types.Part(text=input)]),
    ]
    
    for i in range(20):
        if i == 0:
            response = generate_content(client,check_verbose,messages)
        if not response.function_calls:
            print("="*147)
            print("Response:")
            print(response.text)
            print("="*147)
            sys.exit()
        if i == 19:
            print("Cannot solve this problem. Try again.")
            break
        time.sleep(5)
        response = generate_content(client,check_verbose,messages)
        

def generate_content(client, verbose, messages):    
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=SYSTEM_PROMPT
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config,
    )
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
    if verbose:
        print(f"User prompt: {input}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n\n")
    if response.function_calls:
        print("¨"*147)
        for called_function in response.function_calls:
            print(f"-> Calling function: {called_function.name}({called_function.args})")
            call_result = call_function(called_function)
            if not call_result.parts[0].function_response.response:
                raise Exception("A error has occured during function call.")
            if verbose:
                print(f"-> {call_result.parts[0].function_response.response}")
            messages.append(call_result)
        
    return response
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
    