import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self,root):
        self.root=root
        self.root.title("tic tac toe")
        self.board=[""] * 9
        self.current_player = "X"
        self.buttons = []

        self.create_buttons()


    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2, 
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)             
          
    def click_button(self, index):
        if self.buttons[index]["text"] == "" and self.check_wineer() is False:
           self.buttons[index]["text"]=self.current_player
           self.board[index]=self.current_player
        if self.check_wineer():
            messagebox.showinfo(" TIC TAC TOE",f"player {self.current_player} wins!")
            self.reset_game()
        elif "" not in self.board:
             messagebox.showinfo("TIC TAC TOE","its a tie!")  
             self.reset_game()
        else:
            self.current_player= "O" if self.current_player == "X"  else "X"   
    def check_wineer(self):
        win_condition=[(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for conditon in win_condition:
            if self.board[conditon[0]] == self.board[conditon[1]] == self.board[conditon[2]] != "":
                return True
        return False
    def reset_game(self):
        self.board=[""] * 9
        self.current_player= "X"
        for button in self.button:
            button["text"] = ""

if __name__ == "__main__":
            root=tk.Tk()
            game = TicTacToe(root)
            root.mainloop()
        


