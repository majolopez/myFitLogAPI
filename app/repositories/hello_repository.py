from app.core.supabase import supabase

class HelloRepository:

    @staticmethod
    def get_messages():
        print("HelloRepository.get_messages called")
        result = (
            supabase
            .table("hello_messages")
            .select("*")
            .execute()
        )

        return result.data 