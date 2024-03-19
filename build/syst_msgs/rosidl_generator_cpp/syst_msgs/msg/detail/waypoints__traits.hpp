// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from syst_msgs:msg/Waypoints.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__MSG__DETAIL__WAYPOINTS__TRAITS_HPP_
#define SYST_MSGS__MSG__DETAIL__WAYPOINTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "syst_msgs/msg/detail/waypoints__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace syst_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Waypoints & msg,
  std::ostream & out)
{
  out << "{";
  // member: wps
  {
    if (msg.wps.size() == 0) {
      out << "wps: []";
    } else {
      out << "wps: [";
      size_t pending_items = msg.wps.size();
      for (auto item : msg.wps) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Waypoints & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: wps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.wps.size() == 0) {
      out << "wps: []\n";
    } else {
      out << "wps:\n";
      for (auto item : msg.wps) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Waypoints & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace syst_msgs

namespace rosidl_generator_traits
{

[[deprecated("use syst_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const syst_msgs::msg::Waypoints & msg,
  std::ostream & out, size_t indentation = 0)
{
  syst_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use syst_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const syst_msgs::msg::Waypoints & msg)
{
  return syst_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<syst_msgs::msg::Waypoints>()
{
  return "syst_msgs::msg::Waypoints";
}

template<>
inline const char * name<syst_msgs::msg::Waypoints>()
{
  return "syst_msgs/msg/Waypoints";
}

template<>
struct has_fixed_size<syst_msgs::msg::Waypoints>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<syst_msgs::msg::Waypoints>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<syst_msgs::msg::Waypoints>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SYST_MSGS__MSG__DETAIL__WAYPOINTS__TRAITS_HPP_
