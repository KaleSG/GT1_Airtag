# Buck Converter Externel Component Selection - TPS54360DDAR

**[Datasheet](https://www.lcsc.com/datasheet/C44377.pdf?spm=wm.sxq.inf.ggs&lcsc_vid=FVlYX11URFJWVAJeRgMIVwcDElULXgBQRlFWBFMDFFgxVlNeQ1RcV11RT1NWVjsOAxUeFF5JWBYZEEoBGA4JCwFIFA4DSA%3D%3D)**

## Typical Application

<img src="img/typical-aplication-TPS54360DDA.png" width="700" alt="Simplied Schematic">

## Use Case Parameter Selection

### Frequency Selection

We will choose our final frequency by first choosing a preliminary frequency using a safety margin on the given minimum on-time and our desired duty cycle:

t_onmin = 142 ns (135 ns with +5% margin)

D = 3V / 48V = t_onmin / t_period

1/t_period = 0.0625 / 142 ns
F = 440140.84507 (440 kHz)
