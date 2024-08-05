from math import isnan
from utils.db.session import Session
from utils.db.uow import AlchemyUOW


class DBTool():
    session = Session()
    uow = AlchemyUOW()

    @classmethod
    def filter(cls, *args, **kwargs):
        with cls.uow as u:
            if not len(kwargs) and not len(args):
                return u.session.query(cls)
            if len(args):
                return u.session.query(cls).filter(*args)
            return u.session.query(cls).filter_by(**kwargs)# .first() OR .all()

    @classmethod
    def all(cls, **kwargs):
        return cls.session.query(cls).all()

    @classmethod
    def new(cls, **kwargs):
        with cls.uow as u:
            new = cls(**kwargs)

            u.session.add(new)

            u.commit()

            u.session.refresh(new)
            u.session.expunge(new)
        
            return new

    @classmethod
    def update(cls, obj, **kwargs):
        with cls.uow as u:
            u.session.query(cls).filter_by(id=obj.id).update(kwargs)
            u.commit()

    @classmethod
    def delete_first(cls, **kwargs):
        with cls.uow as u:
            obj = u.session.query(cls).filter_by(**kwargs).first()

            u.session.delete(obj)

            u.session.commit()

    @classmethod
    def delete_all(cls, **kwargs):
        with cls.uow as u:
            u.session.query(cls).filter_by(**kwargs).delete()
            u.commit()

    def as_dict(self):
        return {c.name: getattr(self, c.name) if not (isinstance(getattr(self, c.name), float) and isnan(getattr(self, c.name))) else None for c in self.__table__.columns}