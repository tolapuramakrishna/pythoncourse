#IO bound operations and expensive computations
import time
import threading

arr = [4,5,6,2,9]

def calc_sqaure(num):
    print("Calculation square")
    for n in num:
        time.sleep(.5)
        print('square is:', n*n)
def calc_cube(num):
    print("Calculation cube")
    for n in num:
        time.sleep(.8)
        print('cube is:', n*n*n)


if __name__ == '__main__':
    start = time.time()
    # calc_sqaure(arr)
    # calc_cube(arr)
    th1 = threading.Thread(target=calc_sqaure, args=(arr,)) # , should be passed to have it as tuple/list
    th2 = threading.Thread(target=calc_cube, args=(arr,))
    th1.start()
    th2.start()
    print("I am aslo working")
    th1.join()
    th2.join()
    end = time.time()
    print(f'total time taken by threads {end-start}')