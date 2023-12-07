import tkinter as tk
from tkinter import messagebox
from typing import Dict

class Candidate:
    def __init__(self, name: str) -> None:
        self.name = name
        self.votes = 0

class VotingApplication:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Voting App")

        self.candidates: Dict[int, Candidate] = {i: Candidate(name) for i, name in enumerate(["John", "Jane", "Bob", "Alice"], start=1)}
        self.remaining_votes = 4

        self.create_main_menu()

    def create_main_menu(self) -> None:
        self.clear_widgets()

        tk.Label(self.master, text="MAIN MENU", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.master, text="Vote Again", command=self.reset_voting, font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.master, text="Go to Voting", command=self.show_voting_popup, font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Exit", command=self.confirm_exit, font=("Helvetica", 14)).pack(pady=10)

        self.display_vote_totals()

    def show_voting_popup(self) -> None:
        self.clear_widgets()

        if self.remaining_votes > 0:
            tk.Label(self.master, text="Select a candidate to vote or Skip:", font=("Helvetica", 14)).pack(pady=20)

            button_frame = tk.Frame(self.master)
            button_frame.pack(pady=10)

            for candidate_num, candidate in self.candidates.items():
                tk.Button(
                    button_frame,
                    text=f"{candidate_num} - {candidate.name}",
                    command=lambda num=candidate_num: self.cast_vote(num),
                    font=("Helvetica", 12)
                ).pack(side=tk.LEFT, padx=15)

            tk.Button(
                self.master,
                text="Skip",
                command=self.skip_vote,
                font=("Helvetica", 12)
            ).pack(pady=10)

            tk.Label(self.master, text=f"Remaining Votes: {self.remaining_votes}", font=("Helvetica", 12)).pack(pady=10)
        else:
            self.display_final_results()

    def cast_vote(self, candidate_num: int) -> None:
        if self.remaining_votes > 0:
            self.candidates[candidate_num].votes += 1
            self.remaining_votes -= 1
            self.show_voting_popup()

    def skip_vote(self) -> None:
        if self.remaining_votes > 0:
            self.remaining_votes -= 1
            self.show_voting_popup()

    def display_final_results(self) -> None:
        self.clear_widgets()

        tk.Label(self.master, text="Voting has ended. Final results:", font=("Helvetica", 16)).pack(pady=20)

        for candidate_num, candidate in self.candidates.items():
            tk.Label(self.master, text=f"{candidate.name} Votes: {candidate.votes}", font=("Helvetica", 12)).pack()

        tk.Label(self.master, text=f"Overall Total Votes: {self.calculate_overall_total()}", font=("Helvetica", 12)).pack(pady=15)

        self.create_main_menu()

    def reset_voting(self) -> None:
        self.remaining_votes = 4
        self.show_voting_popup()

    def confirm_exit(self) -> None:
        confirmation = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirmation:
            self.master.destroy()

    def clear_widgets(self) -> None:
        for widget in self.master.winfo_children():
            widget.destroy()

    def display_vote_totals(self) -> None:
        for candidate_num, candidate in self.candidates.items():
            tk.Label(self.master, text=f"{candidate.name} Votes: {candidate.votes}", font=("Helvetica", 12)).pack()

        tk.Label(self.master, text=f"Overall Total Votes: {self.calculate_overall_total()}", font=("Helvetica", 12)).pack(pady=15)

    def calculate_overall_total(self) -> int:
        return sum(candidate.votes for candidate in self.candidates.values())

def main() -> None:
    root = tk.Tk()
    root.geometry("800x500")  # Set the initial size of the window
    app = VotingApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
