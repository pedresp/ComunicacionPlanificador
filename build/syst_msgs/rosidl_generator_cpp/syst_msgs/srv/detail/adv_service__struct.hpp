// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_HPP_
#define SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__syst_msgs__srv__AdvService_Request __attribute__((deprecated))
#else
# define DEPRECATED__syst_msgs__srv__AdvService_Request __declspec(deprecated)
#endif

namespace syst_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AdvService_Request_
{
  using Type = AdvService_Request_<ContainerAllocator>;

  explicit AdvService_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->drone_id = "";
      this->speed = 0.0;
      this->tof = 0.0;
      this->ancho_de_barrido = 0.0;
      this->coordx = 0.0;
      this->coordy = 0.0;
    }
  }

  explicit AdvService_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : drone_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->drone_id = "";
      this->speed = 0.0;
      this->tof = 0.0;
      this->ancho_de_barrido = 0.0;
      this->coordx = 0.0;
      this->coordy = 0.0;
    }
  }

  // field types and members
  using _drone_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _drone_id_type drone_id;
  using _speed_type =
    double;
  _speed_type speed;
  using _tof_type =
    double;
  _tof_type tof;
  using _ancho_de_barrido_type =
    double;
  _ancho_de_barrido_type ancho_de_barrido;
  using _coordx_type =
    double;
  _coordx_type coordx;
  using _coordy_type =
    double;
  _coordy_type coordy;

  // setters for named parameter idiom
  Type & set__drone_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->drone_id = _arg;
    return *this;
  }
  Type & set__speed(
    const double & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__tof(
    const double & _arg)
  {
    this->tof = _arg;
    return *this;
  }
  Type & set__ancho_de_barrido(
    const double & _arg)
  {
    this->ancho_de_barrido = _arg;
    return *this;
  }
  Type & set__coordx(
    const double & _arg)
  {
    this->coordx = _arg;
    return *this;
  }
  Type & set__coordy(
    const double & _arg)
  {
    this->coordy = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    syst_msgs::srv::AdvService_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const syst_msgs::srv::AdvService_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      syst_msgs::srv::AdvService_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      syst_msgs::srv::AdvService_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__syst_msgs__srv__AdvService_Request
    std::shared_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__syst_msgs__srv__AdvService_Request
    std::shared_ptr<syst_msgs::srv::AdvService_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AdvService_Request_ & other) const
  {
    if (this->drone_id != other.drone_id) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->tof != other.tof) {
      return false;
    }
    if (this->ancho_de_barrido != other.ancho_de_barrido) {
      return false;
    }
    if (this->coordx != other.coordx) {
      return false;
    }
    if (this->coordy != other.coordy) {
      return false;
    }
    return true;
  }
  bool operator!=(const AdvService_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AdvService_Request_

// alias to use template instance with default allocator
using AdvService_Request =
  syst_msgs::srv::AdvService_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace syst_msgs


#ifndef _WIN32
# define DEPRECATED__syst_msgs__srv__AdvService_Response __attribute__((deprecated))
#else
# define DEPRECATED__syst_msgs__srv__AdvService_Response __declspec(deprecated)
#endif

namespace syst_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AdvService_Response_
{
  using Type = AdvService_Response_<ContainerAllocator>;

  explicit AdvService_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = 0.0;
    }
  }

  explicit AdvService_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = 0.0;
    }
  }

  // field types and members
  using _response_type =
    double;
  _response_type response;

  // setters for named parameter idiom
  Type & set__response(
    const double & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    syst_msgs::srv::AdvService_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const syst_msgs::srv::AdvService_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      syst_msgs::srv::AdvService_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      syst_msgs::srv::AdvService_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__syst_msgs__srv__AdvService_Response
    std::shared_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__syst_msgs__srv__AdvService_Response
    std::shared_ptr<syst_msgs::srv::AdvService_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AdvService_Response_ & other) const
  {
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const AdvService_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AdvService_Response_

// alias to use template instance with default allocator
using AdvService_Response =
  syst_msgs::srv::AdvService_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace syst_msgs

namespace syst_msgs
{

namespace srv
{

struct AdvService
{
  using Request = syst_msgs::srv::AdvService_Request;
  using Response = syst_msgs::srv::AdvService_Response;
};

}  // namespace srv

}  // namespace syst_msgs

#endif  // SYST_MSGS__SRV__DETAIL__ADV_SERVICE__STRUCT_HPP_
