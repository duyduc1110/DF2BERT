#!/usr/bin/env python
# coding: utf-8


import math

class Feature(object):
    def __init__(self, text, pos=""):
        super(Feature, self).__init__()
        self._text = text
        self._pos = pos
        self._freq = 1
        self._llr = 0.0
        self._present_on_topic = 0
        self._present_off_topic = 0
        self._absent_on_topic = 0
        self._absent_off_topic = 0

    def set_parameters_for_test(self, p_on_t, p_off_t, a_on_t, a_off_t, llr):
        self._llr = llr
        self._present_on_topic = p_on_t
        self._present_off_topic = p_off_t
        self._absent_on_topic = a_on_t
        self._absent_off_topic = a_off_t

    def count_freq(self):
        self._freq += 1

    def count_present_on_topic(self):
        self._present_on_topic += 1
        
    def set_present_off_topic(self):
        self._present_off_topic = self._freq - self._present_on_topic
        
    def set_absent_on_topic(self, num_data_on_topic):
        self._absent_on_topic = num_data_on_topic - self._present_on_topic

    def set_absent_off_topic(self, num_data):
        self._absent_off_topic = num_data - self._present_on_topic - self._present_off_topic - self._absent_on_topic
        
    def print_info(self):
        print(self._text)
        print("freq: ", self._freq)
        print("present_on_topic: ", self._present_on_topic)
        print("present_off_topic: ", self._present_off_topic)
        print("absent_on_topic: ", self._absent_on_topic)
        print("absent_off_topic: ", self._absent_off_topic)
    
    def reset_info(self):
        self._present_on_topic = 0
        self._present_off_topic = 0
        self._absent_on_topic = 0
        self._absent_off_topic = 0
    
    def set_llr(self): 
        N = self._present_on_topic + self._absent_on_topic + self._present_off_topic + self._absent_off_topic
        pt = (self._present_on_topic + self._present_off_topic) / N
        p1 = self._present_on_topic / ( 1e-10 + self._present_on_topic + self._absent_on_topic)
        p2 = self._present_off_topic / ( 1e-10 + self._present_off_topic + self._absent_off_topic)
        

        element1 = element2 = element3 = element4 = 0
        if self._present_on_topic == 0:
            element1 = 0.
        else:
            element1 = -2 * self._present_on_topic * math.log(pt) - (-2 * self._present_on_topic * math.log(p1))

        if self._absent_on_topic == 0:
            element2 = 0.
        else:
            element2 = -2 * self._absent_on_topic * math.log(1 - pt) - (-2 * self._absent_on_topic * math.log(1 - p1))

        if self._present_off_topic == 0:
            element3 = 0.
        else:
            element3 = -2 * self._present_off_topic * math.log(pt) - (-2 * self._present_off_topic * math.log(p2))

        if self._absent_off_topic == 0:
            element4 = 0.
        else:
            element4 = -2 * self._absent_off_topic * math.log(1 - pt) - (-2 * self._absent_off_topic * math.log(1 - p2))
        
        self._llr = (element1 + element2 + element3 + element4)



def get_term_weighting(target_label, num_data_on_topic, wordlist, dataset):
    
    term_weighting = wordlist   
    
    for data in dataset:
        label = data[0]
        text = data[1]
        if label == target_label: #OnTopic
            for word in text:
                term_weighting[word].count_present_on_topic()

    #update wordlist for calculating LLR
    num_data = len(dataset)
    for word in term_weighting:
        term_weighting[word].set_present_off_topic()
        term_weighting[word].set_absent_on_topic(num_data_on_topic)
        term_weighting[word].set_absent_off_topic(num_data)
        term_weighting[word].set_llr()     
     
    return sorted(term_weighting.items(), key=lambda d: d[1]._llr, reverse = True)