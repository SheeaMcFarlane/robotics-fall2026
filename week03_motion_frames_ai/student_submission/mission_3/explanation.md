# Mission 3

## Ai Disclosure

I used ChatGPT to help create a format given specific specifications regarding a closed rectangle pattern. I also used it to debug my code when the compiler wasn't working properly and wasn't finding the file.

## Ai Locked At

2026-09-25T23:25:56.911450+00:00

## Assumptions

Some undocumented assumptions that AI made are that twist commands take effect immediately, timer.cancel() stops future callbacks, the robot is starting in the correct position, no obstacles interferes with the planned route, and wheather or not emergency stops would be needed. 

## Modifications

The big change I made to the code was changing the rounded rectangle implementation so that the curved sections follow the required roolling arc equation v=wr. In the end instead of having linear_x = 0.22 it equals 0.20 being that we are using a turning radius of 25.(0.8*0.25=0.20. I also didn't add a final stop because the ROS wrapper handles the final stop.

## Original Output

#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RoundedRectangle(Node):

    def __init__(self):
        super().__init__('rounded_rectangle')

        # ============================================================
        # Parameters
        # ============================================================

        self.declare_parameter('length', 4.0)
        self.declare_parameter('width', 2.0)
        self.declare_parameter('radius', 0.5)
        self.declare_parameter('linear_velocity_max', 0.5)
        self.declare_parameter('angular_velocity_max', 0.5)

        self.length = self.get_parameter('length').value
        self.width = self.get_parameter('width').value
        self.radius = self.get_parameter('radius').value
        self.linear_velocity_max = self.get_parameter(
            'linear_velocity_max'
        ).value
        self.angular_velocity_max = self.get_parameter(
            'angular_velocity_max'
        ).value

        # ============================================================
        # Check parameters
        # ============================================================

        if self.radius <= 0.0:
            raise ValueError('radius must be greater than 0')

        if self.length <= 2.0 * self.radius:
            raise ValueError(
                'length must be greater than 2 * radius'
            )

        if self.width <= 2.0 * self.radius:
            raise ValueError(
                'width must be greater than 2 * radius'
            )

        if self.linear_velocity_max <= 0.0:
            raise ValueError(
                'linear_velocity_max must be greater than 0'
            )

        if self.angular_velocity_max <= 0.0:
            raise ValueError(
                'angular_velocity_max must be greater than 0'
            )

        # ============================================================
        # Velocity for the arcs
        #
        # v = omega * radius
        #
        # The angular velocity is limited by angular_velocity_max.
        # Therefore:
        #
        # omega = min(angular_velocity_max,
        #             linear_velocity_max / radius)
        #
        # and:
        #
        # v = omega * radius
        #
        # This guarantees the rolling arc equation exactly.
        # ============================================================

        self.angular_velocity_arc = min(
            self.angular_velocity_max,
            self.linear_velocity_max / self.radius
        )

        self.linear_velocity_arc = (
            self.angular_velocity_arc * self.radius
        )

        # ============================================================
        # Straight-line distances
        #
        # Because the corners are rounded, each straight portion
        # is shortened by one radius at each end.
        # ============================================================

        self.straight_length = self.length - 2.0 * self.radius
        self.straight_width = self.width - 2.0 * self.radius

        # ============================================================
        # State machine
        #
        # 0 = straight length
        # 1 = arc
        # 2 = straight width
        # 3 = arc
        # 4 = straight length
        # 5 = arc
        # 6 = straight width
        # 7 = final arc
        # 8 = finished
        # ============================================================

        self.state = 0

        # Time at which the current state started
        self.state_start_time = self.get_clock().now()

        # ============================================================
        # Publisher
        # ============================================================

        self.cmd_vel_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # ============================================================
        # 10 Hz control loop
        # ============================================================

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.get_logger().info(
            'Rounded rectangle controller started.'
        )

    # ================================================================
    # State timing
    # ================================================================

    def state_elapsed(self):
        """Return elapsed time in the current state."""

        now = self.get_clock().now()

        elapsed = (
            now - self.state_start_time
        ).nanoseconds / 1e9

        return elapsed

    # ================================================================
    # Change state
    # ================================================================

    def next_state(self):
        """Move to the next path segment."""

        self.state += 1

        self.state_start_time = self.get_clock().now()

        # There are 8 path segments:
        #
        # straight
        # arc
        # straight
        # arc
        # straight
        # arc
        # straight
        # arc
        #
        # State 8 means the complete path is finished.

        if self.state >= 8:
            self.state = 8

            self.get_logger().info(
                'Closed rounded rectangle completed.'
            )

    # ================================================================
    # Publish velocity
    # ================================================================

    def publish_velocity(self, linear, angular):
        """Publish a Twist command."""

        msg = Twist()

        msg.linear.x = linear
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = angular

        self.cmd_vel_pub.publish(msg)

    # ================================================================
    # Control loop
    # ================================================================

    def control_loop(self):

        # ------------------------------------------------------------
        # Finished
        #
        # Immediately command a complete stop.
        # ------------------------------------------------------------

        if self.state == 8:

            self.publish_velocity(
                0.0,
                0.0
            )

            # Stop the timer so the final command is not followed
            # by another movement command.
            self.timer.cancel()

            return

        # ------------------------------------------------------------
        # State 0: Straight along length
        # ------------------------------------------------------------

        if self.state == 0:

            duration = (
                self.straight_length /
                self.linear_velocity_max
            )

            self.publish_velocity(
                self.linear_velocity_max,
                0.0
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 1: First quarter-circle
        # ------------------------------------------------------------

        elif self.state == 1:

            # Arc length = pi*r/2
            arc_length = (
                math.pi * self.radius / 2.0
            )

            duration = (
                arc_length /
                self.linear_velocity_arc
            )

            self.publish_velocity(
                self.linear_velocity_arc,
                self.angular_velocity_arc
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 2: Straight along width
        # ------------------------------------------------------------

        elif self.state == 2:

            duration = (
                self.straight_width /
                self.linear_velocity_max
            )

            self.publish_velocity(
                self.linear_velocity_max,
                0.0
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 3: Second quarter-circle
        # ------------------------------------------------------------

        elif self.state == 3:

            arc_length = (
                math.pi * self.radius / 2.0
            )

            duration = (
                arc_length /
                self.linear_velocity_arc
            )

            self.publish_velocity(
                self.linear_velocity_arc,
                self.angular_velocity_arc
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 4: Straight along length
        # ------------------------------------------------------------

        elif self.state == 4:

            duration = (
                self.straight_length /
                self.linear_velocity_max
            )

            self.publish_velocity(
                self.linear_velocity_max,
                0.0
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 5: Third quarter-circle
        # ------------------------------------------------------------

        elif self.state == 5:

            arc_length = (
                math.pi * self.radius / 2.0
            )

            duration = (
                arc_length /
                self.linear_velocity_arc
            )

            self.publish_velocity(
                self.linear_velocity_arc,
                self.angular_velocity_arc
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 6: Straight along width
        # ------------------------------------------------------------

        elif self.state == 6:

            duration = (
                self.straight_width /
                self.linear_velocity_max
            )

            self.publish_velocity(
                self.linear_velocity_max,
                0.0
            )

            if self.state_elapsed() >= duration:
                self.next_state()

        # ------------------------------------------------------------
        # State 7: Final quarter-circle
        # ------------------------------------------------------------

        elif self.state == 7:

            arc_length = (
                math.pi * self.radius / 2.0
            )

            duration = (
                arc_length /
                self.linear_velocity_arc
            )

            self.publish_velocity(
                self.linear_velocity_arc,
                self.angular_velocity_arc
            )

            if self.state_elapsed() >= duration:
                # The fourth arc is complete.
                #
                # Immediately transition to the finished state.
                self.next_state()

                # Immediately publish zero velocity.
                self.publish_velocity(
                    0.0,
                    0.0
                )

                # Stop future movement commands.
                self.timer.cancel()


# ====================================================================
# Main
# ====================================================================

def main(args=None):

    rclpy.init(args=args)

    node = RoundedRectangle()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        # Always send a final zero-velocity command when shutting down.
        node.publish_velocity(0.0, 0.0)

        node.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Original Prompt

Write a complete,  ROS 2 Python code that commands a mobile robot to drive a closed rounded rectangle path and stops cleanly once completed.

Inputs & Parameters:
- length (total length of the rectangle layout)
- width (total width of the rectangle layout)
- radius (turning radius for corner arcs)
- linear_velocity_max (velocity limit for moving straight)
- angular_velocity_max  (velocity limit for rotating)
Coordinate Conventions
-X-axis is forward, Y-axis is left, and turning is counter-clockwise
Velocity:
- Straight line segments must move at max_linear_velocity and curved corner arcs must move at the linear speed to strictly satisfy the rolling arc equation: v = angular_velocity * radius.
Output Requirements:
- Continually publish  velocity messages to the '/cmd_vel' at a stable rate of 10Hz.
Stopping Behavior & Loop Closure Test:
- Once the final 4th arc is completed, the node must immediately publish zero velocities (linear.x = 0.0, angular.z = 0.0) to bring the robot to a complete halt.



## Problems

Some things that need verification are the final stop behavior states that after the final arc is completed then the robot should stop but what happens when the the robot doesn't complete that final arc, then what and the robot being commanded using timed velocities assuming the robot travels the expected distance.

## Remaining Limits

The seven tests do not prove that the robot physically drive the exact intended closed rounded rectangle shape. It also doesn't account for real world factors such as wheel slip, timing, and robot behavior could affect the drive path. The ROS run and evaluator provide additional evidence, but there is still some risks that the physical path will not be perfectly accurate.

## Specification

For creation of a closed rounded rectangle I would need the following:
Inputs: length, width, radius, and velocity(linear and angular)
Output: Message in tf2 echo tool terminal that updates at 10Hz 
Coordinate conventions: x-axis is to move forward, y value is to move left and radius to turn
Velocity limits: Straight line limit should be the max linear velocity and curved arcs limit should be (v=angular velocity *turning radius)
Stopping behavior: Zero velocities should appear upon completing the final arc loop and shut down when it is safe to do so
Test expectations:The robot must be able to trace a complete rectangle loop and return to it starting coordinate (0,0) so that it's a closed rounded rectangle


## Test Argument

The test are used to check for safety and the basic structure requirements. Test_nonempty makes sure the pattern has at least three segments, rejecting a pattern that is empty or incomplete.  Test_segment_types makes sure every segment is a valid segment object. Test_positive_durations rules out segments that have zero or negative durations. Test_linear_limits makes sure the linear velocity never exceeds 0.22. Test_angular_limits makes sure the angular velocity never exceeds 0.8. Test_pattern_contains_motion makes sure the pattern actually contains motion. Test_pattern_contains_turning makes sure the pattern contains a turn.
