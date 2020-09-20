# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steward/asset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steward import organization_pb2 as steward_dot_organization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steward/asset.proto',
  package='steward',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13steward/asset.proto\x12\x07steward\x1a\x1asteward/organization.proto\"v\n\x05\x41sset\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12+\n\x0corganization\x18\x04 \x01(\x0b\x32\x15.steward.Organization\x12\x10\n\x08\x61\x63quired\x18\x05 \x01(\x03\"\x1e\n\x0fGetAssetRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\"!\n\x12\x44\x65leteAssetRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\"@\n\x12UpdateAssetRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x1d\n\x05\x61sset\x18\x02 \x01(\x0b\x32\x0e.steward.Asset\",\n\x11ListAssetsRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\tb\x06proto3'
  ,
  dependencies=[steward_dot_organization__pb2.DESCRIPTOR,])




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='steward.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.Asset._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='steward.Asset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='steward.Asset.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization', full_name='steward.Asset.organization', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acquired', full_name='steward.Asset.acquired', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=178,
)


_GETASSETREQUEST = _descriptor.Descriptor(
  name='GetAssetRequest',
  full_name='steward.GetAssetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.GetAssetRequest._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=210,
)


_DELETEASSETREQUEST = _descriptor.Descriptor(
  name='DeleteAssetRequest',
  full_name='steward.DeleteAssetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.DeleteAssetRequest._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=245,
)


_UPDATEASSETREQUEST = _descriptor.Descriptor(
  name='UpdateAssetRequest',
  full_name='steward.UpdateAssetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.UpdateAssetRequest._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='steward.UpdateAssetRequest.asset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=311,
)


_LISTASSETSREQUEST = _descriptor.Descriptor(
  name='ListAssetsRequest',
  full_name='steward.ListAssetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='steward.ListAssetsRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=357,
)

_ASSET.fields_by_name['organization'].message_type = steward_dot_organization__pb2._ORGANIZATION
_UPDATEASSETREQUEST.fields_by_name['asset'].message_type = _ASSET
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['GetAssetRequest'] = _GETASSETREQUEST
DESCRIPTOR.message_types_by_name['DeleteAssetRequest'] = _DELETEASSETREQUEST
DESCRIPTOR.message_types_by_name['UpdateAssetRequest'] = _UPDATEASSETREQUEST
DESCRIPTOR.message_types_by_name['ListAssetsRequest'] = _LISTASSETSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'steward.asset_pb2'
  # @@protoc_insertion_point(class_scope:steward.Asset)
  })
_sym_db.RegisterMessage(Asset)

GetAssetRequest = _reflection.GeneratedProtocolMessageType('GetAssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETASSETREQUEST,
  '__module__' : 'steward.asset_pb2'
  # @@protoc_insertion_point(class_scope:steward.GetAssetRequest)
  })
_sym_db.RegisterMessage(GetAssetRequest)

DeleteAssetRequest = _reflection.GeneratedProtocolMessageType('DeleteAssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEASSETREQUEST,
  '__module__' : 'steward.asset_pb2'
  # @@protoc_insertion_point(class_scope:steward.DeleteAssetRequest)
  })
_sym_db.RegisterMessage(DeleteAssetRequest)

UpdateAssetRequest = _reflection.GeneratedProtocolMessageType('UpdateAssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEASSETREQUEST,
  '__module__' : 'steward.asset_pb2'
  # @@protoc_insertion_point(class_scope:steward.UpdateAssetRequest)
  })
_sym_db.RegisterMessage(UpdateAssetRequest)

ListAssetsRequest = _reflection.GeneratedProtocolMessageType('ListAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTASSETSREQUEST,
  '__module__' : 'steward.asset_pb2'
  # @@protoc_insertion_point(class_scope:steward.ListAssetsRequest)
  })
_sym_db.RegisterMessage(ListAssetsRequest)


# @@protoc_insertion_point(module_scope)
