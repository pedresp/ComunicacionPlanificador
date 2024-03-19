// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice
#include "syst_msgs/srv/detail/adv_service__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `drone_id`
#include "rosidl_runtime_c/string_functions.h"

bool
syst_msgs__srv__AdvService_Request__init(syst_msgs__srv__AdvService_Request * msg)
{
  if (!msg) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__init(&msg->drone_id)) {
    syst_msgs__srv__AdvService_Request__fini(msg);
    return false;
  }
  // speed
  // tof
  // ancho_de_barrido
  // coordx
  // coordy
  return true;
}

void
syst_msgs__srv__AdvService_Request__fini(syst_msgs__srv__AdvService_Request * msg)
{
  if (!msg) {
    return;
  }
  // drone_id
  rosidl_runtime_c__String__fini(&msg->drone_id);
  // speed
  // tof
  // ancho_de_barrido
  // coordx
  // coordy
}

bool
syst_msgs__srv__AdvService_Request__are_equal(const syst_msgs__srv__AdvService_Request * lhs, const syst_msgs__srv__AdvService_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->drone_id), &(rhs->drone_id)))
  {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // tof
  if (lhs->tof != rhs->tof) {
    return false;
  }
  // ancho_de_barrido
  if (lhs->ancho_de_barrido != rhs->ancho_de_barrido) {
    return false;
  }
  // coordx
  if (lhs->coordx != rhs->coordx) {
    return false;
  }
  // coordy
  if (lhs->coordy != rhs->coordy) {
    return false;
  }
  return true;
}

bool
syst_msgs__srv__AdvService_Request__copy(
  const syst_msgs__srv__AdvService_Request * input,
  syst_msgs__srv__AdvService_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__copy(
      &(input->drone_id), &(output->drone_id)))
  {
    return false;
  }
  // speed
  output->speed = input->speed;
  // tof
  output->tof = input->tof;
  // ancho_de_barrido
  output->ancho_de_barrido = input->ancho_de_barrido;
  // coordx
  output->coordx = input->coordx;
  // coordy
  output->coordy = input->coordy;
  return true;
}

syst_msgs__srv__AdvService_Request *
syst_msgs__srv__AdvService_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Request * msg = (syst_msgs__srv__AdvService_Request *)allocator.allocate(sizeof(syst_msgs__srv__AdvService_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(syst_msgs__srv__AdvService_Request));
  bool success = syst_msgs__srv__AdvService_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
syst_msgs__srv__AdvService_Request__destroy(syst_msgs__srv__AdvService_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    syst_msgs__srv__AdvService_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
syst_msgs__srv__AdvService_Request__Sequence__init(syst_msgs__srv__AdvService_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Request * data = NULL;

  if (size) {
    data = (syst_msgs__srv__AdvService_Request *)allocator.zero_allocate(size, sizeof(syst_msgs__srv__AdvService_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = syst_msgs__srv__AdvService_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        syst_msgs__srv__AdvService_Request__fini(&data[i - 1]);
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
syst_msgs__srv__AdvService_Request__Sequence__fini(syst_msgs__srv__AdvService_Request__Sequence * array)
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
      syst_msgs__srv__AdvService_Request__fini(&array->data[i]);
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

syst_msgs__srv__AdvService_Request__Sequence *
syst_msgs__srv__AdvService_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Request__Sequence * array = (syst_msgs__srv__AdvService_Request__Sequence *)allocator.allocate(sizeof(syst_msgs__srv__AdvService_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = syst_msgs__srv__AdvService_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
syst_msgs__srv__AdvService_Request__Sequence__destroy(syst_msgs__srv__AdvService_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    syst_msgs__srv__AdvService_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
syst_msgs__srv__AdvService_Request__Sequence__are_equal(const syst_msgs__srv__AdvService_Request__Sequence * lhs, const syst_msgs__srv__AdvService_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!syst_msgs__srv__AdvService_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
syst_msgs__srv__AdvService_Request__Sequence__copy(
  const syst_msgs__srv__AdvService_Request__Sequence * input,
  syst_msgs__srv__AdvService_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(syst_msgs__srv__AdvService_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    syst_msgs__srv__AdvService_Request * data =
      (syst_msgs__srv__AdvService_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!syst_msgs__srv__AdvService_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          syst_msgs__srv__AdvService_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!syst_msgs__srv__AdvService_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
syst_msgs__srv__AdvService_Response__init(syst_msgs__srv__AdvService_Response * msg)
{
  if (!msg) {
    return false;
  }
  // response
  return true;
}

void
syst_msgs__srv__AdvService_Response__fini(syst_msgs__srv__AdvService_Response * msg)
{
  if (!msg) {
    return;
  }
  // response
}

bool
syst_msgs__srv__AdvService_Response__are_equal(const syst_msgs__srv__AdvService_Response * lhs, const syst_msgs__srv__AdvService_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // response
  if (lhs->response != rhs->response) {
    return false;
  }
  return true;
}

bool
syst_msgs__srv__AdvService_Response__copy(
  const syst_msgs__srv__AdvService_Response * input,
  syst_msgs__srv__AdvService_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // response
  output->response = input->response;
  return true;
}

syst_msgs__srv__AdvService_Response *
syst_msgs__srv__AdvService_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Response * msg = (syst_msgs__srv__AdvService_Response *)allocator.allocate(sizeof(syst_msgs__srv__AdvService_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(syst_msgs__srv__AdvService_Response));
  bool success = syst_msgs__srv__AdvService_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
syst_msgs__srv__AdvService_Response__destroy(syst_msgs__srv__AdvService_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    syst_msgs__srv__AdvService_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
syst_msgs__srv__AdvService_Response__Sequence__init(syst_msgs__srv__AdvService_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Response * data = NULL;

  if (size) {
    data = (syst_msgs__srv__AdvService_Response *)allocator.zero_allocate(size, sizeof(syst_msgs__srv__AdvService_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = syst_msgs__srv__AdvService_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        syst_msgs__srv__AdvService_Response__fini(&data[i - 1]);
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
syst_msgs__srv__AdvService_Response__Sequence__fini(syst_msgs__srv__AdvService_Response__Sequence * array)
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
      syst_msgs__srv__AdvService_Response__fini(&array->data[i]);
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

syst_msgs__srv__AdvService_Response__Sequence *
syst_msgs__srv__AdvService_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  syst_msgs__srv__AdvService_Response__Sequence * array = (syst_msgs__srv__AdvService_Response__Sequence *)allocator.allocate(sizeof(syst_msgs__srv__AdvService_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = syst_msgs__srv__AdvService_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
syst_msgs__srv__AdvService_Response__Sequence__destroy(syst_msgs__srv__AdvService_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    syst_msgs__srv__AdvService_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
syst_msgs__srv__AdvService_Response__Sequence__are_equal(const syst_msgs__srv__AdvService_Response__Sequence * lhs, const syst_msgs__srv__AdvService_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!syst_msgs__srv__AdvService_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
syst_msgs__srv__AdvService_Response__Sequence__copy(
  const syst_msgs__srv__AdvService_Response__Sequence * input,
  syst_msgs__srv__AdvService_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(syst_msgs__srv__AdvService_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    syst_msgs__srv__AdvService_Response * data =
      (syst_msgs__srv__AdvService_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!syst_msgs__srv__AdvService_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          syst_msgs__srv__AdvService_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!syst_msgs__srv__AdvService_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
