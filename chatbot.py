#chatbot implementation
#using pre trained LLM (GPT2 medium from Hugging Face)
import random
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2-medium')
set_seed(42)
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)

[{'generated_text': "Hello, I'm a language model, I'm a language. I'm a compiler, I'm a parser, I'm a server process. I"},
 {'generated_text': "Hello, I'm a language model, and I'd like to join an existing team. What can I do to get started?\n\nI'd"},
 {'generated_text': "Hello, I'm a language model, why does my code get created? Can't I just copy it? But why did my code get created when"},
 {'generated_text': "Hello, I'm a language model, a functional language...\n\nI'm a functional language. Is it hard? A little, yes. But"},
 {'generated_text': "Hello, I'm a language model, not an object model.\n\nIn a nutshell, I need to give me objects from which I can get"}]

#to get the features of a given text from pyTorch
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2Model.from_pretrained('gpt2-medium')
text = "Hello"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

responses = {"hello": ["Hi there!", "Hello!", "Greetings!"],
             "How are you?": ["I'm doing well, thank you!", "I'm fine, and you?"],
             "goodbye": ["Goodbye!", "See you later!", "Take care!"]
             }
#store a few recent exchanges to keep the convo coherent
#allow users to adjust response behavior usig settings like:
max_length
temperture


chart = model.start_chat()
#keep chatting until user says exit
while True:
  user_input = input('You: ')
  if (user_input.lower() == 'exit'):
    break
  else if user_input.lower() in responses:
    bot_reply = random.choice(responses[user_input.lower()])
    print("Chatbot:", bot_reply)
  else:
    print("Chatbot: I'm sorry, I don't understand that."")
  
  response = chat.send_input(user_input)
  print('Chatbot: ', response.text)

#in TensorFlow
