from transformers import AutoTokenizer
from peft import AutoPeftModelForSeq2SeqLM
from newspaper import Article
import nltk

'''
import os

# You can also do export KMP_DUPLICATE_LIB_OK=True on terminal
# os.environ["KMP_DUPLICATE_LIB_OK"]="True" # Only for MAC OS
'''
# Model Id and Token Id used
model_id = "../backend/Flan-T5-Small_Lora"
token_id  = "google/flan-t5-small"

# Load model and tokenizer
model = AutoPeftModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(token_id)


# Tokenize article
def tokenize(article):
   sentences = nltk.sent_tokenize(article)

   num_tokens = 0 
   paragraph = ''
   for s in sentences:
      # Tokenize each sentence and join it as one string
      words = nltk.word_tokenize(s)
      paragraph += ' '.join(words)
      num_tokens += len(words)

      # Break if there's more than 450 tokens and there's a sentence
      if num_tokens >= 450 and words[-1] == '.':
         break
   
   # Return paragraph
   return paragraph


# Download article and parse through it
def get_article(link):
   #For different language newspaper refer above table
   toi_article = Article(link, language="en") # en for English
   
   #To download the article
   toi_article.download()

   #To parse the article
   toi_article.parse()

   # Get Summary
   article = toi_article.text

   # Get shortened summary
   short_article = tokenize(article)

   return short_article


# Get summary of article
def get_summary(input_text):
   # Tokenize input text
   tokens_input = tokenizer.encode(
      "Summarize: " + input_text,
      return_tensors='pt',
      max_length=tokenizer.model_max_length,
      truncation=True
   )

   # Generate summary
   summary_ids = model.generate(
      input_ids=tokens_input, 
      max_length=150,
      bos_token_id=0
   )

   # Decode and print the summary
   summary = tokenizer.decode(
      summary_ids[0],
      skip_special_tokens=True
   )

   # Return finalized summary
   return summary