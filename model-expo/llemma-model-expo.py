from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def solve_math_problem(question):

    model_name = "openlm-research/open-llm-math-7b"  # Replace with the actual model if needed
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)


    inputs = tokenizer(question, return_tensors="pt")


    outputs = model.generate(**inputs, max_length=256, temperature=0.7)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer
