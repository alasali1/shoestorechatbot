# shoestorechatbot
--Setup
This chatbot is made to run on Windows CMD command line
To run this chatbot on Windows 10 you need to follow these steps in this video.
https://www.youtube.com/watch?v=GlR60CvTh8A.
Afterwards you need to install Spacy using the command "pip install spacy"
Then type in the command "pip install spacy-transformers"
Afterwards you need to install a Spacy pretrained model using the command "python -m spacy download en_core_web_md"

--launch
After setting up your environment all you need to do is go into the project directory in your CMD command line and type "rasa train"
After the training is done loading, you need to open a second CMD command line.
In the first command line run the command "rasa run actions".
In the second command line run "rasa shell". 
You can now interact with the bot in the second command line.
