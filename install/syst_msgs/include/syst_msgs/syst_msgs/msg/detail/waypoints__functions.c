// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice
#include "syst_msgs/msg/detail/waypoints__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `wps`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
syst_msgs__msg__Waypoints__init(syst_msgs__msg__Waypoints * msg)
{
  if (!msg) {
    return false;
  }
  // wps
  if (!rosidl_runtime_c__double__Sequence__init(&msg->wps, 0)) {
    syst_msgs__msg__Waypoints__fini(msg);
    return false;
  }
  return true;
}

void
syst_msgs__msg__Waypoints__fini(syst_msgs__msg__Waypoints * msg)
{
  if (!msg) {
    return;
  }
  // wps
  rosidl_runtime_c__double__Sequence__fini(&msg->wps);
}

bool
syst_msgs__msg__Waypoints__are_equal(const syst_msgs__msg__Waypoints * lhs, const syst_msgs__msg__Waypoints * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // wps
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->wps), &(rhs->wps)))
  {
    return false;
  }
  return true;
}

bool
syst_msgs__msg__Waypoints__copy(
  const syst_msgs__msg__Waypoints * input,
  syst_msgs__msg__Waypoints * output)
{
  if (!input || !output) {
    return false;
  }
  // wps
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->wps), &(output->wps)))
  {
    return false;
  }
  return true;
}

syst_msgs__msg__Waypoints *
syst_msgs__msg__Waypoints__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__msg__Waypoints * msg = (syst_msgs__msg__Waypoints *)allocator.allocate(sizeof(syst_msgs__msg__Waypoints), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(syst_msgs__msg__Waypoints));
  bool success = syst_msgs__msg__Waypoints__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
syst_msgs__msg__Waypoints__destroy(syst_msgs__msg__Waypoints * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    syst_msgs__msg__Waypoints__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
syst_msgs__msg__Waypoints__Sequence__init(syst_msgs__msg__Waypoints__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__msg__Waypoints * data = NULL;

  if (size) {
    data = (syst_msgs__msg__Waypoints *)allocator.zero_allocate(size, sizeof(syst_msgs__msg__Waypoints), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = syst_msgs__msg__Waypoints__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        syst_msgs__msg__Waypoints__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
syst_msgs__msg__Waypoints__Sequence__fini(syst_msgs__msg__Waypoints__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      syst_msgs__msg__Waypoints__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

syst_msgs__msg__Waypoints__Sequence *
syst_msgs__msg__Waypoints__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__msg__Waypoints__Sequence * array = (syst_msgs__msg__Waypoints__Sequence *)allocator.allocate(sizeof(syst_msgs__msg__Waypoints__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = syst_msgs__msg__Waypoints__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
syst_msgs__msg__Waypoints__Sequence__destroy(syst_msgs__msg__Waypoints__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    syst_msgs__msg__Waypoints__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
syst_msgs__msg__Waypoints__Sequence__are_equal(const syst_msgs__msg__Waypoints__Sequence * lhs, const syst_msgs__msg__Waypoints__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!syst_msgs__msg__Waypoints__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
syst_msgs__msg__Waypoints__Sequence__copy(
  const syst_msgs__msg__Waypoints__Sequence * input,
  syst_msgs__msg__Waypoints__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(syst_msgs__msg__Waypoints);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    syst_msgs__msg__Waypoints * data =
      (syst_msgs__msg__Waypoints *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!syst_msgs__msg__Waypoints__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          syst_msgs__msg__Waypoints__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!syst_msgs__msg__Waypoints__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
