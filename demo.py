import streamlit as st
import numpy as np
import pandas as pd
from googletrans import Translator

# st.title("Classification of Iris Species")
# st.markdown('**Objective** : Given details about the flower we try to predict the species.')
# st.markdown('The model can predict if it belongs to the following three Categories : **setosa, versicolor, virginica** ')

from transformers import T5Tokenizer, MT5ForConditionalGeneration
import torch
from torch import optim
import pandas as pd
import numpy as np

"# Generating Natural Language Text from RDF"
def get_model(language,model_chosen):
  filepath="/content/t5/model" if language=='English' else "/content/best_modelClipped"\
  if model_chosen=='mT5' else "/content/best_modelbaseline++" if model_chosen =='mT5 multilingual'\
  else "/content/t5/model"
  tokenizer_path = filepath if filepath=='/content/t5/model' else '/content/mt5/model'
  tokenizer = T5Tokenizer.from_pretrained(tokenizer_path)

  model = MT5ForConditionalGeneration.from_pretrained(filepath)

  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  model.to(device)
  return tokenizer,model,device



def get_text(inp,tokenizer,model,device):
    with torch.no_grad():

        otp_texts=[]
        
        test_input_ids = tokenizer([inp],padding='longest',
                      max_length=100,
                      truncation=True,
                      return_tensors="pt")
        test_input_ids = test_input_ids.to(device)
        test_outputs = model.generate(**test_input_ids,)
        test_outputs = test_outputs.to(torch.device('cpu'))
        otp_texts = [tokenizer.decode(i, skip_special_tokens=True) for i in test_outputs]
        return otp_texts[0]
prev_lang = ''
def generate(language,model_chosen):
    st.write('Generating text in ',language)
    tokenizer,model,device = get_model(language,model_chosen)
    if language=='Hindi':
      inp ='translate English to Hindi:'
    else:
      inp ='translate English to English:'
    for string in [first_tuple,second_tuple,third_tuple,fouth_tuple]:
      if len(string)<=2:
        continue
      s,r,o=string.split('|')
      inp+=' <S> '+s
      inp+=' <R> '+r
      inp+=' <O> '+o
    otp = get_text(inp,tokenizer,model,device)
    if language=='Hindi' and model_chosen =='T5':
      translator=Translator()
      if not isinstance(str,otp):
        return 
      otp = translator.translate(otp, src='en',dest='hi').text
    st.write(otp)
   
language = st.selectbox(
    'Choose the target language',
    ('English', 'Hindi',))
model_chosen = st.selectbox(
    'Choose the model',
    ('mT5', 'T5','mT5 multilingual'))
st.markdown("**Please enter the rdf data**")
first_tuple = st.text_input('Enter a triple <subject | relation | object>', '',key =1)
second_tuple = st.text_input('Enter a triple <subject | relation | object>', '',key =2)
third_tuple = st.text_input('Enter a triple <subject | relation | object>', '',key =3)
fouth_tuple = st.text_input('Enter a triple <subject | relation | object>', '',key =4)

if st.button("Generate Text"):
    generate(language,model_chosen)
