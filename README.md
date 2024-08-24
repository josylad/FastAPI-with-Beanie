# A FastAPI with MongoDB and Beanie

This is a CRUD API that stores and retrieves data from a MongoDB Atlas database. Powered by FastAPI and Beanie. 

## **SETUP/INSTALLATION.**
### Prerequisites

To use this App you need to have some few prerequisites.

- Python3.10+

- pip

- Virtual environment (virtualenv)

- Code/text editor

- Terminal


### **Set Up**

1. Installing FastAPI and other Modules

    `python3 -m venv virtual`

    **Activate Virtual Environment**

    `source virtual/bin/activate`

* RUN:
    `pip install -r requirements.txt`
    `export PYTHONPATH=$PWD`
* All required applications should be installed now.

2. **Set up MongoDB Atlas.**
 - Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
 - Create an account
 - Create a project
 - Create a database
 - Create a collection
 - Get the database URL 

   - `mongodb+srv://<user>:<password>@<database>:<port>/<collection>?retryWrites=true&w=majority&appName=<yourAppName>"`


3. **Create a .env file and add MongoDB URL (`MONGO_URL`)**

    `touch .env`

    `echo "MONGO_URL=mongodb+srv://<user>:<password>@<database>:<port>/<collection>?retryWrites=true&w=majority&appName=<yourAppName>" >> .env`

4. Run `python app/main.py`
