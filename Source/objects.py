alldata = None
btn2 = None
import config_activate, keyboard

stop = False
def start():
    global alldata
    import tkinter as tk
    hoseleced = tk.StringVar()
    hoseleced.set('Секунд')
    alldata = tk.StringVar()

    def on_select(event):
        # Получаем выделенный элемент из Listbox
        try:
            hoseleced.set(listbox.get(listbox.curselection()))
        except:
            vtw = 1


    label1 = tk.Label(text='Введите время: ', bg=config_activate.config.get('TEXT', 'bgcolor'), fg=config_activate.config.get('TEXT', 'textcolor'))
    label1.pack()
    entry = tk.Entry(bg=config_activate.config.get('TEXT', 'bgcolor'), fg=config_activate.config.get('TEXT', 'textcolor'))
    entry.pack()
    listbox = tk.Listbox(selectmode=tk.SINGLE, bg=config_activate.config.get('TEXT', 'bgcolor'), fg=config_activate.config.get('TEXT', 'textcolor'))
    listbox.pack(padx=50, pady=20)
    listbox.bind("<<ListboxSelect>>", on_select)
    label2 = tk.Label(textvariable=hoseleced, bg=config_activate.config.get('TEXT', 'bgcolor'), fg=config_activate.config.get('TEXT', 'textcolor'))
    label2.pack(padx=50)

    for item in ["Часов", "Минут", "Секунд"]:
        listbox.insert(tk.END, item)
    label3 = tk.Label(textvariable=alldata, bg='#4c594c', fg=config_activate.config.get('TEXT', 'textcolor'))
    def close_sound():
        global stop
        stop = True
        btn2.destroy()
    def convert():
        global stop
        stop = True
        global btn2
        try:
            btn2.destroy()
        except:
            vtw = 1
        btn2 = tk.Button(text='Выключить звук', command=close_sound, bg='#85131a', fg='#548c46')
        label3.pack()
        config_activate.glitter[1] = in_time(entry.get(), hoseleced.get())

    btn = tk.Button(text='Готово!', command=(convert), bg=config_activate.config.get('TEXT', 'bgcolor'), fg=config_activate.config.get('TEXT', 'textcolor'))
    btn.pack(pady=20)
    keyboard.add_hotkey('return', convert)




def in_time(entry, scalar):

    global alldata
    if type(entry) == str:
        try:
            entry = int(entry)
        except:
            alldata.set('Ошибка в типе данных!')

    if type(entry) != str:
        if scalar == 'Часов':
            config_activate.glitter[0] = True
            return entry*60*60

        elif scalar == 'Секунд':
            config_activate.glitter[0] = True
            return entry

        elif scalar == 'Минут':
            config_activate.glitter[0] = True
            return entry*60

        else:
            alldata.set('Ошибка в еденице измерения!')

    else:
        alldata.set('Ошибка в типе данных!')


