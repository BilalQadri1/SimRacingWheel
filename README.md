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
