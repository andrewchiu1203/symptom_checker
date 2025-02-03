Symptom Checker
-------------------------

This webapp uses the GPT2 model from Pytorch that's fined-tuned by a medical datasets to predict the user's sickness based on their description of symptoms.
The user interface is made by Django. In views.py, the file that handles user views, it links to the LLM model and pass in symptom descriptions for inferencing.

### Datasets

- Sympton description datasets <br>
  https://huggingface.co/datasets/duxprajapati/symptom-disease-dataset

### Dependancies
- python 3.11
- pytorch
- transformer
- django
