from multiprocessing.spawn import import_main_path
from pg_singleton import PGSingleton

class IFQuestions:
    
    def ask_question(self, question: str, user_id: str):
        
        query_str = "INSERT INTO general (Question, UserID, ) VALUES ('%s', '%s')" % (question, user_id)
        
        return query_str


    def get_last_question(self, user_id: str):

        query_str = ""

        return query_str