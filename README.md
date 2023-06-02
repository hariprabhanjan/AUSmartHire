# AUSmartHire
# Project Setup

1)create virtual environment inside of it(main project folder)
    
      #windows users
python -m venv c:\path\to\myenv

2)Activate the virtual environment
      
      #Windows users
\venv\Scripts\activate.bat

3)Install all project dependencies

    pip install flask Flask-PyMongo Flask-WTF
    python -m pip install "pymongo[srv]"

4)Setup the mongoDB cluster


5)Project Structure
-----------------------------------------------------------------------------------------------------------------------------------------
Project_root_dir
│
|
|__ applicati
|   
|    |__ templates 
|    |__ __init__.py 
|    |__ routes.py   
|    |__ forms.py    
|                                
|
|__ env
|
|
|
|__ README.md
|
|
|__ run.py

