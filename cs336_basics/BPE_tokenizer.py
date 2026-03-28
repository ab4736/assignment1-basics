import regex as re
from typing import Tuple


def BPE_train(input_path: str, vocab_size: int, special_tokens: list[str]) -> tuple[dict[int[bytes]], list[tuple[bytes, bytes]]]:
    with open(input_path, "r") as file:
        full_text = file.read()
    
    vocab = dict()
    merges = list()

    # First step, we want to split based on the special tokens
    split_full_text = re.split()

    


"<|endoftext|>"