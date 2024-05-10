================
fastapi-auth
================



----

A personal, ready to go Fast API project with authentication, authorization, and user management using jwt auth with Bearer/Cookie Transport.

----



Installation
============

**First,** clone the repo:

.. code-block:: bash

    git clone https://github.com/YousifAljanabi/fastapi-auth.git

**Second,** install the dependencies:

.. code-block:: bash

    python -m pip install -r requirements.txt


**Third,** create a .env file with the following variables:

.. code-block:: python

    SECRET=
    DATABASE_URL =

**Third,** run the following command:

.. code-block:: bash

    alembic init alembic

now access the env.py file and change the following line:

.. code-block:: python

    # target_metadata = Base.metadata
    from db import Base
    target_metadata = Base.metadata

and access the alembic.ini file and change the following line:

.. code-block:: python

    # sqlalchemy.url = driver://user:pass@localhost/dbname
    sqlalchemy.url = your_database_url

finally run the following commands:

.. code-block:: bash

    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    unicorn main:app --reload


