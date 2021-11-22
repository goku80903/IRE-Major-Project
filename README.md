# IRE-Major-Project
## Members (Team 17)
- Koushik Viswanadha - 2018101109
- Sachin Kumar Danishetty - 2018101108
- Kandru Siri Venkata Pavan Kumar - 2021701024
- Suraj Kumar - 2019900038
- Mentor - Shivprasad Sagare 

## Dataset 
The processed dataset for english and silverSENT can be found can be found [here](https://drive.google.com/drive/folders/1AebEqOdTOlkUtB_D0IMOoCpiJPCmc3ww?usp=sharing).

## Directory Structure
The various models proposed are divided into baseline-1(baseline), baseline-2(baseline+) and baseline-3(baseline++)

### Baseline-1
The baseline models consist of the initial experiments where we get to know the task by using genericT5/BART on the task to see the various difficulties in the task. Since, our task consists of converting EnglishwebNLG data to Hindi directly, we shall start with pre-training and fine-tuning for English and further extend this model to Hindi using Machine Translation. <br/>
The directory consists of a single jupyter notebook which has been used for the same. 

### Baseline-2
The baseline+ models consist of using multilingual models and a change of the task from english to hindi.

The directory consists of the following files: 
- mbartPredictions - The predictions obtained when mbart was trained on english to english and tried zero-shot transfer. 
- mt5PredictionsHindi - The predictions obtained when mt5 was trained on english to hindi as proposed. 
- Hindi_translation_code.ipynb/MT.ipynb - The translation codes used for creating the silverSENT dataset. 
- ire_projectmt5.py - Code used for training the mt5 model along with generating the predictions. Note that the predictions should be run with batch_size=1 for each of the dataset and thus, needs to be changed after training and the trained model should be loaded accordingly. 
- t5_wbnlg_eng_to_hindi.py - Initial code written for training the mt5 model with adaGrad and without checking on the evaluation set. 
- webNLG2020_dev_hindi.csv - The dataset file consisting the en-hi dev set. 
- webNLG_Hindi_Final.csv - The dataset file consisting the en-hi train set. 
- mbartInitial.py - The mbart code which was used for zero-shot transfer.

### Baseline-3
Adding to the baseline+ approaches, this approaches take advantage of the multilingual aspect of the multi-lingual models. Training the model on data in more than one language would help in learning and transferring this knowledge into other languages as opposed to fine-tuning on the same data. Thus, we train the mt5model on en-en, en-hi and en-ru which is all of the available data for the given task and evaluate it on hindi. 

The directory structure is as follows: 
- input - The dataset containing the train, dev and test set which included english, hindi and russuian languages. Note that while evaluating, we ignore the english and russian data. 
- predictionsBaseline++ - The predictions obtained when mt5 was trained on the above dataset and evaluated on hindi. 
- ire_projectmt5All.py - Code used for training the mt5 model along with generating the predictions. Note that the predictions should be run with batch_size=1 for each of the dataset and thus, needs to be changed after training and the trained model should be loaded accordingly. 
