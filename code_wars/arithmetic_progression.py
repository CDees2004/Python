from collections import counter 

def find_missing(sequence):
    # Identifying the sequence with scoring system
    differences: list[int] = [sequence[i + 1] - sequence[i] for i in range(len(sequence))]
    
    # Add all numeric differences to a list the most common occurence is the AP
    # Finding the missing value
    counter = Counter(differences)
    
    
    # Return found value
    pass
    
if __name__ == "__main__":
    test_sequence = [1, 3, 5, 9, 11]
    print(find_missing(