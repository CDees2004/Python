import re

def to_camel_case(text):
    duplicate_text = text
    split_duplicate = re.split(r" -_", duplicate_text)
    print(f"Split duplicate is {split_duplicate}")
    # Use .title to make everything upper but first char
    text.title()
    split_text = re.split(r" -_", text)
    print(f"Split text is {split_text}")
    result_text = ""
    result_text += split_duplicate[0]
    result_text += split_text [1:]
    return result_text
    
    
if __name__ == "__main__":
    test_cases: list[str] = ["the-stealth-warrior", 
                             "The_Stealth_Warrior",
                             "The_Stealth-Warrior"]
                             
    for string in test_cases:
        print(f"CamelCase: {to_camel_case(string)}")