// Auto-generated. Do not edit!

// (in-package mastering_ros_demo_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class demo_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.greeting = null;
      this.number = null;
    }
    else {
      if (initObj.hasOwnProperty('greeting')) {
        this.greeting = initObj.greeting
      }
      else {
        this.greeting = '';
      }
      if (initObj.hasOwnProperty('number')) {
        this.number = initObj.number
      }
      else {
        this.number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type demo_msg
    // Serialize message field [greeting]
    bufferOffset = _serializer.string(obj.greeting, buffer, bufferOffset);
    // Serialize message field [number]
    bufferOffset = _serializer.int32(obj.number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type demo_msg
    let len;
    let data = new demo_msg(null);
    // Deserialize message field [greeting]
    data.greeting = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [number]
    data.number = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.greeting.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mastering_ros_demo_pkg/demo_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4d44a7bb82ba135859a5038705fd5c1d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string greeting 
    int32 number
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new demo_msg(null);
    if (msg.greeting !== undefined) {
      resolved.greeting = msg.greeting;
    }
    else {
      resolved.greeting = ''
    }

    if (msg.number !== undefined) {
      resolved.number = msg.number;
    }
    else {
      resolved.number = 0
    }

    return resolved;
    }
};

module.exports = demo_msg;
