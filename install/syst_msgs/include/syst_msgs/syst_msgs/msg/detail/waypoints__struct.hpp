// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_HPP_
#define SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__syst_msgs__msg__Waypoints __attribute__((deprecated))
#else
# define DEPRECATED__syst_msgs__msg__Waypoints __declspec(deprecated)
#endif

namespace syst_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Waypoints_
{
  using Type = Waypoints_<ContainerAllocator>;

  explicit Waypoints_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit Waypoints_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _wps_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _wps_type wps;

  // setters for named parameter idiom
  Type & set__wps(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->wps = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    syst_msgs::msg::Waypoints_<ContainerAllocator> *;
  using ConstRawPtr =
    const syst_msgs::msg::Waypoints_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      syst_msgs::msg::Waypoints_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      syst_msgs::msg::Waypoints_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__syst_msgs__msg__Waypoints
    std::shared_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__syst_msgs__msg__Waypoints
    std::shared_ptr<syst_msgs::msg::Waypoints_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Waypoints_ & other) const
  {
    if (this->wps != other.wps) {
      return false;
    }
    return true;
  }
  bool operator!=(const Waypoints_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Waypoints_

// alias to use template instance with default allocator
using Waypoints =
  syst_msgs::msg::Waypoints_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace syst_msgs

#endif  // SYST_MSGS__MSG__DETAIL__WAYPOINTS__STRUCT_HPP_
