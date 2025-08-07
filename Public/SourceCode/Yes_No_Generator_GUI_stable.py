import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import pyperclip
from collections import deque

class YesNoGenerator:
    def __init__(self):
        self.options = ["Yes", "No"]
        self.counter = 0
        self.counts = {"Yes": 0, "No": 0}
        self.yes_per = 0
        self.no_per = 0
        self.gen_per_sec = 0
        self.reset_per_sec = 0
        self.start_time = time.time()
        self.reset_start_time = time.time()
        self.update_interval = 100  # Update every 100ms
        self.reset_queue = deque()
        self.sliding_window = 10 # window of 10 seconds
        self.reset_queue_clear_threshold = 0
        self.reset_decrese_flag = False

        self.reset_counter = 0
        self.SHOW_RESET = 69

        self.separator_row = 2
        self.text_row = 1

        # GUI
        self.output_label = None
        self.counter_label = None
        self.yes_count_label = None
        self.no_count_label = None
        self.yes_per_label = None
        self.no_per_label = None
        self.message_text = None
        self.reset_label = None
        self.gen_per_sec_label = None
        self.reset_per_sec_label = None

        self.reset_flag = False

        self.output_fg = "black"
        self.output_bg = "#ffffff"
    

        self.message_label = None
        self.welcome_msg = "Welcome to the Yes/No Generator!\nClick \"GENERATE\" to start."
        self.messages = [
            "0. It is true. There is a message number 0.\n(It is on the 0th index, of a list, thats why it is 0.)",
            "1. This is a simple tool to help you make decisions.",
            "2. Remember, the decision is ultimately yours!",
            "3. Use with caution!",
            "4. The generator is not responsible for any decisions made based on its output.",
            "5. Enjoy the randomness!",
            "6. In case the result doesn't suit your needs, just click \"GENERATE\" again.",
            "7. Your indecisiveness brought you here, embrace it!",
            "8. Trust the process!",
            "9. Sometimes, the answer is right in front of you.",
            "10. Don't overthink it, just go with the flow!",
            "11. Let the universe (pseudorandomness) decide your fate.",
            "12. If you still can't decide and the Yes/No Generator doesn't help you, consider asking a friend.",
            "13. Remember, it's just a game, have fun with it!",
            "14. Why can't you be more decisive?",
            "15. The Yes/No Generator has limited number of answers, so use it wisely!",
            "16. If you generate long enough, you might overflow the counter. What will happen then?",
            "17. The Yes/No Generator is not responsible for any existential crises it may cause.",
            "18. Why are you still here? Just decide already!",
            "19. Maybe you should just flip a coin instead.",
            "20. If you can't decide, just remember: Yes is always a good answer! Or is it No? Who knows?",
            "21. 9/10 programmers agree that the Yes/No Generator is generating only \"Yes\" and \"No\" answers. The 10th programmer still can't decide.",
            "22. How many times do you need to click \"GENERATE\" before you realize that the answer is always Yes or No?",
            "23. Are you \"the 10th programmer\"?.",
            "24. If you are still reading this, you might be procrastinating. Just click \"GENERATE\" already!",
            "25. The Yes/No Generator is not a therapist, but it can help you make decisions.",
            "26. Created by QWeuroR, Štetka Štetkovič and Bacil Muchomúrka",
            "27. What is the purpose of \"RESET\" button?",
            "28. ",
            "29. Recommend this tool to your friends, they might be indecisive too!",
            "30. What if the generator outputs \"Maybe\"?",

                                              ]
        self.msg_separator = "\n_____________________________________\n"


    def generate(self):
        return random.choice(self.options)

    def show_gui(self):
        root = tk.Tk()
        root.title("Yes/No Generator")
        # root.geometry("600x750")
        root.minsize(500, 650)
        
        # Create a frame for better organization
        main_frame = tk.Frame(root)
        main_frame.pack(pady=20, expand=True)

        # grid Layout
        BUTTON_ROW = 1
        OUTPUT_ROW = 2
        STATS_HEADER_ROW = 3
        STATS_COUNT_ROW = 4
        STATS_PERCENT_ROW = 5
        GPS_ROW = 6

        # button at the top
        btn = tk.Button(main_frame, text="GENERATE", command=self.update_label, font=("Arial", 18))
        btn.grid(row=BUTTON_ROW, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # reset button
        reset_btn = tk.Button(main_frame, text="RESET", 
                     command=lambda: self.reset(self.welcome_msg, main_frame), 
                     font=("Arial", 18))
        reset_btn.grid(row=BUTTON_ROW, column=2, columnspan=1, pady=10, padx=10, sticky="ew")

        # Output label below the button 
        self.output_label = tk.Label(main_frame, text="", font=("Arial", 28), width=10, height=2, bg=self.output_bg, fg=self.output_fg)
        self.output_label.grid(row=OUTPUT_ROW, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

        # Statistics in a row
        statistics_label = tk.Label(main_frame, text="Statistics", font=("Arial", 16))
        statistics_label.grid(row=STATS_HEADER_ROW, column=0, columnspan=3, pady=10)

        self.counter_label = tk.Label(main_frame, text="Counter: 0", font=("Arial", 14))
        self.counter_label.grid(row=STATS_COUNT_ROW, column=0, padx=10, pady=10)

        self.Yes_count_label = tk.Label(main_frame, text="Yes Counter: 0", font=("Arial", 14))
        self.Yes_count_label.grid(row=STATS_COUNT_ROW, column=1, padx=10, pady=10)

        self.No_count_label = tk.Label(main_frame, text="No Counter: 0", font=("Arial", 14))
        self.No_count_label.grid(row=STATS_COUNT_ROW, column=2, padx=10, pady=10)

        self.Yes_Per_label = tk.Label(main_frame, text="0% Yes", font=("Arial", 14))
        self.Yes_Per_label.grid(row=STATS_PERCENT_ROW, column=0, padx=10, pady=10)

        self.No_Per_label = tk.Label(main_frame, text="0% No", font=("Arial", 14))
        self.No_Per_label.grid(row=STATS_PERCENT_ROW, column=1, padx=10, pady=10)
        # Reset label
        self.reset_label = tk.Label(main_frame, text="", font=("Arial", 14))
        self.reset_label.grid(row=STATS_PERCENT_ROW, column=2, padx=10, pady=10)

        self.gen_per_sec_label = tk.Label(main_frame, text="0.00 Gener./sec", font=("Arial", 14))
        self.gen_per_sec_label.grid(row=GPS_ROW, column=0, padx=10, pady=10)

        self.reset_per_sec_label = tk.Label(main_frame, text="0.00 Reset/sec", font=("Arial", 14))
        self.reset_per_sec_label.grid(row=GPS_ROW, column=1, padx=10, pady=10)

        # Separators
        separator1 = ttk.Separator(main_frame, orient='horizontal')
        separator1.grid(row=self.separator_row, column=0, columnspan=3, sticky='new', pady=0)

        separator2 = ttk.Separator(main_frame, orient='horizontal')
        separator2.grid(row=self.separator_row+1, column=0, columnspan=3, sticky='new', pady=10)


        # Message
        self.print_message(self.welcome_msg, main_frame)

        # Periodic updates
        self.update_periodically(root)


        root.mainloop()

    def update_label(self):
        result = self.generate()
        self.output_label.config(text=result)
        self.counter += 1


        if result == "Yes":
            self.counts["Yes"] += 1
            self.output_fg = "black"
            self.output_bg = "#00ff3c"  
        else:
            self.counts["No"] += 1
            self.output_fg = "black"
            self.output_bg = "#ff0000"
        self.output_label.config(text=result, bg=self.output_bg, fg=self.output_fg)
        
        # Percentages
        self.yes_per = (self.counts["Yes"] / self.counter) * 100
        self.no_per = (self.counts["No"] / self.counter) * 100

        self.counter_label.config(text=f"Counter: {self.counter}")
        self.Yes_count_label.config(text=f"Yes Count: {self.counts['Yes']}")
        self.No_count_label.config(text=f"No Count: {self.counts['No']}")
        self.Yes_Per_label.config(text=f"{self.yes_per:.2f}% Yes")
        self.No_Per_label.config(text=f"{self.no_per:.2f}% No")
           

        self.add_message(self.choose_msg())

    def update_periodically(self, root):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        
        # __________________________ #
        # # # Generations per second #
        if elapsed_time > 0 and self.counter > 0:
            self.gen_per_sec = self.counter / elapsed_time
            self.gen_per_sec_label.config(text=f"{self.gen_per_sec:.2f} Gener./sec")
        
        # _____________________ #
        # # # Resets per second #
        while len(self.reset_queue) > 1 and (self.reset_queue[-1] - self.reset_queue[0]) > self.sliding_window:
            self.reset_queue.popleft()  
        # _________________________________ #
        # # # Calculating Resets per second #
        if self.reset_decrese_flag == False:
            if len(self.reset_queue) > 1:
                avg_reset_time = (self.reset_queue[-1] - self.reset_queue[0]) / (len(self.reset_queue) - 1)
                if avg_reset_time > 0:
                    self.reset_per_sec = 1 / avg_reset_time
            else:
                self.reset_per_sec = 0
        # ______________________________________________ #
        # # # decreasing Resets per second in inactivity #
        self.reset_queue_clear_threshold += 1
        # print(self.reset_queue_clear_threshold)
        if self.reset_queue_clear_threshold >= 50 and len(self.reset_queue) > 0:  
            self.reset_decrese_flag = True
            self.reset_per_sec -= 0.319
            # print("Reset per sec decreased to: ", self.reset_per_sec)
            self.reset_queue_clear_threshold = 49
            if self.reset_per_sec <= 0:
                self.reset_per_sec = 0
                self.reset_queue.clear()  
                self.reset_decrese_flag = False

        # if len(self.reset_queue) > 0: # removing oldest timestamp every periodical update 
        #     self.reset_queue.popleft()



        self.reset_per_sec_label.config(text=f"{self.reset_per_sec:.2f} Reset/sec")

        root.after(self.update_interval, lambda: self.update_periodically(root))

        
        

    def print_message(self, message, main_frame):
 
       text_frame = tk.Frame(main_frame)
       text_frame.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

       scrollbar = tk.Scrollbar(text_frame)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

       self.message_text = tk.Text(text_frame, height=10, width=50,
                                   yscrollcommand=scrollbar.set, wrap=tk.WORD,
                                   font=("Times New Roman", 12))
       self.message_text.tag_configure("center", justify='center')
       
       self.message_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       scrollbar.config(command=self.message_text.yview)

       self.message_text.insert(tk.END, message + self.msg_separator, "center")
            
    def choose_msg(self):
        chosen_msg = random.choice(self.messages)
        
        if self.counter >= 2 and self.yes_per == 50.0:
            chosen_msg = "100. Perfectly balanced...\n...as all things should be."
        if chosen_msg.startswith("28."):
            return "28. You have reset the generator %d times.\nBut what resets the reset counter?" % self.reset_counter
        else:
            return chosen_msg

    def add_message(self, text):
        if hasattr(self, 'message_text'):
            self.message_text.insert(tk.END, text + self.msg_separator, "center")
            self.message_text.see(tk.END)


    def reset(self, msg, frame):
      
        self.reset_counter += 1
        self.counter = 0
        self.counts = {"Yes": 0, "No": 0}
        self.output_label.config(text="")
        self.counter_label.config(text="Counter: 0")
        self.Yes_count_label.config(text="Yes Counter: 0")
        self.No_count_label.config(text="No Counter: 0")
        self.Yes_Per_label.config(text="0% Yes")
        self.No_Per_label.config(text="0% No")
        self.message_text.delete(1.0, tk.END)
        # self.print_message(msg, frame)
        self.reset_queue_clear_threshold = 0
        self.reset_decrese_flag = False
        
        if self.reset_counter == self.SHOW_RESET:
            self.reset_flag = True
            
            nice_message = "69. \tNice...\n...now seriously, why do you keep resetting the generator?\nThe reset counter cannot be reset."
            self.message_text.insert(tk.END, nice_message + self.msg_separator, "center")
        else:
            self.print_message(msg, frame)

        if self.reset_flag:
            self.reset_label.config(text=f"Reset Counter: {self.reset_counter}")
        
        self.reset_queue.append(time.time())
        # print("Reset queue: ", self.reset_queue)


        # reset output window
        self.output_fg = "black"
        self.output_bg = "#ffffff"
        self.output_label.config(bg=self.output_bg, fg=self.output_fg)

        # Reset timer
        self.start_time = time.time() # TOTO MOZNO ZAKOMENTOVAT
        self.gen_per_sec = 0 # TOTO MOZNO ZAKOMENTOVAT
        self.gen_per_sec_label.config(text="0.00 Gener./sec")

if __name__ == "__main__":
    YesNoGenerator().show_gui()