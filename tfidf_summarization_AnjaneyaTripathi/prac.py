import re
import nltk
import math
from nltk.tokenize import word_tokenize, sent_tokenize

def clean_text(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    article = sent_tokenize(text)
    sentences = []
    # removing special characters and extra whitespaces
    for sentence in article:
        sentence = re.sub('[\s+]', ' ', sentence)
        sentences.append(sentence)
    sentences.pop() 
    display = "".join(sentences)
    print('Initial Text: ')
    print(display)
    print('\n')
    return sentences

# counting the number of words in the document (sentence)
def cnt_words(sent):
    cnt = 0
    words = word_tokenize(sent)
    for word in words:
        cnt = cnt + 1
    return cnt
   
# getting data about each sentence (frequency of words) 
def cnt_in_sent(sentences):
    txt_data = []
    i = 0
    for sent in sentences:
        i = i + 1
        cnt = cnt_words(sent)
        temp = {'id' : i, 'word_cnt' : cnt}
        txt_data.append(temp)
    return txt_data

# creating a dictionary of words for each document (sentence)
def freq_dict(sentences):
    i = 0
    freq_list = []
    for sent in sentences:
        i = i + 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1
            temp = {'id' : i, 'freq_dict' : freq_dict}
        freq_list.append(temp)
    return freq_list
   
# calculating the term frequency 
def calc_TF(text_data, freq_list):
    tf_scores = []
    for item in freq_list:
        ID = item['id']
        for k in item['freq_dict']:
            temp = {
                'id': item['id'],
                'tf_score': item['freq_dict'][k]/text_data[ID-1]['word_cnt'],
                'key': k
                }
            tf_scores.append(temp)
    return tf_scores
    
#calculating the inverse document frequency
def calc_IDF(text_data, freq_list):
    idf_scores =[]
    cnt = 0
    for item in freq_list:
        cnt = cnt + 1
        for k in item['freq_dict']:
            val = sum([k in it['freq_dict'] for it in freq_list])
            temp = {
                'id': cnt, 
                'idf_score': math.log(len(text_data)/(val+1)), 
                'key': k}
            idf_scores.append(temp)
    return idf_scores

# calculating TFIDF value
def calc_TFIDF(tf_scores, idf_scores):
    tfidf_scores = []
    for j in idf_scores:
        for i in tf_scores:
            if j['key'] == i['key'] and j['id'] == i['id']:
                temp = {
                    'id': j['id'],
                    'tfidf_score': j['idf_score'] * i['tf_score'],
                    'key': j['key']
                    }
                tfidf_scores.append(temp)
    return tfidf_scores

# giving each sentence a score
def sent_scores(tfidf_scores, sentences, text_data):
    sent_data = []
    for txt in text_data:
        score = 0
        for i in range(0, len(tfidf_scores)):
            t_dict = tfidf_scores[i]
            if txt['id'] == t_dict['id']:
                score = score + t_dict['tfidf_score']
        temp = {
            'id': txt['id'],
            'score': score,
            'sentence': sentences[txt['id']-1]}
        sent_data.append(temp)
    return sent_data

# creating the summary
def summary(sent_data):
    cnt = 0
    summary = []
    for t_dict in sent_data:
        cnt  = cnt + t_dict['score']
    avg = cnt / len(sent_data)
    for sent in sent_data:
        if sent['score'] >= (avg):
            summary.append(sent['sentence'])
    summary = " ".join(summary)
    return summary


sentences =  clean_text('text.txt')
text_data = cnt_in_sent(sentences)

freq_list = freq_dict(sentences)
tf_scores = calc_TF(text_data, freq_list)
idf_scores = calc_IDF(text_data, freq_list)

tfidf_scores = calc_TFIDF(tf_scores, idf_scores)

sent_data = sent_scores(tfidf_scores, sentences, text_data)
result = summary(sent_data)

print('Final Summary: ')
print(result)



        
            
    