import numpy as np
import time

print("pythonic way vs numpy")

start = time.time()
array1 = list(range(1000000))
array2 = list(range(1000000))

newArray = [array1[i]+array2[i] for i in range(len(array1))]

end= time.time()

print(f"Time taken by pythonic way {end -start} secs")


#numpy

start = time.time()
array1 = np.arange(1000000)
array2 = np.arange(1000000)

newArray = array1+array2

end= time.time()

print(f"Time taken by numpy way {end -start} secs")
#numpy uses optimized algo from c language code internally