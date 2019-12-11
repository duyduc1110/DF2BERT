#!/usr/bin/env python
# coding: utf-8


import tmunlp as nlp

def get_label_term_weighting(data_filepath, label_list):
    labels = {} # label : freq
    label_wordlist = {}
    dataset = [] # label : text

    for l in label_list:
        labels[l] = 0
        label_wordlist[l] = dict()


    for data in open(data_filepath, 'r', encoding='UTF-8-sig').readlines():
        items = data.strip('\n').split("\t")

        if len(items) == 2:
            label = items[0]
            text = items[1]
            seg_content = text.split()

            distinct_text = list(set(seg_content)) #distinct the list, but revert the order
            dataset.append([label, distinct_text]) 

            labels[label] += 1

            for word in distinct_text:
                for l in label_list:
                    if word in label_wordlist[l]:
                        label_wordlist[l][word].count_freq()
                    else:
                        label_wordlist[l][word] = nlp.Feature(word)


    label_term_weighting = {}
    for label, num_data_label in labels.items():
        for word in label_wordlist[label]:
            label_wordlist[label][word].reset_info()

        label_term_weighting[label] = nlp.get_term_weighting(label, num_data_label, label_wordlist[label], dataset)  
    
    return label_term_weighting 



def get_keyword(label, label_term_weighting, topN = 10, skip_unigram = False):
    keyword_list = {}
    for term in label_term_weighting[label]:
        if skip_unigram and len(term[0]) > 1 and term[1]._present_on_topic >= term[1]._present_off_topic:
            keyword_list[term[0]] = term[1]._llr
        if skip_unigram == False and term[1]._present_on_topic >= term[1]._present_off_topic:
            keyword_list[term[0]] = term[1]._llr

    if len(keyword_list) <= topN:
        return keyword_list
    else:
        return dict(list(keyword_list.items())[:topN])


