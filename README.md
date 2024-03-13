# Setup to run:

cd library-backend
python manange.py migrate
python seed.py
python manage.py runserver

# TODO:
- Can create data migration to add these data
- Add member in queryselectors for all model for permission management
- proper error handling when object(s) not found
- Write wrapper for integrity error
- Play on id of circulation instead of book_id and member_id
- use routers for including viewsets
- Create proper viewsets
- Implement redis cache
