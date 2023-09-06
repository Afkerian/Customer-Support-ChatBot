import random
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

def response(user_promt):

    model_id = "clibrain/Llama-2-7b-ft-instruct-es"

    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("cuda")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, device=0)

    prompt = user_promt

    result = pipe(prompt)
    print(result[0]['generated_text'])

    return result[0]


