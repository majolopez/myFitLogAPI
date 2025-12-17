from app.repositories.hello_repository import HelloRepository

class HelloService:

    @staticmethod
    def get_user():
        messages = HelloRepository.get_messages()
        
        return {
            "status": "ok",
            "data": messages[0]["message"] if messages else "No messages found"
        }
