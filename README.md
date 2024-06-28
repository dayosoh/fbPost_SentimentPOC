# To set up code base

First
pip install -r requirements.txt

---to be continued-----

# How to spin off the Apps
On terminal, spin on the backend
 '''
    export ************************
python3 -m backend.app
 '''

 On terminal, spin on the front end
 ''' python3 -m http.server 8000 '''

 Open the below  URL at anybrowser
 http://localhost:8000

 # Logic 
 This is a zero-shot learning algorithm (starting only) infact it is few-shot learning concept, and this is a continuous learning algoritm that improve from user's data
 Intention to deduce the facebook post on single parameter (label) -> **Sentiment** , the reasoning for sentiment is that over promise / over optimistic can be a form of mis selling.

 1. There is 3 part of prompt that work together System Prompt + User Control Prompt + past Result prompt
 
 A. **System Prompt** : System Prompt"You are a compliance officer that classifies the sentiment of posts." is already embeded into Backend Code as part of the prompt
 
 B. **User Control Prompt**[optional]: Front end User control Promt is optional, if compliance officer or Cynopsis have a specific idea to design the prompt for better classification, it is temporary host on Front end for convenient, can be either on our user's CRM portal or exclusive Cynopsis control console.
 
 C. **Past Result Prompt**: As the result pile up, the prompt will take in previous examples (Latest 10 count) and it's acquired sentiment as example. 