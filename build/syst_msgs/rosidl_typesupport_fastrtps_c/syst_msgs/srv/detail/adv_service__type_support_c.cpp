// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice
#include "syst_msgs/srv/detail/adv_service__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "syst_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "syst_msgs/srv/detail/adv_service__struct.h"
#include "syst_msgs/srv/detail/adv_service__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // drone_id
#include "rosidl_runtime_c/string_functions.h"  // drone_id

// forward declare type support functions


using _AdvService_Request__ros_msg_type = syst_msgs__srv__AdvService_Request;

static bool _AdvService_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AdvService_Request__ros_msg_type * ros_message = static_cast<const _AdvService_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: drone_id
  {
    const rosidl_runtime_c__String * str = &ros_message->drone_id;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: speed
  {
    cdr << ros_message->speed;
  }

  // Field name: tof
  {
    cdr << ros_message->tof;
  }

  // Field name: ancho_de_barrido
  {
    cdr << ros_message->ancho_de_barrido;
  }

  // Field name: coordx
  {
    cdr << ros_message->coordx;
  }

  // Field name: coordy
  {
    cdr << ros_message->coordy;
  }

  return true;
}

static bool _AdvService_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AdvService_Request__ros_msg_type * ros_message = static_cast<_AdvService_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: drone_id
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->drone_id.data) {
      rosidl_runtime_c__String__init(&ros_message->drone_id);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->drone_id,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'drone_id'\n");
      return false;
    }
  }

  // Field name: speed
  {
    cdr >> ros_message->speed;
  }

  // Field name: tof
  {
    cdr >> ros_message->tof;
  }

  // Field name: ancho_de_barrido
  {
    cdr >> ros_message->ancho_de_barrido;
  }

  // Field name: coordx
  {
    cdr >> ros_message->coordx;
  }

  // Field name: coordy
  {
    cdr >> ros_message->coordy;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_syst_msgs
size_t get_serialized_size_syst_msgs__srv__AdvService_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AdvService_Request__ros_msg_type * ros_message = static_cast<const _AdvService_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name drone_id
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->drone_id.size + 1);
  // field.name speed
  {
    size_t item_size = sizeof(ros_message->speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tof
  {
    size_t item_size = sizeof(ros_message->tof);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ancho_de_barrido
  {
    size_t item_size = sizeof(ros_message->ancho_de_barrido);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name coordx
  {
    size_t item_size = sizeof(ros_message->coordx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name coordy
  {
    size_t item_size = sizeof(ros_message->coordy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AdvService_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_syst_msgs__srv__AdvService_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_syst_msgs
size_t max_serialized_size_syst_msgs__srv__AdvService_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: drone_id
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: speed
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: tof
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ancho_de_barrido
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: coordx
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: coordy
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = syst_msgs__srv__AdvService_Request;
    is_plain =
      (
      offsetof(DataType, coordy) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AdvService_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_syst_msgs__srv__AdvService_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AdvService_Request = {
  "syst_msgs::srv",
  "AdvService_Request",
  _AdvService_Request__cdr_serialize,
  _AdvService_Request__cdr_deserialize,
  _AdvService_Request__get_serialized_size,
  _AdvService_Request__max_serialized_size
};

static rosidl_message_type_support_t _AdvService_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AdvService_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, syst_msgs, srv, AdvService_Request)() {
  return &_AdvService_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "syst_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__struct.h"
// already included above
// #include "syst_msgs/srv/detail/adv_service__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _AdvService_Response__ros_msg_type = syst_msgs__srv__AdvService_Response;

static bool _AdvService_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AdvService_Response__ros_msg_type * ros_message = static_cast<const _AdvService_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: response
  {
    cdr << ros_message->response;
  }

  return true;
}

static bool _AdvService_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AdvService_Response__ros_msg_type * ros_message = static_cast<_AdvService_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: response
  {
    cdr >> ros_message->response;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_syst_msgs
size_t get_serialized_size_syst_msgs__srv__AdvService_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AdvService_Response__ros_msg_type * ros_message = static_cast<const _AdvService_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name response
  {
    size_t item_size = sizeof(ros_message->response);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AdvService_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_syst_msgs__srv__AdvService_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_syst_msgs
size_t max_serialized_size_syst_msgs__srv__AdvService_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: response
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = syst_msgs__srv__AdvService_Response;
    is_plain =
      (
      offsetof(DataType, response) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AdvService_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_syst_msgs__srv__AdvService_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AdvService_Response = {
  "syst_msgs::srv",
  "AdvService_Response",
  _AdvService_Response__cdr_serialize,
  _AdvService_Response__cdr_deserialize,
  _AdvService_Response__get_serialized_size,
  _AdvService_Response__max_serialized_size
};

static rosidl_message_type_support_t _AdvService_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AdvService_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, syst_msgs, srv, AdvService_Response)() {
  return &_AdvService_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "syst_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "syst_msgs/srv/adv_service.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t AdvService__callbacks = {
  "syst_msgs::srv",
  "AdvService",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, syst_msgs, srv, AdvService_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, syst_msgs, srv, AdvService_Response)(),
};

static rosidl_service_type_support_t AdvService__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &AdvService__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, syst_msgs, srv, AdvService)() {
  return &AdvService__handle;
}

#if defined(__cplusplus)
}
#endif
