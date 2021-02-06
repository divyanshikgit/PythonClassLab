import numpy as np

random_numbers = np.random.uniform(1,20,20)
print(random_numbers)               # Printing the array

b = random_numbers.reshape(4,5)     # Reshaping the array in 4,5
print('Reshaped array in 4,5: \n{}'.format(b))

b[np.where(b == np.max(b, axis=1, keepdims=True))] = 0      # Replacing the max number with 0
print('Replaced max with 0 array: \n{}'.format(b))
