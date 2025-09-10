# SimRacingWheel
# Sim Racing Steering Wheel
**Bilal Qadri — 2025**  
DIY sim racing steering wheel: a 3D-printed enclosure and micro:bit-based controller that emulates an Xbox 360 joystick for racing games.

---

## Quick links
- 📄 Project PDF: `docs/Sim-Wheel-Project.pdf`  
- ▶️ Demo video: *YouTube/Vimeo link (unlisted)*  
- 🧰 CAD files: `cad/`  
- 💻 Code: `code/`

---

## Executive summary
This project produces a low-cost, modular sim-racing steering wheel that maps rotation to an Xbox-compatible joystick input. The goal was to learn embedded programming, CAD, and rapid prototyping while producing a usable racing input device.

**Skills:** Python, sensor fusion, micro:bit, Fusion 360, 3D printing (PLA/PLA-CF), iterative design.  
**Time spent (approx):** 40–60 hours.  
**Material cost (approx):** \$XX (filament, fasteners, button modules).

---

## Features
- micro:bit accelerometer → Python script → vgamepad virtual joystick  
- Modular 3D printed enclosure with snap-fit lid and replaceable handles  
- Desk mount with adjustable clamp  
- PLA-CF final prints for stiffness and finish

---

## Hardware & BOM
See `hardware/BOM.md` or short list below:
- micro:bit (model X)
- Button modules ×12
- Rotary encoders ×3
- Microbit extension board
- PLA-CF filament
- Misc: screws, tape, cardboard (early prototype)

---

## Software
- Python 3.x (vgamepad library) — see `code/README.md` for setup and run instructions.  
- Fusion 360 files in `cad/`.  
- Slicing and print profiles tested in Bambu Studio.

---

## How to run (short)
1. Connect micro:bit to PC via USB.  
2. Run `code/vgamepad_bridge.py` (install dependencies listed in `code/requirements.txt`).  
3. Calibrate center position by holding wheel still for 3s at startup.  
4. Launch supported racing game and select controller input.

---

## Sensor mapping (high-level pseudocode)
angle_raw = read_accel()
angle = compute_rotation_from_accel(angle_raw)
angle = apply_lowpass(angle)
angle = apply_deadzone(angle, threshold=3deg)
joystick = map(angle, -max_angle..+max_angle, -1..1)
send_to_vgamepad(joystick)


---

## Build notes, iterations & lessons
- Potentiometer initially used but found broken → switched to micro:bit accelerometer.  
- Blender model was hollow and unprintable → moved to Fusion 360 for precise dimensions.  
- Printing: iterated 7 times to refine tolerances and support strategy.  
- Final material: PLA-CF for improved stiffness.

---

## Images
![Cover](images/cover.jpg)  
*Figure 1: Final printed wheel — front view.*

---

## Downloads
- Project PDF: `docs/Sim-Wheel-Project.pdf`  
- CAD and STLs: `cad/`

---

## Contact
Bilal Qadri — github.com/your-username • bilal.email@example.com

---

## License
This project is released under the MIT License. See `LICENSE` for details.
