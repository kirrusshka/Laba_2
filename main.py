from tkinter import *
import random
from tkinter import messagebox

# Генерация случайного числа
secret_number = random.randint(1, 100)

def start_game():
    global secret_number
    secret_number = random.randint(1, 100)  # Генерируем новое число при начале игры

    # Очистка окна
    for widget in root.winfo_children():
        widget.destroy()

    # Создание новой страницы с игрой
    game_frame = Frame(root, bg='#b3a068')
    game_frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

    game_title = Label(game_frame, text='Игра: Угадай число!', bg='#ffc18f', font=("Calibri", 20))
    game_title.pack(pady=17)

    guess_label = Label(game_frame, text='Введите ваше число (1-100):', bg='#b3a068', font=("Calibri", 12))
    guess_label.pack(pady=10)

    guess_entry = Entry(game_frame)
    guess_entry.pack(pady=10)

    result_label = Label(game_frame, text='', bg='#b3a068', font=("Calibri", 12))
    result_label.pack(pady=10)

    def check_guess():
        try:
            guess = int(guess_entry.get())
            if guess < 1 or guess > 100:
                result_label.config(text='Число должно быть от 1 до 100!')
            elif guess < secret_number:
                result_label.config(text='Слишком низко!')
            elif guess > secret_number:
                result_label.config(text='Слишком высоко!')
            else:
                result_label.config(text='Поздравляем! Вы угадали число!')
                ask_restart() 
        except ValueError:
            result_label.config(text='Пожалуйста, введите целое число!')

    check_button = Button(game_frame, text='Проверить', bg='#b3a068', font=("Calibri", 13), command=check_guess)
    check_button.pack(pady=20)

def ask_restart():
    response = messagebox.askyesno("Игра завершена", "Хотите сыграть снова?")
    if response:  
        start_game()
    else:  
        root.quit()  

root = Tk()

root['bg'] = '#fff1c7'
root.title('Угадай число')
root.geometry('400x400')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=400, width=400)
canvas.pack()

frame = Frame(root, bg='#b3a068')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(root, text='Угадай число!', bg='#ffc18f', font=("Calibri", 20))
title.pack(pady=17)

btn = Button(frame, text='Начать игру', bg='#b3a068', font=("Calibri", 13), command=start_game)
btn.pack(pady=20)

root.mainloop()
