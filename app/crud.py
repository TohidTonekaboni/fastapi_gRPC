from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Student

async def create_student(db: AsyncSession, first_name: str, last_name: str, age: int):
    student = Student(first_name=first_name, last_name=last_name, age=age)
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student

async def get_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).where(Student.id == student_id))
    return result.scalars().first()

async def list_students(db: AsyncSession):
    result = await db.execute(select(Student))
    return result.scalars().all()
