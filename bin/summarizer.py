import yaml
import numpy as np
from preprocessor import PreprocessText

class FindSummary:
    
    '''
    
    Summarize news articles fed form file
    
    '''
    
    def __init__(self, config_path):
        '''
        Provvide path of file to summarize

        Parameters
        ----------
        text : path of file to summarize
            text from news article

        Returns
        -------
        article_text : file loaded

        '''
        
        with open(config_path, 'r') as fl:
            self.config = yaml.load(fl, Loader = yaml.FullLoader)
            
    def load_data(self):
        '''
        Load file to summarize

        Parameters
        ----------
        data : text from the news article

        Returns
        -------
        article_text : file loaded as news article

        '''
        
        with open(self.config['data']['articles_path'], 'r', encoding = 'utf-8') as fl:
            article_text = fl.read()
        return article_text
    
    def split_sentences(self, text):
        '''
        split article text into sentences

        Parameters
        ----------
        text: text from the news article

        Returns
        -------
        sentences: text split into seperate sentences

        '''
        
        sentences = text.split('.')
        return sentences
    
    def group_sentences(self, sentences):
        '''
        split sentences into two groups - first sentences and rest of the sentences

        Parameters
        ----------
        sentences: sentences split
        
        Returns
        -------
        text1: first sentences
        remaining_text: rest of the sentences

        '''
        
        first_sentence = sentences[0]
        remaining_sentences = sentences[1:]
        return first_sentence, remaining_sentences
    
    def find_sentence_length(self, sentences):
        '''
        find length of each sentence from the article

        Parameters
        ----------
        sentences: sentences split
        
        Returns
        -------
        sentence_length: list of lenghts of all sentences

        '''
        
        sentence_lengths = [len(sentence) for sentence in sentences]
        return sentence_lengths
    
    def find_top_five(self, sentences, sentence_lengths):
        '''
        find length of top 5 sentences from the article

        Parameters
        ----------
        sentences: sentences split
        sentence_lengths: list of sentence lengths
        
        Returns
        -------
        top5_sentences: top 5 sentences by length

        '''
        
        sorted_idx = np.argsort(sentence_lengths)
        top5_idx = sorted_idx[-5:]
        top5_sentences = [sentences[i] for i in top5_idx]
        return top5_sentences
    
    def summarize(self, article):
        '''
        summarize news article using all functions defined above

        Parameters
        ----------
        article: article to summarize
        
        Returns
        -------
        summary_text: news article summarized

        '''
        
        article_text = article
        preprocess_obj = PreprocessText()
        lowered_text = preprocess_obj.convert_to_lower(article_text)
        filtered_text = preprocess_obj.remove_special_character(lowered_text)
        sentences = self.split_sentences(filtered_text)
        first_sentence, remaining_sentences = self.group_sentences(sentences)
        sentence_lengths = self.find_sentence_length(remaining_sentences)
        top5_sentences = self.find_top_five(remaining_sentences, sentence_lengths)
        
        summary_text_list = [first_sentence]
        summary_text_list.extend(top5_sentences)
        
        summary_text = ' '.join(summary_text_list)
        return summary_text
        
        
        
            