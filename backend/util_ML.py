from transformers import AutoTokenizer
from peft import AutoPeftModelForSeq2SeqLM
from newspaper import Article
import os

# You can also do export KMP_DUPLICATE_LIB_OK=True on terminal
# Only on mac os
# os.environ["KMP_DUPLICATE_LIB_OK"]="True"

# Model Id and Token Id used
model_id = "../backend/Flan-T5-Small_Lora"
token_id  = "google/flan-t5-small"

# Load model and tokenizer
model = AutoPeftModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(token_id)


def get_article(link):
   #For different language newspaper refer above table
   toi_article = Article(link, language="en") # en for English
   
   #To download the article
   toi_article.download()

   #To parse the article
   toi_article.parse()

   # Get Summary
   article = toi_article.text

   return article


def get_summary(input_text):
   # Tokenize input text
   tokens_input = tokenizer.encode("Summarize: "+ input_text, return_tensors='pt',
                                   max_length=tokenizer.model_max_length,
                                   truncation=True)

   # Generate summary
   summary_ids = model.generate(input_ids=tokens_input,
                                min_length=80,
                                max_length=150,
                                length_penalty=20, 
                                num_beams=2)

   # Decode and print the summary
   summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

   return summary