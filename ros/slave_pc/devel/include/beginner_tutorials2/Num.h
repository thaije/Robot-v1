// Generated by gencpp from file beginner_tutorials2/Num.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS2_MESSAGE_NUM_H
#define BEGINNER_TUTORIALS2_MESSAGE_NUM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace beginner_tutorials2
{
template <class ContainerAllocator>
struct Num_
{
  typedef Num_<ContainerAllocator> Type;

  Num_()
    : num(0)
    , first_name()
    , last_name()
    , age(0)
    , score(0)  {
    }
  Num_(const ContainerAllocator& _alloc)
    : num(0)
    , first_name(_alloc)
    , last_name(_alloc)
    , age(0)
    , score(0)  {
  (void)_alloc;
    }



   typedef int64_t _num_type;
  _num_type num;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _first_name_type;
  _first_name_type first_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _last_name_type;
  _last_name_type last_name;

   typedef uint8_t _age_type;
  _age_type age;

   typedef uint32_t _score_type;
  _score_type score;




  typedef boost::shared_ptr< ::beginner_tutorials2::Num_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials2::Num_<ContainerAllocator> const> ConstPtr;

}; // struct Num_

typedef ::beginner_tutorials2::Num_<std::allocator<void> > Num;

typedef boost::shared_ptr< ::beginner_tutorials2::Num > NumPtr;
typedef boost::shared_ptr< ::beginner_tutorials2::Num const> NumConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials2::Num_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials2::Num_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace beginner_tutorials2

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'beginner_tutorials2': ['/home/sophie/Bureaublad/Robot/ros/slave_pc/src/beginner_tutorials2/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials2::Num_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials2::Num_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials2::Num_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials2::Num_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials2::Num_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials2::Num_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials2::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "379cbe21d44c48c3d9a5a30aa0ddaafb";
  }

  static const char* value(const ::beginner_tutorials2::Num_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x379cbe21d44c48c3ULL;
  static const uint64_t static_value2 = 0xd9a5a30aa0ddaafbULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials2::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials2/Num";
  }

  static const char* value(const ::beginner_tutorials2::Num_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials2::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 num\n\
string first_name\n\
string last_name\n\
uint8 age\n\
uint32 score\n\
";
  }

  static const char* value(const ::beginner_tutorials2::Num_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials2::Num_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.num);
      stream.next(m.first_name);
      stream.next(m.last_name);
      stream.next(m.age);
      stream.next(m.score);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Num_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::beginner_tutorials2::Num_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials2::Num_<ContainerAllocator>& v)
  {
    s << indent << "num: ";
    Printer<int64_t>::stream(s, indent + "  ", v.num);
    s << indent << "first_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.first_name);
    s << indent << "last_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.last_name);
    s << indent << "age: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.age);
    s << indent << "score: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.score);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS2_MESSAGE_NUM_H
