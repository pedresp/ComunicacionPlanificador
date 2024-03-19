// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "syst_msgs/srv/detail/adv_service__rosidl_typesupport_introspection_c.h"
#include "syst_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "syst_msgs/srv/detail/adv_service__functions.h"
#include "syst_msgs/srv/detail/adv_service__struct.h"


// Include directives for member types
// Member `drone_id`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  syst_msgs__srv__AdvService_Request__init(message_memory);
}

void syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_fini_function(void * message_memory)
{
  syst_msgs__srv__AdvService_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_member_array[6] = {
  {
    "drone_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, drone_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tof",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, tof),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ancho_de_barrido",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, ancho_de_barrido),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "coordx",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, coordx),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "coordy",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Request, coordy),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_members = {
  "syst_msgs__srv",  // message namespace
  "AdvService_Request",  // message name
  6,  // number of fields
  sizeof(syst_msgs__srv__AdvService_Request),
  syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_member_array,  // message members
  syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_type_support_handle = {
  0,
  &syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_syst_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Request)() {
  if (!syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_type_support_handle.typesupport_identifier) {
    syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &syst_msgs__srv__AdvService_Request__rosidl_typesupport_introspection_c__AdvService_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "syst_msgs/srv/detail/adv_service__rosidl_typesupport_introspection_c.h"
// already included above
// #include "syst_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__functions.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  syst_msgs__srv__AdvService_Response__init(message_memory);
}

void syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_fini_function(void * message_memory)
{
  syst_msgs__srv__AdvService_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_member_array[1] = {
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__srv__AdvService_Response, response),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_members = {
  "syst_msgs__srv",  // message namespace
  "AdvService_Response",  // message name
  1,  // number of fields
  sizeof(syst_msgs__srv__AdvService_Response),
  syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_member_array,  // message members
  syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_type_support_handle = {
  0,
  &syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_syst_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Response)() {
  if (!syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_type_support_handle.typesupport_identifier) {
    syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &syst_msgs__srv__AdvService_Response__rosidl_typesupport_introspection_c__AdvService_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "syst_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_members = {
  "syst_msgs__srv",  // service namespace
  "AdvService",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_Request_message_type_support_handle,
  NULL  // response message
  // syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_Response_message_type_support_handle
};

static rosidl_service_type_support_t syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_type_support_handle = {
  0,
  &syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_syst_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService)() {
  if (!syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_type_support_handle.typesupport_identifier) {
    syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, srv, AdvService_Response)()->data;
  }

  return &syst_msgs__srv__detail__adv_service__rosidl_typesupport_introspection_c__AdvService_service_type_support_handle;
}
