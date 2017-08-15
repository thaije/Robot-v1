; Auto-generated. Do not edit!


(cl:in-package mastering_ros_demo_pkg-msg)


;//! \htmlinclude demo_msg.msg.html

(cl:defclass <demo_msg> (roslisp-msg-protocol:ros-message)
  ((greeting
    :reader greeting
    :initarg :greeting
    :type cl:string
    :initform "")
   (number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0))
)

(cl:defclass demo_msg (<demo_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <demo_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'demo_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mastering_ros_demo_pkg-msg:<demo_msg> is deprecated: use mastering_ros_demo_pkg-msg:demo_msg instead.")))

(cl:ensure-generic-function 'greeting-val :lambda-list '(m))
(cl:defmethod greeting-val ((m <demo_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mastering_ros_demo_pkg-msg:greeting-val is deprecated.  Use mastering_ros_demo_pkg-msg:greeting instead.")
  (greeting m))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <demo_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mastering_ros_demo_pkg-msg:number-val is deprecated.  Use mastering_ros_demo_pkg-msg:number instead.")
  (number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <demo_msg>) ostream)
  "Serializes a message object of type '<demo_msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'greeting))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'greeting))
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <demo_msg>) istream)
  "Deserializes a message object of type '<demo_msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'greeting) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'greeting) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<demo_msg>)))
  "Returns string type for a message object of type '<demo_msg>"
  "mastering_ros_demo_pkg/demo_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'demo_msg)))
  "Returns string type for a message object of type 'demo_msg"
  "mastering_ros_demo_pkg/demo_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<demo_msg>)))
  "Returns md5sum for a message object of type '<demo_msg>"
  "4d44a7bb82ba135859a5038705fd5c1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'demo_msg)))
  "Returns md5sum for a message object of type 'demo_msg"
  "4d44a7bb82ba135859a5038705fd5c1d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<demo_msg>)))
  "Returns full string definition for message of type '<demo_msg>"
  (cl:format cl:nil "string greeting ~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'demo_msg)))
  "Returns full string definition for message of type 'demo_msg"
  (cl:format cl:nil "string greeting ~%int32 number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <demo_msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'greeting))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <demo_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'demo_msg
    (cl:cons ':greeting (greeting msg))
    (cl:cons ':number (number msg))
))
