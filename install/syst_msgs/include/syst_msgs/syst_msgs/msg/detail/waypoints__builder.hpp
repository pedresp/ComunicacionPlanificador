// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_
#define SYST_MSGS__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "syst_msgs/msg/detail/waypoints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace syst_msgs
{

namespace msg
{

namespace builder
{

class Init_Waypoints_wps
{
public:
  Init_Waypoints_wps()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::syst_msgs::msg::Waypoints wps(::syst_msgs::msg::Waypoints::_wps_type arg)
  {
    msg_.wps = std::move(arg);
    return std::move(msg_);
  }

private:
  ::syst_msgs::msg::Waypoints msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::syst_msgs::msg::Waypoints>()
{
  return syst_msgs::msg::builder::Init_Waypoints_wps();
}

}  // namespace syst_msgs

#endif  // SYST_MSGS__MSG__DETAIL__WAYPOINTS__BUILDER_HPP_
