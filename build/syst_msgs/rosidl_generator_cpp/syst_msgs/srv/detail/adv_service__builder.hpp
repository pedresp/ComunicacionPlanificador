// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__SRV__DETAIL__ADV_SERVICE__BUILDER_HPP_
#define SYST_MSGS__SRV__DETAIL__ADV_SERVICE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "syst_msgs/srv/detail/adv_service__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace syst_msgs
{

namespace srv
{

namespace builder
{

class Init_AdvService_Request_coordy
{
public:
  explicit Init_AdvService_Request_coordy(::syst_msgs::srv::AdvService_Request & msg)
  : msg_(msg)
  {}
  ::syst_msgs::srv::AdvService_Request coordy(::syst_msgs::srv::AdvService_Request::_coordy_type arg)
  {
    msg_.coordy = std::move(arg);
    return std::move(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

class Init_AdvService_Request_coordx
{
public:
  explicit Init_AdvService_Request_coordx(::syst_msgs::srv::AdvService_Request & msg)
  : msg_(msg)
  {}
  Init_AdvService_Request_coordy coordx(::syst_msgs::srv::AdvService_Request::_coordx_type arg)
  {
    msg_.coordx = std::move(arg);
    return Init_AdvService_Request_coordy(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

class Init_AdvService_Request_ancho_de_barrido
{
public:
  explicit Init_AdvService_Request_ancho_de_barrido(::syst_msgs::srv::AdvService_Request & msg)
  : msg_(msg)
  {}
  Init_AdvService_Request_coordx ancho_de_barrido(::syst_msgs::srv::AdvService_Request::_ancho_de_barrido_type arg)
  {
    msg_.ancho_de_barrido = std::move(arg);
    return Init_AdvService_Request_coordx(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

class Init_AdvService_Request_tof
{
public:
  explicit Init_AdvService_Request_tof(::syst_msgs::srv::AdvService_Request & msg)
  : msg_(msg)
  {}
  Init_AdvService_Request_ancho_de_barrido tof(::syst_msgs::srv::AdvService_Request::_tof_type arg)
  {
    msg_.tof = std::move(arg);
    return Init_AdvService_Request_ancho_de_barrido(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

class Init_AdvService_Request_speed
{
public:
  explicit Init_AdvService_Request_speed(::syst_msgs::srv::AdvService_Request & msg)
  : msg_(msg)
  {}
  Init_AdvService_Request_tof speed(::syst_msgs::srv::AdvService_Request::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_AdvService_Request_tof(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

class Init_AdvService_Request_drone_id
{
public:
  Init_AdvService_Request_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AdvService_Request_speed drone_id(::syst_msgs::srv::AdvService_Request::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_AdvService_Request_speed(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::syst_msgs::srv::AdvService_Request>()
{
  return syst_msgs::srv::builder::Init_AdvService_Request_drone_id();
}

}  // namespace syst_msgs


namespace syst_msgs
{

namespace srv
{

namespace builder
{

class Init_AdvService_Response_response
{
public:
  Init_AdvService_Response_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::syst_msgs::srv::AdvService_Response response(::syst_msgs::srv::AdvService_Response::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::syst_msgs::srv::AdvService_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::syst_msgs::srv::AdvService_Response>()
{
  return syst_msgs::srv::builder::Init_AdvService_Response_response();
}

}  // namespace syst_msgs

#endif  // SYST_MSGS__SRV__DETAIL__ADV_SERVICE__BUILDER_HPP_
