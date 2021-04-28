from plugins.base.db_manager import Base, engine


def init_db():
    from .models.api_tests import SecurityTestsDAST
    from .models.security_results import SecurityResultsDAST
    Base.metadata.create_all(bind=engine)
