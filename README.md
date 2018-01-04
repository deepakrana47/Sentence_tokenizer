# Fullstop_predictor

This is a simple sentence tokenizer that uses neural network for pridecting whether a given dot is end of sentence or not.

Usages:

  To train the neural network for a given text:
  
    $ python nn_git filename
   
  To use the sentence tokenizer in your code:
  
  Add Following files to your code directory:
    
    -weights.pickle
    -sentence_tokenization.py
    
  Add these lines to top of code:
  
    from sentence_tokenization.py import nn_sent_tokenizer
  
  Then to tokenize the text use:
    
    lines = nn_sent_tokenizer(text)
      
      text: is the input text for sentence tokenization
      
      lines: ouput sentence of text in list form.
    
