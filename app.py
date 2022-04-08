
from django.shortcuts import redirect
from flask import Flask, request, render_template, redirect
import speech_recognition as sr




app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript=""
    if request.method =='POST':
         print("आप की file हमें  Recive हो गई है और हुमने काम शुरू कर दिया है ।  जय हिन्द साहब 💂‍♀️👨‍✈️")

         if "file" not in request.files:
             return redirect(request.url)

         file = request.files["file"]
         if file.filename == "":
            return redirect(request.url)

         if file:
             recognizer = sr.Recognizer()
             audioFile = sr.AudioFile(file)
             with audioFile as source:
                 data = recognizer.record(source)
             transcript = recognizer.recognize_google(data, key = None)
             print(transcript)
             


    return render_template('index.html', transcript = transcript )

    
if __name__ =="__main__":
    app.run(debug=True)

