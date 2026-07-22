# A helpful calculation tool used to determine component values for the tps54360ddar buck converter IC

# This project optimizes responsiveness over power budget since 
# the source battery is so massive; thus, higher switch frequencies will be prioritized


# Electrical Characteristics
MIN_V_IN = 4.5 # Volts
MAX_V_IN = 60 # Volts
MOSFET_ON_RESISTANCE_MILLIOHMS = 92 # mOhms (typical)
MAX_CONTINUOUS_CURRENT = 3.5 # Amps
MINIMUM_PEAK_INDUCTOR_CURRENT_LIMIT = 4.5 # A


MINIMUM_SWITCHING_FREQUENCY = 100000 # Hz
MAXIMUM_SWITCHING_FREQUENCY = 25000000 # HZ
T_MIN_ON = 135 # ns

# Configurable Mins/Maxed
UVLO_VOLTAGE = 4.3 # Volts ( Default is 4.3 volts )

# Safety Margins
V_IN_MARGIN = .1
I_OUT_MAX_MARGIN = 1
T_MIN_ON_MARGIN = .1
MAX_K_IND_RATIO = .3



from helpers import *

def computeComponentValues(v_in_nominal: float, v_in_max:float, v_out: float, i_out_max: float, catch_diode_voltage: float = .7):
    safe_t_min_on = computeMarginedValue(T_MIN_ON,T_MIN_ON_MARGIN)
    safe_i_out_max = computeMarginedValue(i_out_max, I_OUT_MAX_MARGIN)

    target_switch_frequency = computeOptimalSwitchingSpeed(v_in_nominal,v_out,safe_t_min_on)
    
    # Compute Minimum Viable Inductor Value
    safe_l_out_min = computeMinInductorValue(v_in_max,v_out,safe_i_out_max,target_switch_frequency)
    # Compute Output Capacitor Value


    # Operate on Catch Diode if necessary, currently, the B560C-13-F Catch Schottcky Diode is forward voltage is set to default

    # Input Capacitor Determination (Based on desired ripple)

    # Undervoltage Lockout Set Point Compute

    # Compensation Network Compute

    # Compute Resistor Division for Desired V_Out
    
    return safe_l_out_min


# Compute optimal switching speed from desired parameters (in Hz)
# D = v_out / v_in = t_min_on / t_period
# F = v_out / ( v_in * t_min_on )
# Units:
#   v_in: Volts
#   v_out: Volts
#   t_min_on: nanoseconds
#   
#
def computeOptimalSwitchingSpeed(v_in, v_out, t_min_on):
    t_min_on_seconds = t_min_on * pow(10,-9)
    return round(v_out / ( v_in * t_min_on_seconds))

# Compute Minimum Inductor Value
# Units: 
#   v_in_max: Volts
#   v_out: Volts
#   i_out_max: Amperes
#   switch_frequency: Hz
#
#
def computeMinInductorValue(v_in_max: float,v_out: float, i_out_max: float, switch_frequency: float):
    return ((v_in_max - v_out) / (i_out_max * MAX_K_IND_RATIO)) * v_out / (v_in_max * switch_frequency)