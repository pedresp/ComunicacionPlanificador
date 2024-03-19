// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from syst_msgs:srv/AdvService.idl
// generated code does not contain a copyright notice

#ifndef SYST_MSGS__SRV__DETAIL__ADV_SERVICE__TRAITS_HPP_
#define SYST_MSGS__SRV__DETAIL__ADV_SERVICE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "syst_msgs/srv/detail/adv_service__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace syst_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const AdvService_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: drone_id
  {
    out << "drone_id: ";
    rosidl_generator_traits::value_to_yaml(msg.drone_id, out);
    out << ", ";
  }

  // member: speed
  {
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << ", ";
  }

  // member: tof
  {
    out << "tof: ";
    rosidl_generator_traits::value_to_yaml(msg.tof, out);
    out << ", ";
  }

  // member: ancho_de_barrido
  {
    out << "ancho_de_barrido: ";
    rosidl_generator_traits::value_to_yaml(msg.ancho_de_barrido, out);
    out << ", ";
  }

  // member: coordx
  {
    out << "coordx: ";
    rosidl_generator_traits::value_to_yaml(msg.coordx, out);
    out << ", ";
  }

  // member: coordy
  {
    out << "coordy: ";
    rosidl_generator_traits::value_to_yaml(msg.coordy, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AdvService_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: drone_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "drone_id: ";
    rosidl_generator_traits::value_to_yaml(msg.drone_id, out);
    out << "\n";
  }

  // member: speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << "\n";
  }

  // member: tof
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tof: ";
    rosidl_generator_traits::value_to_yaml(msg.tof, out);
    out << "\n";
  }

  // member: ancho_de_barrido
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ancho_de_barrido: ";
    rosidl_generator_traits::value_to_yaml(msg.ancho_de_barrido, out);
    out << "\n";
  }

  // member: coordx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "coordx: ";
    rosidl_generator_traits::value_to_yaml(msg.coordx, out);
    out << "\n";
  }

  // member: coordy
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "coordy: ";
    rosidl_generator_traits::value_to_yaml(msg.coordy, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AdvService_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace syst_msgs

namespace rosidl_generator_traits
{

[[deprecated("use syst_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const syst_msgs::srv::AdvService_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  syst_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use syst_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const syst_msgs::srv::AdvService_Request & msg)
{
  return syst_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<syst_msgs::srv::AdvService_Request>()
{
  return "syst_msgs::srv::AdvService_Request";
}

template<>
inline const char * name<syst_msgs::srv::AdvService_Request>()
{
  return "syst_msgs/srv/AdvService_Request";
}

template<>
struct has_fixed_size<syst_msgs::srv::AdvService_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<syst_msgs::srv::AdvService_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<syst_msgs::srv::AdvService_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace syst_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const AdvService_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: response
  {
    out << "response: ";
    rosidl_generator_traits::value_to_yaml(msg.response, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AdvService_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "response: ";
    rosidl_generator_traits::value_to_yaml(msg.response, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AdvService_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace syst_msgs

namespace rosidl_generator_traits
{

[[deprecated("use syst_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const syst_msgs::srv::AdvService_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  syst_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use syst_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const syst_msgs::srv::AdvService_Response & msg)
{
  return syst_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<syst_msgs::srv::AdvService_Response>()
{
  return "syst_msgs::srv::AdvService_Response";
}

template<>
inline const char * name<syst_msgs::srv::AdvService_Response>()
{
  return "syst_msgs/srv/AdvService_Response";
}

template<>
struct has_fixed_size<syst_msgs::srv::AdvService_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<syst_msgs::srv::AdvService_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<syst_msgs::srv::AdvService_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<syst_msgs::srv::AdvService>()
{
  return "syst_msgs::srv::AdvService";
}

template<>
inline const char * name<syst_msgs::srv::AdvService>()
{
  return "syst_msgs/srv/AdvService";
}

template<>
struct has_fixed_size<syst_msgs::srv::AdvService>
  : std::integral_constant<
    bool,
    has_fixed_size<syst_msgs::srv::AdvService_Request>::value &&
    has_fixed_size<syst_msgs::srv::AdvService_Response>::value
  >
{
};

template<>
struct has_bounded_size<syst_msgs::srv::AdvService>
  : std::integral_constant<
    bool,
    has_bounded_size<syst_msgs::srv::AdvService_Request>::value &&
    has_bounded_size<syst_msgs::srv::AdvService_Response>::value
  >
{
};

template<>
struct is_service<syst_msgs::srv::AdvService>
  : std::true_type
{
};

template<>
struct is_service_request<syst_msgs::srv::AdvService_Request>
  : std::true_type
{
};

template<>
struct is_service_response<syst_msgs::srv::AdvService_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SYST_MSGS__SRV__DETAIL__ADV_SERVICE__TRAITS_HPP_
