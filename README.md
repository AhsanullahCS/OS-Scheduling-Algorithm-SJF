# 🖥️ Non-Preemptive SJF Scheduling Simulator

A Python-based GUI application that simulates **Non-Preemptive Shortest Job First (SJF) CPU Scheduling** using Tkinter. It allows users to add processes, execute the scheduling algorithm, calculate performance metrics, and visualize process execution through a Gantt Chart.

---

## 📌 Project Overview

CPU Scheduling is an important concept in Operating Systems. It determines which process gets access to the CPU and in what order.

This project implements the **Non-Preemptive Shortest Job First (SJF)** scheduling algorithm.

In SJF scheduling, the process with the shortest burst time among the currently available processes is selected for execution. Once a process starts executing, it continues until completion.

The application provides an interactive graphical interface to make CPU scheduling easier to understand and visualize.

## ✨ Features

- **Add Processes:** Enter Process ID, Arrival Time, and Burst Time.
- **Input Validation:** Prevents invalid process information and duplicate process IDs.
- **Non-Preemptive SJF Scheduling:** Automatically selects the available process with the shortest burst time.
- **Completion Time (CT):** Calculates the time at which each process finishes.
- **Turnaround Time (TAT):** Calculates the total time spent by a process in the system.
- **Waiting Time (WT):** Calculates how long a process waits before execution.
- **Average TAT:** Calculates average turnaround time.
- **Average WT:** Calculates average waiting time.
- **Gantt Chart:** Provides a visual representation of process execution.
- **Reset Functionality:** Clears processes, scheduling results, and the Gantt Chart.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | GUI development |
| ttk.Treeview | Process metrics table |
| Tkinter Canvas | Gantt Chart visualization |

## 📂 Project Structure

```text
SJF-Scheduling-Simulator/
│
├── sjf_simulator.py
│
├── README.md
│
```

*Note: Add your actual screenshots to the screenshots folder.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/SJF-Scheduling-Simulator.git
```

### 2. Navigate to the Project Directory

```bash
cd SJF-Scheduling-Simulator
```

### 3. Run the Application

```bash
python sjf_simulator.py
```

**Requirements:**
- Python 3.x
- Tkinter (usually included with standard Python installations)

No additional third-party Python packages are required.

## 🧮 Scheduling Algorithm

The project uses the Non-Preemptive Shortest Job First scheduling algorithm.

### How It Works

1. The user enters process information.
2. The application stores processes in a list.
3. The scheduler checks which processes have arrived.
4. Among the available processes, it selects the one with the shortest burst time.
5. The selected process executes until completion.
6. The scheduler calculates CT, TAT, and WT.
7. The process metrics table and Gantt Chart are updated.

### Scheduling Formulas

**Completion Time (CT)**

The time at which a process completes execution.

**Turnaround Time (TAT)**

```text
TAT = Completion Time - Arrival Time
```

**Waiting Time (WT)**

```text
WT = Turnaround Time - Burst Time
```

**Average Turnaround Time**

```text
Average TAT = Total TAT / Number of Processes
```

**Average Waiting Time**

```text
Average WT = Total WT / Number of Processes
```

## 📊 Example Execution

Consider the following processes:

| Process | Arrival Time | Burst Time |
|---|---:|---:|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 2 |

### Execution Order

```text
P1 → P3 → P4 → P2
```

### Gantt Chart

```text
0       7   8    10       14
|  P1   | P3 | P4 |   P2   |
```

### Calculated Results

| Process | CT | TAT | WT |
|---|---:|---:|---:|
| P1 | 7 | 7 | 0 |
| P2 | 14 | 12 | 8 |
| P3 | 8 | 4 | 3 |
| P4 | 10 | 5 | 3 |

**Average Turnaround Time:** 7.00

**Average Waiting Time:** 3.50

## 🎯 Learning Outcomes

Through this project, I practiced and improved my understanding of:

- CPU Scheduling Algorithms.
- Non-Preemptive Scheduling.
- Process Management.
- Completion Time, Turnaround Time, and Waiting Time.
- Python Object-Oriented Programming.
- Tkinter GUI Development.
- Data Visualization using Gantt Charts.
- Event Handling in Python GUI applications.

## 👨‍💻 Author

**Ahsan Ullah**

BS Computer Science Student

National University of Modern Languages (NUML)

GitHub: [AhsanullahCS](https://github.com/AhsanullahCS)

---

## 📜 License

This project is developed for educational purposes as part of Operating Systems coursework.

Feel free to explore, learn, and improve the implementation.

⭐ If you find this project useful, consider giving the repository a star!