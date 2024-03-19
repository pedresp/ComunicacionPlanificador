// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_H_
#define SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'wps'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/Waypoints in the package syst_msgs.
typedef struct syst_msgs__msg__Waypoints
{
  rosidl_runtime_c__double__Sequence wps;
} syst_msgs__msg__Waypoints;

// Struct for a sequence of syst_msgs__msg__Waypoints.
typedef struct syst_msgs__msg__Waypoints__Sequence
{
  syst_msgs__msg__Waypoints * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} syst_msgs__msg__Waypoints__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_H_
