# db_service.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from db_config import DB_CONFIG

class DBService:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_engine(self):
        """Get the SQLAlchemy engine."""
        return self.engine

    @contextmanager
    def get_session(self):
        """Provide a transactional scope."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()




# # Create a singleton instance of DBService
# db_service = DBService()