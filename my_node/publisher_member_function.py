import rclpy
import cv2
import numpy as np
from rclpy.node import Node

from geometry_msgs.msg import Twist


def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY, upORdown
    if event == cv2.EVENT_LBUTTONDOWN:
        img[:, :, :] = 0
        cv2.rectangle(img, (x - 30, y - 30), (x + 30, y + 30), (0, 255, 0), 3)
        cv2.imshow('image', img)
        mouseX, mouseY = x, y
        if mouseY < 256:
            upORdown = 1
        else:
            upORdown = -1


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_circle)
mouseX = 0
mouseY = 0
upORdown = 0


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
    	#k = cv2.waitKey(20) & 0xFF
    	#if k == 27:
        #	break
        k = cv2.waitKey(20) & 0xFF
        msg = Twist()
        msg.linear.x = upORdown * 2.0
        #msg.linear.y = upORdown * 2.0
        #msg.linear.x = 0.0
        #msg.linear.z = 0.0
        #msg.angular.x = 0.0
        #msg.angular.y = 0.0
        #msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing:' )
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

        
    rclpy.spin(minimal_publisher)

   
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



