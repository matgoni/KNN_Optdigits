import numpy as np 

class KNN:
    def __init__(self, k):
        # -- Public Variables --
        self.k = k                   
        self.predicted_classes = []  
        # -- Private Variables --
        self.__values = np.array([])          
        self.__classes = np.array([])           
        self.__distances = np.array([])    
    
    # -- Properties for implementing getters and setters --
    @property
    def values(self):
        return self.__values
    
    @values.setter
    def values(self, values):
        self.__values = values  

    @property
    def classes(self):
        return self.__classes 

    @classes.setter
    def classes(self, classes):
        self.__classes = classes
       
    @property
    def distances(self):
        return self.__distances
    
    @distances.setter
    def distances(self, distances):
        self.__distances = distances

    # -- Methods --
    def calculate_distances(self, p):
        distances = np.sqrt(np.sum((self.values - p) ** 2, axis=1)) 
        self.distances = distances
        return distances.argsort()[:self.k]

    def find_class(self, p): # By majority vote
        nearest_k_indices = self.calculate_distances(p)
        nearest_k_classes = np.array([self.classes[i] for i in nearest_k_indices])

        unique_values, counts = np.unique(nearest_k_classes, return_counts=True)

        max_count = np.max(counts)
        mode_indices = np.where(counts == max_count)[0]

        if len(mode_indices) > 1:
            return nearest_k_classes[0] 
        else:
            return unique_values[mode_indices[0]]  
    
    def compare_classes(self, true_class, p, i):
        predicted_class = self.find_class(p)
        self.predicted_classes.append(predicted_class)
        if self.predicted_classes[-1] == true_class:
            result = f"Point {i}: True class: {true_class}, Predicted class: {self.predicted_classes[-1]}. Correct."
        else:
            result = f"Point {i}: True class: {true_class}, Predicted class: {self.predicted_classes[-1]}. Incorrect."
        return result
    
    def calculate_accuracy(self, true_classes, k):
        correct_count = 0  
        for i in range(len(self.predicted_classes)):
            if self.predicted_classes[i] == true_classes[i]:
                correct_count += 1 
        accuracy = correct_count / len(self.predicted_classes) * 100
        text = f"The accuracy of the KNN algorithm with k={k} is {accuracy:.2f}%."
        print(text)
        return text