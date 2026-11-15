# Non-Preemptive SJF CPU Scheduling Simulator

A desktop GUI application built with Python and Tkinter that simulates the **Non-Preemptive Shortest Job First (SJF)** CPU scheduling algorithm. It dynamically calculates process scheduling metrics and renders a visual Gantt chart of the execution timeline.

## Features
- **Interactive Process Entry:** Add processes with custom Process IDs (supports numeric `1` or prefixed `P1` formats), Arrival Times, and Burst Times.
- **Input Validation:** Prevents duplicate Process IDs, negative values, and zero-burst processes.
- **Automated Metric Calculation:** Computes Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT) for every process, along with overall averages.
- **Dynamic Gantt Chart:** Visually draws the CPU execution timeline and timestamps on an embedded Tkinter canvas.
- **One-Click Reset:** Clear all entries, tables, and charts to run new simulations immediately.

## Scheduling Formulas Used
- **Turnaround Time (TAT)** = `Completion Time - Arrival Time`
- **Waiting Time (WT)** = `Turnaround Time - Burst Time`

## Prerequisites
- **Python 3.x** (Tkinter comes pre-installed with standard Python distributions on Windows and macOS).

## How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/AhsanullahCS/OS-Scheduling-Algorithm-SJF.git](https://github.com/AhsanullahCS/OS-Scheduling-Algorithm-SJF.git)