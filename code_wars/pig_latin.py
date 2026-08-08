def pig_it(text):
    pig_list = text.split()
    result_list = []
    for word in pig_list:
        result_list.append(word[1:] + word[0] + "ay")
        
    result = " ".join(result_list)
    return result
    

if __name__ == "__main__":
    test_string = 'Pig latin is cool'
    print(pig_it(test_string))