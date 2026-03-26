import math

def projectilemotion_solver(v_i, theta_deg):
    g = 9.8  # acceleration due to gravity in m/s^2
    theta_rad = math.radians(theta_deg)
    
    # Range Formula: R = (v_i^2 * sin(2 * theta)) / g
    range_h = (v_i**2 * math.sin(2 * theta_rad)) / g
    
    # Max Height Formula: h = (v_i^2 * (sin(theta))^2) / (2 * g)
    max_height = (v_i**2 * (math.sin(theta_rad)**2)) / (2 * g)
    
    return range_h, max_height