Instructions on how to run and customize the chatbot.

Using a pre-trained model gpt2-medium from hugging face:

This model was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token i only uses the inputs from 1 to i but not the future tokens.

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility.

HOW TO RUN:

***Conversing with chat might be slow and contain warnings about truncation and tokenization that can be ignored -they are not cover by the gpt2-medium model

1) You must input this command into your terminal to use the transformers module: pip install transformers torch

2) I recommend running it with the command: python chatbot.py instead of hitting the play button as that might say the transformers module is not found.

4) Before you start to chat, you will be prompted with an option to change the maximum response length and the temperature of the model. So, how long can you the responses be (default is 80) and how advanced can they be (from 0.1 - 1.0 being the most advanced/creative, default is 0.2). Max_length variable contains tokens that chat reads, not quite full words. Defaults are used when you do not enter anything.

5) You will be prompted with a "You: " and you must enter what you want to say, common responses include "Hi, how are you?", "Hello", "What's up?", etc. Keeping it simple.

5) Chatbot will respond simply and the most recent few responses will be recorded to keep the conversation coherent.

6) To stop chatting, say "exit".
