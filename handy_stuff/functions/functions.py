
#######################################
# General methods / methods to move the servos
#######################################


# limit a value to a min and max
def clamp(n, minN, maxN):
    return max(min(maxN, n), minN)