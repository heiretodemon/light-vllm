import os
from vllm import LLM,SamplingParams
from transformers import AutoTokenizer

def main():
    path = os.path.expanduser("~/huggingface/Qwen3-0.6B/")
    tokenizer = AutoTokenizer.from_pretrained(path)

if __name__ == "__main__":
    main()