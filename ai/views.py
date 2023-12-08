from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.python.keras.optimizer_v2 import adam

import sqlite3
import mysql.connector

 
  


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sentimentanalasis(request):
     if request.method == 'POST':
        val1 = request.POST['num1'] # Use get() to avoid MultiValueDictKeyError

   
        # Rest of your view logic
        custom_optimizer = adam.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-7, amsgrad=False)

# Load the model with the custom optimizer
        loaded_model = load_model('moviereviews3.h5', custom_objects={'Adam': custom_optimizer}, compile=False)
        mydb = mysql.connector.connect(
  host ="192.168.55.104",
  user ="Samanth",
  passwd ="Samanth12@",
  database="movies"
)
 
        sentiment = ['Neutral','Negative','Positive']
        s=[]
        sequence = Tokenizer().texts_to_sequences(val1)
        test = pad_sequences(sequence, maxlen=500)
        sentiment[np.around(loaded_model.predict(test), decimals=0).argmax(axis=1)[0]]
        res=loaded_model.predict(test)
        pred=res[0]
        sentiment = 'Negative' if pred < 0.5 else 'Positive'
            
        mycursor = mydb.cursor()
        sql_insert_data = "INSERT INTO predictions (results_of_predicted_sentiments) VALUES (%s)"
# Execute the INSERT statement with the value of 'pred'
        # Execute the INSERT statement with the value of 'pred'
        # Execute the INSERT statement with the value of 'pred'
        mycursor.execute(sql_insert_data, (float(pred),))



# Commit the changes to the database
        mydb.commit()

# Close the cursor and connection
        mycursor.close()
        mydb.close()

# Execute the INSERT statement with the value of 'pred'
        
    
        return render(request, "result.html", {'result': pred,'state': sentiment})
     

     else:
        # Handle the case when the view is accessed with a GET request
        return HttpResponse("Method Not Allowed", status=405)
    