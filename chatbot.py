#chatbot implementation
#using pre trained LLM (GPT2 medium from Hugging Face)
#import random
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2-medium')
set_seed(42)
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)

[{'generated_text': "Hello, I'm a language model, I'm a language. I'm a compiler, I'm a parser, I'm a server process. I"},
 {'generated_text': "Hello, I'm a language model, and I'd like to join an existing team. What can I do to get started?\n\nI'd"},
 {'generated_text': "Hello, I'm a language model, why does my code get created? Can't I just copy it? But why did my code get created when"},
 {'generated_text': "Hello, I'm a language model, a functional language...\n\nI'm a functional language. Is it hard? A little, yes. But"},
 {'generated_text': "Hello, I'm a language model, not an object model.\n\nIn a nutshell, I need to give me objects from which I can get"}]

#store a few recent exchanges to keep the convo coherent
recent_exchanges = []

#allow users to adjust response behavior usig settings like max length and setting
# temp is how creative/advanced the models responses are. Range from 0.1 - 1.0 (lowest is less creative)
max_length = int (input("Enter max response length") or 80) #if they dont give one then default 80
temperature = float(input("Enter how creative/advanced you would like chatbot to be (range 0.1-1.0): ") or 0.2)

while True:
  user_input = input("You: ")
  if (user_input.lower() == "exit"): #keep chatting until user says exit
    break
  #add their response to array of history
  recent_exchanges.append(f"You: {user_input}")
  recent_exchanges = recent_exchanges[-3:] #keep most recent 3
  chat_prompt = "\n".join(recent_exchanges) + "\nChatbot:"
  #storing in array should look like this 
  #{You: Hello, Chatbot: Hi I'm a chatbot!, You: Bye}

  #chat prompt has recent exchanges and prompt to help generate response all in one string tho
  response = generator(chat_prompt, max_length = max_length, temperature = temperature[0]['generated_text']) #set higher max length ??
  #response has recent exchanges+ its response so need to strip the first part for just the answer
  answer = response[len(chat_prompt):].strip().split("\n")[0]
  
  print("Chatbot: ", answer)
  recent_exchanges.append(f"Chatbot: {answer}")

  #else:
   # print("Chatbot: I'm sorry, I don't understand that.")
