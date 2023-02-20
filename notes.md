
creating vitual environments

1. venv module - built in
2. virtualenv (pip install virtualenv)
3. pipenv (pip install pipenv)
example:
python -m venv <foldername>

-go to that particular env folder and activate it 
cd env/Scripts
activate
- come to project folder install any modules (which will use activated environment)
pip install numpy
- you have to deactivate whenever you want 


#####
one file = one module = .py file

there will be only one main (__main__)

#python is both interpreter and compiler




#### Lamda - single line/expression fns - lambdademo.py
allows us to write few lines code 
limitations:
1. we can't intialize parameters 
2. debugging becomes diffcult 

map,filter,