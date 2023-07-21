from transformers import GPT2Tokenizer

class MaxTokensExceeded(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def tokens_count(text: str) -> int:
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    tokens = tokenizer.encode(text, add_special_tokens=False)

    num_tokens = len(tokens)
    
    return num_tokens

def verify_maxtokens(question: str, max_tokens: int = 450):
    message_token = tokens_count(question)

    if message_token > max_tokens:
        raise MaxTokensExceeded(f"Number of tokens exceeds the maximum limit of {max_tokens}")

