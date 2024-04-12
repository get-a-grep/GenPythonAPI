import pg_singleton

class IFQuestions:
    
    def ask_question(self, question: str, user_id: str):
        
        pg_db = pg_singleton.PGSingleton()

