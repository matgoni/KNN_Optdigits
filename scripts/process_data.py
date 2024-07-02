class DATA:
    def __init__(self, file_name, data=None, values=None, classes=None):
        self.file_name = file_name
        self.data = data if data is not None else []
        self.values = values if values is not None else []
        self.classes = classes if classes is not None else []

    def get_data(self):
        try:
            with open(self.file_name, 'r') as file:
                self.data = []
                for line in file:
                    try:
                        values_str = line.rstrip().split(',')
                        values_int = [int(value) for value in values_str]
                        self.data.append(values_int)
                    except ValueError as e:
                        print(f"Error converting values to integers: {e}")
        except FileNotFoundError as e:
            print(f"Error opening file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def split_data(self):
        self.values = []  
        self.classes = []   
        for array in self.data:
            self.values.append(array[:-1])  
            self.classes.append(array[-1])  