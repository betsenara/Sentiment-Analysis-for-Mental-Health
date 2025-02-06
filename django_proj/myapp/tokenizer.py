import re
import torch
from transformers import BertTokenizer
from torch.utils.data import TensorDataset


# Text cleaning function for BERT
def text_clean_for_bert(text):
    if not isinstance(text, str):
        text = str(text)

    text = re.sub(r'\S+@\S+', '', text)  # remove emails
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # remove URLs
    text = re.sub(r'\d+', '', text)  # remove numbers
    # Remove emojis
    emoji_pattern = re.compile("[" 
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # geometric shapes extended
                               u"\U0001F800-\U0001F8FF"  # supplemental arrows
                               u"\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
                               u"\U0001FA00-\U0001FA6F"  # chess symbols
                               u"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"  # Enclosed characters
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    
    return text.strip()

# Clean and Tokenize single text
def clean_and_tokenize_single_text(text, max_len=256):
    """
    Cleans and tokenizes a single text input using BERT tokenizer and returns input IDs and attention mask.
    """
    cleaned_text = text_clean_for_bert(text)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    inputs = tokenizer(
        cleaned_text, 
        padding='max_length', 
        truncation=True, 
        max_length=max_len, 
        return_tensors="pt"
    )

    input_ids = inputs['input_ids'].squeeze(0)  # Remove batch dimension
    attention_mask = inputs['attention_mask'].squeeze(0)
    return input_ids, attention_mask

# Clean and Tokenize dataframes 
def clean_and_tokenize_dataframe(df_column, max_len=256):
    df_bert_clean = df_column.apply(text_clean_for_bert)
    # Load the pre-trained BERT tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    inputs = tokenizer(
        df_bert_clean.tolist(),  
        padding=True, 
        truncation=True, 
        max_length=max_len, 
        return_tensors="pt"
    )

    # Convert labels to long type
    dataset = TensorDataset(inputs['input_ids'], inputs['attention_mask'])
    return dataset



