# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: student.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'student.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstudent.proto\x12\x07student\"=\n\x07Student\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"\"\n\x0fStudentResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0eStudentRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"1\n\x0bStudentList\x12\"\n\x08students\x18\x01 \x03(\x0b\x32\x10.student.Student\"\x0e\n\x0c\x45mptyRequest2\xc3\x01\n\x0eStudentService\x12;\n\rCreateStudent\x12\x10.student.Student\x1a\x18.student.StudentResponse\x12\x37\n\nGetStudent\x12\x17.student.StudentRequest\x1a\x10.student.Student\x12;\n\x0cListStudents\x12\x15.student.EmptyRequest\x1a\x14.student.StudentListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'student_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STUDENT']._serialized_start=26
  _globals['_STUDENT']._serialized_end=87
  _globals['_STUDENTRESPONSE']._serialized_start=89
  _globals['_STUDENTRESPONSE']._serialized_end=123
  _globals['_STUDENTREQUEST']._serialized_start=125
  _globals['_STUDENTREQUEST']._serialized_end=153
  _globals['_STUDENTLIST']._serialized_start=155
  _globals['_STUDENTLIST']._serialized_end=204
  _globals['_EMPTYREQUEST']._serialized_start=206
  _globals['_EMPTYREQUEST']._serialized_end=220
  _globals['_STUDENTSERVICE']._serialized_start=223
  _globals['_STUDENTSERVICE']._serialized_end=418
# @@protoc_insertion_point(module_scope)
