// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "syst_msgs/srv/detail/adv_service__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace syst_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AdvService_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AdvService_Request_type_support_ids_t;

static const _AdvService_Request_type_support_ids_t _AdvService_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AdvService_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AdvService_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AdvService_Request_type_support_symbol_names_t _AdvService_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, syst_msgs, srv, AdvService_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, syst_msgs, srv, AdvService_Request)),
  }
};

typedef struct _AdvService_Request_type_support_data_t
{
  void * data[2];
} _AdvService_Request_type_support_data_t;

static _AdvService_Request_type_support_data_t _AdvService_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AdvService_Request_message_typesupport_map = {
  2,
  "syst_msgs",
  &_AdvService_Request_message_typesupport_ids.typesupport_identifier[0],
  &_AdvService_Request_message_typesupport_symbol_names.symbol_name[0],
  &_AdvService_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AdvService_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AdvService_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace syst_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<syst_msgs::srv::AdvService_Request>()
{
  return &::syst_msgs::srv::rosidl_typesupport_cpp::AdvService_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, syst_msgs, srv, AdvService_Request)() {
  return get_message_type_support_handle<syst_msgs::srv::AdvService_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace syst_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AdvService_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AdvService_Response_type_support_ids_t;

static const _AdvService_Response_type_support_ids_t _AdvService_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AdvService_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AdvService_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AdvService_Response_type_support_symbol_names_t _AdvService_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, syst_msgs, srv, AdvService_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, syst_msgs, srv, AdvService_Response)),
  }
};

typedef struct _AdvService_Response_type_support_data_t
{
  void * data[2];
} _AdvService_Response_type_support_data_t;

static _AdvService_Response_type_support_data_t _AdvService_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AdvService_Response_message_typesupport_map = {
  2,
  "syst_msgs",
  &_AdvService_Response_message_typesupport_ids.typesupport_identifier[0],
  &_AdvService_Response_message_typesupport_symbol_names.symbol_name[0],
  &_AdvService_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AdvService_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AdvService_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace syst_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<syst_msgs::srv::AdvService_Response>()
{
  return &::syst_msgs::srv::rosidl_typesupport_cpp::AdvService_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, syst_msgs, srv, AdvService_Response)() {
  return get_message_type_support_handle<syst_msgs::srv::AdvService_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace syst_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AdvService_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AdvService_type_support_ids_t;

static const _AdvService_type_support_ids_t _AdvService_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AdvService_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AdvService_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AdvService_type_support_symbol_names_t _AdvService_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, syst_msgs, srv, AdvService)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, syst_msgs, srv, AdvService)),
  }
};

typedef struct _AdvService_type_support_data_t
{
  void * data[2];
} _AdvService_type_support_data_t;

static _AdvService_type_support_data_t _AdvService_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AdvService_service_typesupport_map = {
  2,
  "syst_msgs",
  &_AdvService_service_typesupport_ids.typesupport_identifier[0],
  &_AdvService_service_typesupport_symbol_names.symbol_name[0],
  &_AdvService_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t AdvService_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AdvService_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace syst_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<syst_msgs::srv::AdvService>()
{
  return &::syst_msgs::srv::rosidl_typesupport_cpp::AdvService_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
