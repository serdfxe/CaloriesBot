from datetime import datetime
from typing import List

from app.models.diary import DiaryRecord


class DiaryService:
    @classmethod
    def record(cls, user_id: int, cpfc: List[int]):
        DiaryRecord.new(user_id=user_id, calories=cpfc[0], protein=cpfc[1], fats=cpfc[2], carbs=cpfc[3])

    @classmethod
    def get_day_summary(cls, user_id: int, date: datetime) -> List[int]:
        today = date.date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())

        records = DiaryRecord.filter(
            DiaryRecord.user_id == user_id,
            DiaryRecord.created_at >= start_of_day,
            DiaryRecord.created_at <= end_of_day
        ).all()

        cpfc = [0] * 4

        for r in records:
            cpfc[0] += r.calories
            cpfc[1] += r.protein
            cpfc[2] += r.fats
            cpfc[3] += r.carbs

        return cpfc

    @classmethod
    def get_today_summary(cls, user_id: int) -> List[int]:
        return cls.get_day_summary(user_id, datetime.today())
    
    @classmethod
    def clear_day_summary(cls, user_id: int, date: datetime):
        today = date.date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())
        
        DiaryRecord.delete_all(
            DiaryRecord.user_id == user_id,
            DiaryRecord.created_at >= start_of_day,
            DiaryRecord.created_at <= end_of_day
        )

    @classmethod
    def clear_today_summary(cls, user_id: int):
        cls.clear_day_summary(user_id, datetime.today())