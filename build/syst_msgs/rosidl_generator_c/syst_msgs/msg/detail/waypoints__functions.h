// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__MSG__DETAIL__WAYPOINTS__FUNCTIONS_H_
#define SYST_MSGS__MSG__DETAIL__WAYPOINTS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "syst_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "syst_msgs/msg/detail/waypoints__struct.h"

/// Initialize msg/Waypoints message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * syst_msgs__msg__Waypoints
 * )) before or use
 * syst_msgs__msg__Waypoints__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__init(syst_msgs__msg__Waypoints * msg);

/// Finalize msg/Waypoints message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
void
syst_msgs__msg__Waypoints__fini(syst_msgs__msg__Waypoints * msg);

/// Create msg/Waypoints message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * syst_msgs__msg__Waypoints__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
syst_msgs__msg__Waypoints *
syst_msgs__msg__Waypoints__create();

/// Destroy msg/Waypoints message.
/**
 * It calls
 * syst_msgs__msg__Waypoints__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
void
syst_msgs__msg__Waypoints__destroy(syst_msgs__msg__Waypoints * msg);

/// Check for msg/Waypoints message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__are_equal(const syst_msgs__msg__Waypoints * lhs, const syst_msgs__msg__Waypoints * rhs);

/// Copy a msg/Waypoints message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__copy(
  const syst_msgs__msg__Waypoints * input,
  syst_msgs__msg__Waypoints * output);

/// Initialize array of msg/Waypoints messages.
/**
 * It allocates the memory for the number of elements and calls
 * syst_msgs__msg__Waypoints__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__Sequence__init(syst_msgs__msg__Waypoints__Sequence * array, size_t size);

/// Finalize array of msg/Waypoints messages.
/**
 * It calls
 * syst_msgs__msg__Waypoints__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
void
syst_msgs__msg__Waypoints__Sequence__fini(syst_msgs__msg__Waypoints__Sequence * array);

/// Create array of msg/Waypoints messages.
/**
 * It allocates the memory for the array and calls
 * syst_msgs__msg__Waypoints__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
syst_msgs__msg__Waypoints__Sequence *
syst_msgs__msg__Waypoints__Sequence__create(size_t size);

/// Destroy array of msg/Waypoints messages.
/**
 * It calls
 * syst_msgs__msg__Waypoints__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
void
syst_msgs__msg__Waypoints__Sequence__destroy(syst_msgs__msg__Waypoints__Sequence * array);

/// Check for msg/Waypoints message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__Sequence__are_equal(const syst_msgs__msg__Waypoints__Sequence * lhs, const syst_msgs__msg__Waypoints__Sequence * rhs);

/// Copy an array of msg/Waypoints messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_syst_msgs
bool
syst_msgs__msg__Waypoints__Sequence__copy(
  const syst_msgs__msg__Waypoints__Sequence * input,
  syst_msgs__msg__Waypoints__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SYST_MSGS__MSG__DETAIL__WAYPOINTS__FUNCTIONS_H_
