from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, ForeignKey, LargeBinary, text
from database import Base
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, TIMESTAMP


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(255))
    title = Column(String(127))
    firstName = Column(String(255))
    lastName = Column(String(255))
    email = Column(String(255), unique=True)
    secondary_email = Column(String(255))
    defaultEmail = Column(TINYINT(1), comment='1= email, 2=secondary')
    password = Column(String(255))
    image = Column(LargeBinary)
    account_id = Column(ForeignKey('account.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    last_login_time = Column(DateTime)
    created_time = Column(DateTime)
    inactive = Column(TINYINT(1), server_default=text("'0'"))
    inactive_datetime = Column(DateTime)
    language_id = Column(ForeignKey('language.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    signature = Column(Text)
    coach_id = Column(ForeignKey('user.id'), index=True)
    secondary_coach_id = Column(ForeignKey('user.id'), index=True)
    timezone_offset = Column(Float)
    timezone = Column(INTEGER(11))
    brand_id = Column(INTEGER(11))
    terms_accepted_datetime = Column(TIMESTAMP)
    passwordchanged_time = Column(TIMESTAMP)
    otp = Column(String(255))
    thumbnail = Column(String(255))
    thumbnail = Column(String(255))
    jwt_access_token = Column(String(255))
    jwt_refresh_token = Column(String(255))
    previous_password = Column(Text)



# DATABASE_URL = "mysql://root:Harsh@15@localhost/zenarate_db"
# engine = create_engine(DATABASE_URL)
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class Assistant(Base):
#     pass
