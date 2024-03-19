# generated from rosidl_generator_py/resource/_idl.py.em
# with input from syst_msgs:srv/AdvService.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AdvService_Request(type):
    """Metaclass of message 'AdvService_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('syst_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'syst_msgs.srv.AdvService_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__adv_service__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__adv_service__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__adv_service__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__adv_service__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__adv_service__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AdvService_Request(metaclass=Metaclass_AdvService_Request):
    """Message class 'AdvService_Request'."""

    __slots__ = [
        '_drone_id',
        '_speed',
        '_tof',
        '_ancho_de_barrido',
        '_coordx',
        '_coordy',
    ]

    _fields_and_field_types = {
        'drone_id': 'string',
        'speed': 'double',
        'tof': 'double',
        'ancho_de_barrido': 'double',
        'coordx': 'double',
        'coordy': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.drone_id = kwargs.get('drone_id', str())
        self.speed = kwargs.get('speed', float())
        self.tof = kwargs.get('tof', float())
        self.ancho_de_barrido = kwargs.get('ancho_de_barrido', float())
        self.coordx = kwargs.get('coordx', float())
        self.coordy = kwargs.get('coordy', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.drone_id != other.drone_id:
            return False
        if self.speed != other.speed:
            return False
        if self.tof != other.tof:
            return False
        if self.ancho_de_barrido != other.ancho_de_barrido:
            return False
        if self.coordx != other.coordx:
            return False
        if self.coordy != other.coordy:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def drone_id(self):
        """Message field 'drone_id'."""
        return self._drone_id

    @drone_id.setter
    def drone_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'drone_id' field must be of type 'str'"
        self._drone_id = value

    @builtins.property
    def speed(self):
        """Message field 'speed'."""
        return self._speed

    @speed.setter
    def speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'speed' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'speed' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._speed = value

    @builtins.property
    def tof(self):
        """Message field 'tof'."""
        return self._tof

    @tof.setter
    def tof(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tof' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tof' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tof = value

    @builtins.property
    def ancho_de_barrido(self):
        """Message field 'ancho_de_barrido'."""
        return self._ancho_de_barrido

    @ancho_de_barrido.setter
    def ancho_de_barrido(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ancho_de_barrido' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ancho_de_barrido' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ancho_de_barrido = value

    @builtins.property
    def coordx(self):
        """Message field 'coordx'."""
        return self._coordx

    @coordx.setter
    def coordx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'coordx' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'coordx' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._coordx = value

    @builtins.property
    def coordy(self):
        """Message field 'coordy'."""
        return self._coordy

    @coordy.setter
    def coordy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'coordy' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'coordy' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._coordy = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_AdvService_Response(type):
    """Metaclass of message 'AdvService_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('syst_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'syst_msgs.srv.AdvService_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__adv_service__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__adv_service__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__adv_service__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__adv_service__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__adv_service__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AdvService_Response(metaclass=Metaclass_AdvService_Response):
    """Message class 'AdvService_Response'."""

    __slots__ = [
        '_response',
    ]

    _fields_and_field_types = {
        'response': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.response = kwargs.get('response', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'response' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'response' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._response = value


class Metaclass_AdvService(type):
    """Metaclass of service 'AdvService'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('syst_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'syst_msgs.srv.AdvService')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__adv_service

            from syst_msgs.srv import _adv_service
            if _adv_service.Metaclass_AdvService_Request._TYPE_SUPPORT is None:
                _adv_service.Metaclass_AdvService_Request.__import_type_support__()
            if _adv_service.Metaclass_AdvService_Response._TYPE_SUPPORT is None:
                _adv_service.Metaclass_AdvService_Response.__import_type_support__()


class AdvService(metaclass=Metaclass_AdvService):
    from syst_msgs.srv._adv_service import AdvService_Request as Request
    from syst_msgs.srv._adv_service import AdvService_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
