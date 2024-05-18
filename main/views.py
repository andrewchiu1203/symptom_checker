from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from transformers import GPT2Tokenizer
import torch

def get_symptom(sickness):
    model = torch.load("C:\Dev\symptom_checker\symptom_lm\SmallMedLM.pt")
    device = torch.device('cuda')
    tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')

    input_str = sickness
    input_ids = tokenizer.encode(input_str, return_tensors = 'pt').to(device)

    output = model.generate(
        input_ids,
        max_length = 40,
        num_return_sequences = 1,
        do_sample = True,
        top_k = 8,
        top_p = 0.95,
        temperature = 0.5,
        repetition_penalty = 1.2,
        pad_token_id = tokenizer.eos_token_id,
    )

    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded_output

def blank(request):
    return redirect(reverse_lazy("main:welcome"))

def index(request):
    if request.method == "POST":
        sickness = request.POST['sickness']

        if sickness == "":
            return render(request, "main/index.html", {
                "result": "Empty string is not allowed",
            })
        
        symptom = get_symptom(sickness)

        return render(request, "main/index.html", {
            "result": symptom,
        })

    return render(request, "main/index.html", {
            "result": None,
        })

def welcome(request):
    return render(request, "main/welcome.html")