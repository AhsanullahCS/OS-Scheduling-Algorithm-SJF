import tkinter as tk  
from tkinter import ttk, messagebox  
class SJFSimulatorGUI: 
    def __init__(self, root):  
        self.root = root      
        self.root.title("Non-Preemptive SJF Scheduling Simulator") 
        self.root.geometry("750x650")       
        self.root.configure(bg="#f5f5f5")  

        self.processes = [] 
        self.build_ui()    
    def build_ui(self):
        header = tk.Label(self.root,  
            text="Non-Preemptive SJF Scheduling Simulator", 
            font=("Arial", 16, "bold"), 
            bg="#f5f5f5", 
            fg="#333"
        )
        header.pack(pady=10)  
        # Input Frame
        input_frame = tk.LabelFrame( 
            self.root, 
            text=" Add New Process ", 
            font=("Arial", 11, "bold"), 
            bg="#f5f5f5", 
            padx=10, 
            pady=10
        )
        input_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(input_frame, text="Process ID (e.g. 1 or P1):", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
        self.ent_pid = tk.Entry(input_frame, width=8)
        self.ent_pid.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Arrival Time:", bg="#f5f5f5").grid(row=0, column=2, padx=5, pady=5)
        self.ent_at = tk.Entry(input_frame, width=8)
        self.ent_at.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Burst Time:", bg="#f5f5f5").grid(row=0, column=4, padx=5, pady=5)
        self.ent_bt = tk.Entry(input_frame, width=8)
        self.ent_bt.grid(row=0, column=5, padx=5, pady=5)

        btn_add = tk.Button(
            input_frame, 
            text="Add Process", 
            command=self.add_process, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 9, "bold")
        )
        btn_add.grid(row=0, column=6, padx=10, pady=5)

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(fill="x", padx=20, pady=5)

        btn_run = tk.Button(
            btn_frame, 
            text="Run SJF Simulation", 
            command=self.run_sjf, 
            bg="#2196F3", 
            fg="white", 
            font=("Arial", 11, "bold"), 
            padx=15, 
            pady=5
        )
        btn_run.pack(side="left", padx=5)

        btn_reset = tk.Button(
            btn_frame, 
            text="Reset All", 
            command=self.reset_all, 
            bg="#f44336", 
            fg="white", 
            font=("Arial", 11, "bold"), 
            padx=15, 
            pady=5
        )
        btn_reset.pack(side="left", padx=5)

        # Process Table Frame
        table_frame = tk.LabelFrame(
            self.root, 
            text=" Process Metrics Table ", 
            font=("Arial", 11, "bold"), 
            bg="#f5f5f5", 
            padx=10, 
            pady=10
        )
        table_frame.pack(fill="both", expand=True, padx=20, pady=5)

        columns = ("pid", "at", "bt", "ct", "tat", "wt")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=6)
        
        self.tree.heading("pid", text="Process ID")
        self.tree.heading("at", text="Arrival Time")
        self.tree.heading("bt", text="Burst Time")
        self.tree.heading("ct", text="Completion Time")
        self.tree.heading("tat", text="Turnaround Time")
        self.tree.heading("wt", text="Waiting Time")

        for col in columns:
            self.tree.column(col, anchor="center", width=100)

        self.tree.pack(fill="both", expand=True)

        # Summary Averages Label
        self.lbl_avg = tk.Label(
            self.root, 
            text="Average TAT: -  |  Average WT: -", 
            font=("Arial", 11, "bold"), 
            bg="#f5f5f5", 
            fg="#333"
        )
        self.lbl_avg.pack(pady=5)

        # Gantt Chart Canvas Frame
        self.gantt_frame = tk.LabelFrame(
            self.root, 
            text=" Gantt Chart ", 
            font=("Arial", 11, "bold"), 
            bg="#f5f5f5", 
            padx=10, 
            pady=10
        )
        self.gantt_frame.pack(fill="x", padx=20, pady=10)

        self.canvas = tk.Canvas(self.gantt_frame, height=80, bg="white")
        self.canvas.pack(fill="x", expand=True)

    def add_process(self):
        try:
            pid_str = self.ent_pid.get().strip()
            if not pid_str:
                raise ValueError

            # Extract numeric value if user enters 'P1' or 'p1'
            if pid_str.upper().startswith('P'):
                clean_pid = pid_str[1:]
            else:
                clean_pid = pid_str

            pid = int(clean_pid)
            at = int(self.ent_at.get().strip())
            bt = int(self.ent_bt.get().strip())

            if bt <= 0 or at < 0:
                raise ValueError

            # Avoid Duplicate Process ID
            if any(p['id'] == pid for p in self.processes):
                messagebox.showerror("Error", f"Process P{pid} already exists!")
                return

            p = {'id': pid, 'arrival_time': at, 'burst_time': bt}
            self.processes.append(p)
            self.tree.insert("", "end", values=(f"P{p['id']}", p['arrival_time'], p['burst_time'], "-", "-", "-"))

            # Clear entry boxes
            self.ent_pid.delete(0, tk.END)
            self.ent_at.delete(0, tk.END)
            self.ent_bt.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Invalid Input", 
                "Please enter valid non-negative numbers for Arrival/Burst time (Burst Time must be > 0)."
            )

    def run_sjf(self):
        if not self.processes:
            messagebox.showwarning("Warning", "Please add at least one process first!")
            return

        n = len(self.processes)
        completed = 0
        current_time = 0
        is_completed = [False] * n
        gantt_chart = []

        # Non-Preemptive SJF Algorithm Logic
        while completed < n:
            idx = -1
            min_burst = float('inf')

            for i in range(n):
                if self.processes[i]['arrival_time'] <= current_time and not is_completed[i]:
                    if self.processes[i]['burst_time'] < min_burst:
                        min_burst = self.processes[i]['burst_time']
                        idx = i

            if idx == -1:
                current_time += 1
            else:
                p = self.processes[idx]
                start_time = current_time
                completion_time = start_time + p['burst_time']
                turnaround_time = completion_time - p['arrival_time']
                waiting_time = turnaround_time - p['burst_time']

                p['start_time'] = start_time
                p['completion_time'] = completion_time
                p['turnaround_time'] = turnaround_time
                p['waiting_time'] = waiting_time

                gantt_chart.append(p)
                current_time = completion_time
                is_completed[idx] = True
                completed += 1

        # Update Treeview Table
        for item in self.tree.get_children():
            self.tree.delete(item)

        total_tat = 0
        total_wt = 0
        sorted_processes = sorted(self.processes, key=lambda x: x['id'])

        for p in sorted_processes:
            self.tree.insert("", "end", values=(
                f"P{p['id']}", 
                p['arrival_time'], 
                p['burst_time'],
                p['completion_time'], 
                p['turnaround_time'], 
                p['waiting_time']
            ))
            total_tat += p['turnaround_time']
            total_wt += p['waiting_time']

        avg_tat = total_tat / n
        avg_wt = total_wt / n
        self.lbl_avg.config(
            text=f"Average Turnaround Time (TAT): {avg_tat:.2f}  |  Average Waiting Time (WT): {avg_wt:.2f}"
        )

        # Render Gantt Chart
        self.draw_gantt_chart(gantt_chart)

    def draw_gantt_chart(self, gantt_chart):
        self.canvas.delete("all")
        if not gantt_chart:
            return

        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:
            canvas_width = 680

        total_time = gantt_chart[-1]['completion_time']
        start_x = 30
        usable_width = canvas_width - 60
        scale = usable_width / max(total_time, 1)

        y_top = 20
        y_bottom = 50

        # Initial time mark
        first_start = gantt_chart[0]['start_time']
        self.canvas.create_text(
            start_x + (first_start * scale), 
            y_bottom + 12, 
            text=str(first_start), 
            font=("Arial", 9, "bold")
        )

        for p in gantt_chart:
            x1 = start_x + (p['start_time'] * scale)
            x2 = start_x + (p['completion_time'] * scale)

            # Draw execution block box
            self.canvas.create_rectangle(x1, y_top, x2, y_bottom, fill="#e3f2fd", outline="#1565c0", width=2)
            # Process label inside block
            self.canvas.create_text((x1 + x2) / 2, (y_top + y_bottom) / 2, text=f"P{p['id']}", font=("Arial", 10, "bold"), fill="#0d47a1")
            # Completion time tick under box
            self.canvas.create_text(x2, y_bottom + 12, text=str(p['completion_time']), font=("Arial", 9, "bold"))

    def reset_all(self):
        self.processes.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.canvas.delete("all")
        self.lbl_avg.config(text="Average TAT: -  |  Average WT: -")


if __name__ == "__main__":
    root = tk.Tk()
    app = SJFSimulatorGUI(root)
    root.mainloop()