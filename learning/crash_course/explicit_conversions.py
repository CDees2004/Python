# int to str cannot be implicit
age = 22
# Below is incorrect
# message = "Happy " + age + "rd Birthday!"

# Correct 
message = "Happy " + str(age) + "rd Birthday!"
print(message)