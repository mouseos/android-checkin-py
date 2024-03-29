# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\n\031com.android.checkin.proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onfig.proto\"\xb5\x03\n\x18\x44\x65viceConfigurationProto\x12\x13\n\x0btouchScreen\x18\x01 \x01(\x05\x12\x10\n\x08keyboard\x18\x02 \x01(\x05\x12\x12\n\nnavigation\x18\x03 \x01(\x05\x12\x14\n\x0cscreenLayout\x18\x04 \x01(\x05\x12\x17\n\x0fhasHardKeyboard\x18\x05 \x01(\x08\x12\x1c\n\x14hasFiveWayNavigation\x18\x06 \x01(\x08\x12\x15\n\rscreenDensity\x18\x07 \x01(\x05\x12\x13\n\x0bglEsVersion\x18\x08 \x01(\x05\x12\x1b\n\x13systemSharedLibrary\x18\t \x03(\t\x12\x1e\n\x16systemAvailableFeature\x18\n \x03(\t\x12\x16\n\x0enativePlatform\x18\x0b \x03(\t\x12\x13\n\x0bscreenWidth\x18\x0c \x01(\x05\x12\x14\n\x0cscreenHeight\x18\r \x01(\x05\x12\x1d\n\x15systemSupportedLocale\x18\x0e \x03(\t\x12\x13\n\x0bglExtension\x18\x0f \x03(\t\x12\x13\n\x0b\x64\x65viceClass\x18\x10 \x01(\x05\x12\x1c\n\x14maxApkDownloadSizeMb\x18\x11 \x01(\x05\x42\x1b\n\x19\x63om.android.checkin.proto'
)




_DEVICECONFIGURATIONPROTO = _descriptor.Descriptor(
  name='DeviceConfigurationProto',
  full_name='DeviceConfigurationProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='touchScreen', full_name='DeviceConfigurationProto.touchScreen', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyboard', full_name='DeviceConfigurationProto.keyboard', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='navigation', full_name='DeviceConfigurationProto.navigation', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screenLayout', full_name='DeviceConfigurationProto.screenLayout', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hasHardKeyboard', full_name='DeviceConfigurationProto.hasHardKeyboard', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hasFiveWayNavigation', full_name='DeviceConfigurationProto.hasFiveWayNavigation', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screenDensity', full_name='DeviceConfigurationProto.screenDensity', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glEsVersion', full_name='DeviceConfigurationProto.glEsVersion', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemSharedLibrary', full_name='DeviceConfigurationProto.systemSharedLibrary', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemAvailableFeature', full_name='DeviceConfigurationProto.systemAvailableFeature', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nativePlatform', full_name='DeviceConfigurationProto.nativePlatform', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screenWidth', full_name='DeviceConfigurationProto.screenWidth', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screenHeight', full_name='DeviceConfigurationProto.screenHeight', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemSupportedLocale', full_name='DeviceConfigurationProto.systemSupportedLocale', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glExtension', full_name='DeviceConfigurationProto.glExtension', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceClass', full_name='DeviceConfigurationProto.deviceClass', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxApkDownloadSizeMb', full_name='DeviceConfigurationProto.maxApkDownloadSizeMb', index=16,
      number=17, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=454,
)

DESCRIPTOR.message_types_by_name['DeviceConfigurationProto'] = _DEVICECONFIGURATIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceConfigurationProto = _reflection.GeneratedProtocolMessageType('DeviceConfigurationProto', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECONFIGURATIONPROTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DeviceConfigurationProto)
  })
_sym_db.RegisterMessage(DeviceConfigurationProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
