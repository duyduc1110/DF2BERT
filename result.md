# Method
## Bert
Fine-tuned bert sequence classification `bert-base-uncased`. Build from Pytorch Modules and `transformer` package. Using last hidden layer of [CLS] token with Dropout(0.1) to connect with Dense(2). Training configuration:
* Max sequence length: 512
* Learning rate: 1e-5
* Epochs: 3
* Batch size: 6

## Bert+CNN
Extract last hidden layer for each token as embedding layer. Then connect it to 3 convolution neural network layers of 768 filter and kernel sizes of [2, 3, 4].  After that is a max pooling layer for each CNN layer with their kernel size, then concatenate them. Training configuration:
* Max sequence length: 512
* Learning rate: 1e-5
* Epochs: 10
* Batch size: 5

## Bert + Feature Extraction
Not yet T.T

## ML (Naive Bayer, KNN)
Tfidf vectors, 10 epochs per model

# Result
I will update it later bro

Bert eb512 1e-5 e4:
loss, 0.2554, 0.1213, 0.0652, 0.0445
acc, 0.9586, 0.9831, 0.9878, 0.9949
f1, 0.9276, 0.9296, 0.9304, 0.9334



Bert + CNN(64,3):
loss, 0.1386, 0.1125, 0.0822, 0.0606, 0.0494, 0.0332, 0.0207, 0.0144, 0.0105, 0.0068, 0.0050, 0.0038, 0.0023, 0.0019, 0.



BertLLR30: 
train loss: 0.0139
train f1: 0.9970
test f1: 0.9357

