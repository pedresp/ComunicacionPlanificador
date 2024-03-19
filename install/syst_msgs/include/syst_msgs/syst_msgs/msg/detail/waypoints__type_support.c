// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "syst_msgs/msg/detail/waypoints__rosidl_typesupport_introspection_c.h"
#include "syst_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "syst_msgs/msg/detail/waypoints__functions.h"
#include "syst_msgs/msg/detail/waypoints__struct.h"


// Include directives for member types
// Member `wps`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  syst_msgs__msg__Waypoints__init(message_memory);
}

void syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_fini_function(void * message_memory)
{
  syst_msgs__msg__Waypoints__fini(message_memory);
}

size_t syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__size_function__Waypoints__wps(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_const_function__Waypoints__wps(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_function__Waypoints__wps(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__fetch_function__Waypoints__wps(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_const_function__Waypoints__wps(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__assign_function__Waypoints__wps(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_function__Waypoints__wps(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__resize_function__Waypoints__wps(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_member_array[1] = {
  {
    "wps",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(syst_msgs__msg__Waypoints, wps),  // bytes offset in struct
    NULL,  // default value
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__size_function__Waypoints__wps,  // size() function pointer
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_const_function__Waypoints__wps,  // get_const(index) function pointer
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__get_function__Waypoints__wps,  // get(index) function pointer
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__fetch_function__Waypoints__wps,  // fetch(index, &value) function pointer
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__assign_function__Waypoints__wps,  // assign(index, value) function pointer
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__resize_function__Waypoints__wps  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_members = {
  "syst_msgs__msg",  // message namespace
  "Waypoints",  // message name
  1,  // number of fields
  sizeof(syst_msgs__msg__Waypoints),
  syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_member_array,  // message members
  syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_init_function,  // function to initialize message memory (memory has to be allocated)
  syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_type_support_handle = {
  0,
  &syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_syst_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, syst_msgs, msg, Waypoints)() {
  if (!syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_type_support_handle.typesupport_identifier) {
    syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &syst_msgs__msg__Waypoints__rosidl_typesupport_introspection_c__Waypoints_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
