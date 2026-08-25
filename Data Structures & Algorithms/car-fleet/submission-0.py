class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for position, speed in cars:
            speed = ((target - position)/speed)

            if not stack:
                stack.append(speed)
            else:
                if speed > stack[-1]:
                    stack.append(speed)

        return len(stack)