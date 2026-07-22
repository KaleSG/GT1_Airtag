# Buck Converter Externel Component Selection - TPS54360DDAR

**[Datasheet](https://www.lcsc.com/datasheet/C44377.pdf?spm=wm.sxq.inf.ggs&lcsc_vid=FVlYX11URFJWVAJeRgMIVwcDElULXgBQRlFWBFMDFFgxVlNeQ1RcV11RT1NWVjsOAxUeFF5JWBYZEEoBGA4JCwFIFA4DSA%3D%3D)**

## Typical Application

<img src="img/typical-aplication-TPS54360DDA.png" width="700" alt="Simplied Schematic">

## Use Case Parameter Selection

### Frequency Selection

We will choose our final frequency by first choosing a preliminary frequency using a safety margin on the given minimum on-time and our desired duty cycle:

t_onmin = 142 ns (135 ns with +5% margin)

D = 3.25V / 48V = t_onmin / t_period

1/t_period = 0.0677 / 142 ns
F = 476760.56338 (476 kHz)

### Inductor Selection

We assume K_ind to be .3 as it is the industry standard for typical use cases. High power management is not critical here as power consumption is quite low in the Samsung SmartTag2

<img src="img/Eq-26-Inductor.png" width="700" alt="Simplied Schematic">

L*O(min) = ([54.6V - 3V] / [5.5A * .3]) \* (3V / [54.6V _ 476 kHz])

= 3.61 uH

To achieve the minimum buck inductance, we seek an inductor with a minimum value of 3.61uH

Based on Availability and safety margin, we choose a 4.7uH +- 10% 0805 inductor

The 0805 standard is chosen out of personal preference.

### Output Capacitor Selection

<img src="img/output-cap-eq.png" width="700" alt="Simplied Schematic">

C*OUT > 2 * (50mA) / [476 kHz _ 3.25v]

= 64.6 nF

The output capacitor must have a value of atleast 64.6 nf. Voltage rating is negligible as long as it is above 3.5ish volts for stability.

We will design out output capacitor using a 68nF 0805 ceramic capacitor with a 50V rating due to market supply.

### Catch Diode

We will use the the B560C-13-F schottky diode as our catch diode as a simplicity measure since it is provided by the datasheet. Power loss isn't too applicable in this use case due to the sheer size of the scooter battery and the extremely high power budget alloted.

### Input Capacitor

The TPS54360 requires an input decoupling capacitor of at least 3 uF of effective capacitance. Due to supply and safety margin, we aim for an 100V 0805 ceramic capacitor.

We choose a 4.7 uF 0805 ceramic capacitor for this case.
