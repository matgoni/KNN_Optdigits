# KNN_Optdigits

## Problem Description📚

The presented project is based on the "Optical Recognition of Handwritten Digits" database, developed through the joint effort of E. Alpaydin and C. Kaynak from the Department of Computer Engineering at Bogazici University in Istanbul, Turkey, in July 1998. The essence of the problem is the automated classification of handwritten digits, a crucial research area within optical character recognition (OCR). The database was constructed using NIST preprocessing programs to extract normalized bitmaps of handwritten digits, achieving a reduced and dimensionally efficient 8x8 representation, presented in an array of 64 elements where each is an integer in the range of 0 to 16.

To address this classification problem, we propose the implementation of a k-nearest neighbors (k-NN) algorithm 🤖, noted for its simplicity and effectiveness in classifying complex patterns such as handwritten digits ✍️. The dataset is divided into two parts: a training set with 3823 instances 📊 and a test set with 1797 instances 📈. The prediction of the class for new digits is performed by considering the majority class among the nearest points, thus allowing classification based on similarity to previously known examples.

## Results
