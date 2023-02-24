# --------------------------- TESTING FILE--------------------------------------
# File for testing functions, modules

# Import the modules
import application.models.model as model
from application.models.model import *

# Tests

# --------------- Testing model
# OKK
# insert_doc_data('5', '4', 'bsc', 'woljwc', 'col2', 'en')
# delete_doc_data('1')

# OKK
# insert_cor_data('1', 'corpus_name_1', 'c22', 'this is a corpus', 'v2', '5')
# delete_cor_data('1')


# --------------- Testing Document Model
from application.models.Document import *
print(select_where('2'))
# insert_doc_data('5', '4', 'bsc', 'woljwc', 'col2', 'en')
# ---------------- Testing database
from application.config.database import get_connection

# conn = get_connection()
# cursor = conn.cursor()

# print(cursor.execute('SELECT * FROM documents;'))
# conn.commit()


# Testing controller
import application.controllers.api as contr

# Testing controller documents
import application.controllers.controller_documents as Document
