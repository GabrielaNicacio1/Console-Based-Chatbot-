Console-Based-Chatbot

Instructions on how to run and customize the chatbot.


This model was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token i only uses the inputs from 1 to i but not the future tokens.

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility.

can customize max_length and temperature..
