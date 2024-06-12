from sqlmodel import create_engine, Session

DATABASE_URL = 'postgresql://postgres@localhost/crud_u'

# from sqlmodel import create_engine, SQLModel, Session

engine = create_engine(DATABASE_URL, echo=True)

# def init_db():
#     SQLModel.metadata.create_all(engine)
    
def get_session():
        with Session(engine) as session:
            yield session

