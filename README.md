# NER Demo
#### By Sean Liu @ UIUC
This code was written in a week so is pretty messy. Sorry! 

## How to run the Chrome extension: 
1. please install the required packages: 
```bash
$ pip install -r ./requirements.txt
```
2. Then, go to chrome://extensions/ and turn on "Developer Mode".
3. Click on "Load unpacked" and select the `ner_extension` folder to import. 
4. At the top right of the browser, there should be a puzzle icon - press it and pin the extension, named **NER Demo Extension**.
5. To download the trained weights for the model, please go to [this link](https://drive.google.com/drive/folders/1Zk0KksUbsHmecJEbVhtGlzHxcLtcIyjd?usp=sharing). Download `best.pt` and place it within `mysite/wiki`. 
6. Open a shell and navigate to `/mysite`. To run the Django backend, run 
```bash
python3 manage.py runserver
```
7. Now, you can start using the extension! Paste any block of text into the textbox and click "Analyze". When the loading finishes, you'll hopefully get the finished material. 

