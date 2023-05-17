# Sentiment140
This repository contains a sentiment analysis project implemented on the Sentiment140 dataset from Kaggle. The goal of the project is to classify the sentiment of Twitter messages into positive, negative, or neutral categories using various techniques and models.

The dataset used for this project is the Sentiment140 dataset, which consists of 1.6 million tweets labeled with sentiment. The project explores different approaches for cleaning the text data, including using NLTK and SpaCy libraries for text preprocessing.

The project incorporates several sentiment analysis techniques and models:

Vader Sentiment Analysis: The Vader sentiment analysis model, a rule-based sentiment analysis tool, is utilized to analyze the sentiment of the preprocessed text data.

Transformers Pipeline: The Transformers library is employed to leverage pre-trained transformer models, such as BERT, to perform sentiment analysis on the cleaned text data.

RoBERTa Model: The project includes the RoBERTa model, a state-of-the-art transformer-based language model, to conduct sentiment analysis. The RoBERTa model is fine-tuned on the Sentiment140 dataset to improve the sentiment classification performance.

Custom LSTM Model: A custom LSTM (Long Short-Term Memory) model is implemented to perform sentiment analysis. The LSTM model takes the preprocessed text data as input and learns to classify the sentiment based on sequential information.

Bag-of-Words with Naive Bayes Classifier and XGBoost: The project explores traditional machine learning approaches, such as bag-of-words representation combined with Naive Bayes classifier and XGBoost, for sentiment analysis on the cleaned text data.

The repository includes python notebook with all the sentiment analysis techniques and models, along with a CSV file containing the cleaned text data processed using NLTK and SpaCy.

This project serves as a comprehensive exploration of sentiment analysis techniques, ranging from rule-based approaches to advanced transformer models and traditional machine learning algorithms. It provides valuable insights into the performance and effectiveness of different methods for sentiment classification on the Sentiment140 dataset.