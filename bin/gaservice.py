import flask
from flask import request, Flask
import json
from summarizer import FindSummary

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def check_api_status():
    '''
    Check if api is working
    
    Returns
    -------
    string- 'Boom! API is working!!'
    
    '''
        
    return 'Boom! API is working!!'

@app.route('/get_summary', methods = ['POST'])
def summarize_app():
    '''
    summarize news article
      
    Parameters
    ----------
    news article loaded through configuration path
          
    Returns
    -------
    summarized news article

    '''
    
    article = json.loads(request.data.decode())['article']
    summary_obj = FindSummary('../config/config2.yaml')
    summary_text = summary_obj.summarize(article)
    return summary_text

@app.route('/about_us', methods = ['POST'])
def dummy_request():
    '''
    check for dummy data
      
    Parameters
    ----------
    string loaded as json
          
    Returns
    -------
    string: 'Ok, request works'

    '''
    jsonStr = request.data.decode()
    dataDict = json.loads(jsonStr)
    article = dataDict['article']
    print('printing data: \n', article)
    return "Ok, request works"

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8080)
