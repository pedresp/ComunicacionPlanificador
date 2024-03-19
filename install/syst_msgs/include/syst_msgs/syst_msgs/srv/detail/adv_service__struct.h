// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_H_
#define SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'drone_id'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AdvService in the package syst_msgs.
typedef struct syst_msgs__srv__AdvService_Request
{
  rosidl_runtime_c__String drone_id;
  double speed;
  double tof;
  double ancho_de_barrido;
  double coordx;
  double coordy;
} syst_msgs__srv__AdvService_Request;

// Struct for a sequence of syst_msgs__srv__AdvService_Request.
typedef struct syst_msgs__srv__AdvService_Request__Sequence
{
  syst_msgs__srv__AdvService_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} syst_msgs__srv__AdvService_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/AdvService in the package syst_msgs.
typedef struct syst_msgs__srv__AdvService_Response
{
  double response;
} syst_msgs__srv__AdvService_Response;

// Struct for a sequence of syst_msgs__srv__AdvService_Response.
typedef struct syst_msgs__srv__AdvService_Response__Sequence
{
  syst_msgs__srv__AdvService_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} syst_msgs__srv__AdvService_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_H_
