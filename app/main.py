from fastapi import FastAPI, Depends
import grpc
from concurrent import futures
import asyncio

from . import database, crud, models
from .proto import student_pb2, student_pb2_grpc

app = FastAPI()

# gRPC server setup
class StudentService(student_pb2_grpc.StudentServiceServicer):
    async def CreateStudent(self, request, context):
        async with database.get_db() as db:
            student = await crud.create_student(db, request.first_name, request.last_name, request.age)
            return student_pb2.StudentResponse(message=f"Student {student.first_name} created")

    async def GetStudent(self, request, context):
        async with database.get_db() as db:
            student = await crud.get_student(db, request.id)
            return student_pb2.Student(first_name=student.first_name, last_name=student.last_name, age=student.age)

    async def ListStudents(self, request, context):
        async with database.get_db() as db:
            students = await crud.list_students(db)
            return student_pb2.StudentList(students=[student_pb2.Student(
                first_name=student.first_name, last_name=student.last_name, age=student.age) for student in students])

async def serve():
    server = grpc.aio.server()
    student_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(serve())
