
(cl:in-package :asdf)

(defsystem "mastering_ros_demo_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "demo_msg" :depends-on ("_package_demo_msg"))
    (:file "_package_demo_msg" :depends-on ("_package"))
  ))