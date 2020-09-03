import re

class PreprocessText:
    
    '''
    
    Preprocess news articles fed from files
    
    '''
    
    def __init__(self):
        pass
    
    def convert_to_lower(self, text):
        '''
        Convert text to lowercase

        Parameters
        ----------
        text : string
            text from news article

        Returns
        -------
        lowered_text : string
            lower case characters.

        '''
        
        lowered_text = text.lower()
        return lowered_text
    
    
    def remove_special_character(self, text):
        '''
        remove special characters from text

        Parameters
        ----------
        text : string
            text from news article

        Returns
        -------
        processed_text : string
            text without special characters
        '''
        
        processed_text = re.sub(',|;|:|<|>|', '', text)
        return processed_text
    
    

    
