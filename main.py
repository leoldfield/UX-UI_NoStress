import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
from pygame import mixer
import winsound

#Basic functions
def swapFrame(dest):
    dest.tkraise()

def play_sound():
    count = 5
    while count > 0:
        winsound.Beep(2000, 440)
        count-=1
    

#Classes
class User:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood
    
    def updateName(self, newName):
        self.name = newName

    def updateMood(self, newMood):
        self.mood = newMood



#Window
window = tk.Tk()
window.title("NoStress")
window.geometry('450x700')
window.resizable(False, False)

#Header background
header_bg_path = "resources\\header_beach.jpg"
header_bg_orig = Image.open(header_bg_path)
header_bg_resize = header_bg_orig.resize((450, 200))
header_bg = ImageTk.PhotoImage(header_bg_resize)

#Header bar
header_frame = tk.Frame(window, width=450, height=200)
header_frame.pack()

header_bg_label = tk.Label(header_frame, image = header_bg)
header_bg_label.place(x=0, y=0, width=450, height=200)
header_bg_label.pack()

#Body frame
body_bg_path = "resources\\body_bg.jpg"
body_bg_orig = Image.open(body_bg_path)
body_bg_resize = body_bg_orig.crop((0, 0, 460, 410))
body_bg = ImageTk.PhotoImage(body_bg_resize)


body_frame = tk.Frame(window)
#body_canvas = Canvas(body_frame)
#body_canvas.pack(side = tk.TOP, fill = "both", expand = True)

#body_canvas.create_image(0, 0, image = body_bg, anchor = "nw")
body_frame.pack(side = tk.TOP, fill = "both", expand = True)


#Footer frame
footer_frame = tk.Frame(window, width = 450, height = 100, bg="#234265")
footer_frame.pack()

button_frame_footer = tk.Frame(footer_frame, bg="#234265", width=400, height=90)
button_frame_footer.pack()
button_frame_footer.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #Footer icons
home_icon_path = "resources\\home_icon.png"
home_icon_orig = Image.open(home_icon_path)
home_icon_resize = home_icon_orig.resize((50, 50))
home_icon = ImageTk.PhotoImage(home_icon_resize)
profile_icon_path = "resources\\profile_icon.png"
profile_icon_orig = Image.open(profile_icon_path)
profile_icon_resize = profile_icon_orig.resize((50, 50))
profile_icon = ImageTk.PhotoImage(profile_icon_resize)
settings_icon_path = "resources\\settings_icon.png"
settings_icon_orig = Image.open(settings_icon_path)
settings_icon_resize = settings_icon_orig.resize((50, 50))
settings_icon = ImageTk.PhotoImage(settings_icon_resize)

home_icon_label = tk.Button(button_frame_footer, text="home", image=home_icon, bg="#234265", relief="flat", command = lambda:swapFrame(home_frame))
profile_icon_label = tk.Button(button_frame_footer, text="profile", image=profile_icon, bg="#234265", relief="flat", command = lambda:swapFrame(home_frame))
settings_icon_label = tk.Button(button_frame_footer, text="settings", image=settings_icon, bg="#234265", relief="flat", command = lambda:swapFrame(home_frame))

home_icon_label.grid(row=0, column=0, padx=50)
profile_icon_label.grid(row=0, column=2, padx=50)
settings_icon_label.grid(row=0, column=4, padx=50)

#Home screen
home_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
home_frame.pack()
home_frame.place(x=0, y=0, anchor=tk.NW)

button_frame_home = tk.Frame(home_frame, bg="#E7F4F5")
button_frame_home.pack()
button_frame_home.place(relx=0.5, rely=0, anchor=tk.N)

home_button_1 = tk.Button(button_frame_home, text="Start Break Timer", bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 22), command = lambda:swapFrame(timer_frame))
home_button_1.pack(fill="x", pady=20)
home_button_2 = tk.Button(button_frame_home, text="Meditation Exercises", bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 22),  command = lambda:swapFrame(medit_sel_frame))
home_button_2.pack(fill="x", pady=20)
home_button_3 = tk.Button(button_frame_home, text="How Stressed Am I?", bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 22),  command = lambda:swapFrame(quiz_frame))
home_button_3.pack(fill="x", pady=20)
home_button_4 = tk.Button(button_frame_home, text="Monitor Your Stress", bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 22),  command = lambda:swapFrame(review_frame))
home_button_4.pack(fill="x", pady=20)


#Timer screen
timer_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
timer_frame.pack()
timer_frame.place(x=0, y=0, anchor=tk.NW)

timer_icon_path = "resources\\timer_icon.png"
timer_icon_orig = Image.open(timer_icon_path)
timer_icon_resize = timer_icon_orig.resize((60, 60))
timer_icon = ImageTk.PhotoImage(timer_icon_resize)

#Timer duration function
def setTimerDuration(duration):
    global timer_duration
    timer_duration = duration
    timer_stop == False

timer_duration = 0
timer_stop = False

#Countdown function
def countdownTimer(duration, timer_label, target_frame, home_frame):
    swapFrame(target_frame)
    if duration > -1:
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text="\n" + timeformat)
        timer_label.after(1000, countdownTimer, duration -1, timer_label, target_frame, home_frame)
    else:
        play_sound()
        swapFrame(home_frame)

timer_options_frame = tk.Frame(timer_frame, bg="#E7F4F5")
timer_options_frame.pack(pady = 200)
timer_options_frame.place(relx=0.5, rely=1, anchor=tk.S)

timer_op1_frame = tk.Frame(timer_options_frame, bg="#E7F4F5")
timer_op1_frame.pack()
timer_op1_entry_var = tk.IntVar()
timer_op1_entry = tk.Entry(timer_op1_frame, textvariable=timer_op1_entry_var, font=("Helvetica", 14))
timer_op1 = tk.Button(timer_op1_frame, text="Set Duration\n(minutes)", width=20, height=2, bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 16), command = lambda:setTimerDuration(timer_op1_entry_var.get()*60))

timer_op1_entry.pack(pady=12)
timer_op1.pack(pady=20)

#timer_op2_frame = tk.Frame(timer_options_frame)
#timer_op2_frame.pack(side="left")
#timer_op2 = tk.Button(timer_op2_frame, text="Stop Timer", bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", font=("Helvetica", 12), command = lambda:stopCountdown(countdownTimer, timer_button_frame))

#timer_op2.pack(pady=20)

timer_countdown_frame = tk.Frame(timer_frame, bg="#E7F4F5")
timer_countdown_frame.pack()
timer_countdown_frame.place(relx=0.5, rely=0, anchor=tk.N)

countdown_label = tk.Label(timer_countdown_frame, text="\nTimer", compound=tk.TOP, font=("Helvetica", 24), width = 250, height = 200, image = timer_icon, bg="#205B95", fg="white")
countdown_label.pack(pady = 20)

timer_button_frame = tk.Frame(timer_frame, bg="#E7F4F5")
timer_button_frame.pack()
timer_button_frame.place(relx=0.5, rely=0, anchor=tk.N)

timer_button = tk.Button(timer_button_frame, text="\nStart Timer", compound=tk.TOP, font=("Helvetica", 24), width = 250, height = 200, image = timer_icon, bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", relief="groove", command = lambda:countdownTimer(timer_duration, countdown_label, timer_countdown_frame, timer_button_frame))
timer_button.pack(pady = 20)


#Meditation select screen
medit_sel_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
medit_sel_frame.pack()
medit_sel_frame.place(x=0, y=0, anchor=tk.NW)

medit_opt_frame = tk.Frame(medit_sel_frame, bg="#E7F4F5")
medit_opt_frame.pack()

    #Meditation images
medit1_path = "resources\\medit1.png"
medit1_orig = Image.open(medit1_path)
medit1_resize = medit1_orig.resize((350, 350))
medit1 = ImageTk.PhotoImage(medit1_resize)
medit2_path = "resources\\medit2.png"
medit2_orig = Image.open(medit2_path)
medit2_resize = medit2_orig.resize((200, 200))
medit2 = ImageTk.PhotoImage(medit2_resize)
medit3_path = "resources\\medit3.png"
medit3_orig = Image.open(medit3_path)
medit3_resize = medit3_orig.resize((200, 200))
medit3 = ImageTk.PhotoImage(medit3_resize)
medit4_path = "resources\\medit4.png"
medit4_orig = Image.open(medit4_path)
medit4_resize = medit4_orig.resize((200, 200))
medit4 = ImageTk.PhotoImage(medit4_resize)
medit5_path = "resources\\medit5.png"
medit5_orig = Image.open(medit5_path)
medit5_resize = medit5_orig.resize((200, 200))
medit5 = ImageTk.PhotoImage(medit5_resize)


medit_opt1 = tk.Button(medit_opt_frame, image = medit1, compound = tk.CENTER, width = 350, height = 100, relief="ridge", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:swapFrame(gmed_frame))
medit_opt1.pack(pady=20)

medit_row1 = tk.Frame(medit_sel_frame, bg="#E7F4F5")
medit_row1.pack()
medit_opt2 = tk.Button(medit_row1, image = medit2, compound = tk.CENTER, width = 175, height = 100, relief="ridge", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:swapFrame(breath_frame))
medit_opt2.pack(side="left", padx = 20)
medit_opt3 = tk.Button(medit_row1, image = medit3, compound = tk.CENTER, width = 175, height = 100, relief="ridge", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:swapFrame(bscan_frame))
medit_opt3.pack(side="left", padx = 20)

medit_row2 = tk.Frame(medit_sel_frame, bg="#E7F4F5")
medit_row2.pack()
medit_opt4 = tk.Button(medit_row2, image = medit4, compound = tk.CENTER, width = 175, height = 100, relief="ridge", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#D0DFF5", command = lambda:swapFrame(gimg_frame))
medit_opt4.pack(side="left", pady=10, padx = 20)
medit_opt5 = tk.Button(medit_row2, image = medit5, compound = tk.CENTER, width = 175, height = 100, relief="ridge", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#D0DFF5", command = lambda:swapFrame(exercise_frame))
medit_opt5.pack(side="left", pady=10, padx = 20)



#Guided meditation screen
gmed_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
gmed_frame.pack()
gmed_frame.place(x=0, y=0, anchor=tk.NW)

gmed_content_frame = tk.Frame(gmed_frame, bg="#E7F4F5")
gmed_content_frame.pack()
gmed_content_frame.place(relx=0.5, rely=0, anchor=tk.N)

gmed_play_path = "resources\\gmed_play.png"
gmed_play_orig = Image.open(gmed_play_path)
gmed_play_resize = gmed_play_orig.resize((350, 233))
gmed_play = ImageTk.PhotoImage(gmed_play_resize)
gmed_pause_path = "resources\\gmed_pause.png"
gmed_pause_orig = Image.open(gmed_pause_path)
gmed_pause_resize = gmed_pause_orig.resize((350, 233))
gmed_pause = ImageTk.PhotoImage(gmed_pause_resize)

if mixer.get_init() == None:
    mixer.init()

gmed_paused = False

def play_gmed():
    global gmed_paused
    global gmed_play
    global gmed_pause
    if str(gmed_content.cget("image")) == str(gmed_play):
        gmed_content.config(image = gmed_pause)
        if gmed_paused or mixer.music.get_busy():
            mixer.music.unpause()
            gmed_paused = False
        else:
            mixer.music.load("resources\\meditation.mp3")
            mixer.music.play()
    else:
        gmed_content.config(image = gmed_play)
        mixer.music.pause()
        gmed_paused = True

def stop_gmed():
    global medit_paused
    mixer.music.stop()
    gmed_content.config(image = gmed_play)

gmed_title = tk.Label(gmed_content_frame, text="Daily Guided Meditation", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
gmed_title.pack(pady=10)

gmed_content = tk.Button(gmed_content_frame, image = gmed_play, compound = tk.CENTER, width = 350, height = 233, relief="flat", font=("Helvetica", 22, "bold"), fg="black", command = play_gmed)
gmed_content.pack()

gmed_stop = tk.Button(gmed_content_frame, text="Stop", relief="groove", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = stop_gmed)
gmed_stop.pack(pady = 10)


#Breathing exercises screen
breath_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
breath_frame.pack()
breath_frame.place(x=0, y=0, anchor=tk.NW)

breath_content_frame = tk.Frame(breath_frame, bg="#E7F4F5")
breath_content_frame.pack()
breath_content_frame.place(relx=0.5, rely=0, anchor=tk.N)

breath_img_path = "resources\\breath.png"
breath_img_orig = Image.open(breath_img_path)
breath_img_resize = breath_img_orig.resize((350, 200))
breath_img = ImageTk.PhotoImage(breath_img_resize)

def start_breathe():
    global breath_stop
    breath_stop = False
    breathe()

def stop_breathe():
    global breath_stop
    breath_stop = True

def breathe():
    cycles = 6
    breath_in = 4
    breath_hold = 7
    breath_out = 8

    for i in range(cycles):
        if breath_stop == True:
            breath_text["text"] = "Breathing Exercise"
            break

        #Breathe in
        start_time = time.time()
        while time.time() < start_time + breath_in:
            window.update()
            time_left = int(start_time + breath_in - time.time())
            breath_text["text"] = "Inhale for\n" + str(time_left) + " seconds"
        
        if breath_stop == True:
            breath_text["text"] = "Breathing Exercise"
            break
        
        #Hold breath
        start_time = time.time()
        while time.time() < start_time + breath_hold:
            window.update()
            time_left = int(start_time + breath_hold - time.time())
            breath_text["text"] = "Hold your breath for\n" + str(time_left) + " seconds"

        if breath_stop == True:
            breath_text["text"] = "Breathing Exercise"
            break

        #Breathe out
        start_time = time.time()
        while time.time() < start_time + breath_out:
            window.update()
            time_left = int(start_time + breath_out - time.time())
            breath_text["text"] = "Exhale for\n" + str(time_left) + " seconds"
    
    breath_text["text"] = "Breathing Exercise"
    

breath_text = tk.Label(breath_content_frame, text="Breathing Exercise", image=breath_img, compound = tk.CENTER, font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="black")
breath_button = tk.Button(breath_content_frame, text="Begin", font=("Helvetica", 16, "bold"), width = 10, height = 1, bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = start_breathe)
breath_stop = tk.Button(breath_content_frame, text="Stop", font=("Helvetica", 16, "bold"), width = 10, height = 1, bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = stop_breathe)
breath_text.pack(pady=20)
breath_button.pack(side="left", padx=10, pady=20)
breath_stop.pack(side="left", padx=10, pady=20)


#Body scan screen
bscan_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
bscan_frame.pack()
bscan_frame.place(x=0, y=0, anchor=tk.NW)

bscan_content_frame = tk.Frame(bscan_frame, bg="#E7F4F5")
bscan_content_frame.pack()
bscan_content_frame.place(relx=0.5, rely=0, anchor=tk.N)

bscan_play_path = "resources\\bscan_play.jpg"
bscan_play_orig = Image.open(bscan_play_path)
bscan_play_resize = bscan_play_orig.resize((350, 233))
bscan_play = ImageTk.PhotoImage(bscan_play_resize)
bscan_pause_path = "resources\\bscan_pause.jpg"
bscan_pause_orig = Image.open(bscan_pause_path)
bscan_pause_resize = bscan_pause_orig.resize((350, 233))
bscan_pause = ImageTk.PhotoImage(bscan_pause_resize)

if mixer.get_init() == None:
    mixer.init()

bscan_paused = False

def play_bscan():
    global bscan_paused
    global bscan_play
    global bscan_pause
    if str(bscan_content.cget("image")) == str(bscan_play):
        bscan_content.config(image = bscan_pause)
        if bscan_paused or mixer.music.get_busy():
            mixer.music.unpause()
            bscan_paused = False
        else:
            mixer.music.load("resources\\body_scan.mp3")
            mixer.music.play()
    else:
        bscan_content.config(image = bscan_play)
        mixer.music.pause()
        bscan_paused = True

def stop_bscan():
    global bscan_paused
    mixer.music.stop()
    bscan_paused = False
    bscan_content.config(image = bscan_play)

bscan_title = tk.Label(bscan_content_frame, text="Body Scan", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
bscan_title.pack(pady=10)

bscan_content = tk.Button(bscan_content_frame, image = bscan_play, compound = tk.CENTER, width = 350, height = 233, relief="flat", font=("Helvetica", 22, "bold"), fg="white", command = play_bscan)
bscan_content.pack()

bscan_stop = tk.Button(bscan_content_frame, text="Stop", relief="groove", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = stop_bscan)
bscan_stop.pack(pady = 10)


#Guided imagery screen
gimg_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
gimg_frame.pack()
gimg_frame.place(x=0, y=0, anchor=tk.NW)

gimg_content_frame = tk.Frame(gimg_frame, bg="#E7F4F5")
gimg_content_frame.pack()
gimg_content_frame.place(relx=0.5, rely=0, anchor=tk.N)

gimg_play_path = "resources\\gimg_play.jpg"
gimg_play_orig = Image.open(gimg_play_path)
gimg_play_resize = gimg_play_orig.resize((350, 233))
gimg_play = ImageTk.PhotoImage(gimg_play_resize)
gimg_pause_path = "resources\\gimg_pause.jpg"
gimg_pause_orig = Image.open(gimg_pause_path)
gimg_pause_resize = gimg_pause_orig.resize((350, 233))
gimg_pause = ImageTk.PhotoImage(gimg_play_resize)

if mixer.get_init() == None:
    mixer.init()

gimg_paused = False

def play_gimg():
    global gimg_paused
    global gimg_play
    global gimg_pause
    if str(gimg_content.cget("image")) == str(gimg_play):
        gimg_content.configure(image = gimg_pause)
        if gimg_paused or mixer.music.get_busy():
            mixer.music.unpause()
            gimg_paused = False
        else:
            mixer.music.load("resources\\guided_imagery.mp3")
            mixer.music.play()
    else:
        gimg_content.configure(image = gimg_play)
        mixer.music.pause()
        gimg_paused = True

def stop_gimg():
    global gimg_paused
    gimg_paused = False
    mixer.music.stop()
    gimg_content.configure(image = gimg_play)

gimg_title = tk.Label(gimg_content_frame, text="Guided Imagery", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
gimg_title.pack(pady=10)

gimg_content = tk.Button(gimg_content_frame, image = gimg_play, compound = tk.CENTER, width = 350, height = 233, relief="flat", font=("Helvetica", 22, "bold"), fg="white", command = play_gimg)
gimg_content.pack()

gimg_stop = tk.Button(gimg_content_frame, text="Stop", relief="groove", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = stop_gimg)
gimg_stop.pack(pady = 10)


#Exercise screen
exercise_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
exercise_frame.pack()
exercise_frame.place(x=0, y=0, anchor=tk.NW)

exercise_content_frame = tk.Frame(exercise_frame, bg="#E7F4F5")
exercise_content_frame.pack()
exercise_content_frame.place(relx=0.5, rely=0, anchor=tk.N)

exercise_stop = False
#Exercise countdown
def exerciseCountdown(duration, timer_label):
    if duration > -1:
        if exercise_stop == True:
            timer_label["text"] = "Ready to Start"
            return
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        timer_label.after(1000, exerciseCountdown, duration -1, timer_label)
    else:
        play_sound()
        timer_label["text"] = "Finished"

exercise_today = tk.Label(exercise_content_frame, text="Today's Daily Exercise:\n1 Minute Walk", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
exercise_timer_text = tk.Label(exercise_content_frame, text="01:00", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
exercise_start_button = tk.Button(exercise_content_frame, text="Start Walk", relief="groove", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:exerciseCountdown(60, exercise_timer_text))
exercise_today.pack(pady=20)
exercise_timer_text.pack(pady=20)
exercise_start_button.pack(pady=20)


#Quiz screen
quiz_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
quiz_frame.pack(fill="y")
quiz_frame.place(x=0, y=0, anchor=tk.NW)

qstart_frame = tk.Frame(quiz_frame, bg="#E7F4F5")
qstart_frame.pack(padx=16)
qstart_frame.place(relx=0.5, rely=0, anchor=tk.N)

qstart_frame.grid_rowconfigure(0, weight=1)
qstart_frame.grid_rowconfigure(1, weight=1)
qstart_frame.grid_columnconfigure(0, weight=1)
qstart_frame.grid_columnconfigure(1, weight=1)

qstart_st_frame= tk.Frame(qstart_frame, bg="#E7F4F5")
qstart_st_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=20)
qstart_lt_frame= tk.Frame(qstart_frame, bg="#E7F4F5")
qstart_lt_frame.grid(row=1, column=0, sticky="nsew", pady=20)
qstart_rev_frame= tk.Frame(qstart_frame, bg="#E7F4F5")
qstart_rev_frame.grid(row=1, column=1, sticky="nsew", pady=20)

quiz_st_label = tk.Label(qstart_st_frame, text="How Do You \nFeel Right Now?", font=("Helvetica", 20, "bold"), bg="#E7F4F5")
quiz_st_button = tk.Button(qstart_st_frame, text="Rate Your Current Stress", font=("Helvetica", 18), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(stquiz_frame))
quiz_st_label.pack(pady=10)
quiz_st_button.pack()

quiz_lt_label = tk.Label(qstart_lt_frame, text="How Is Your Long-\nTerm Stress?", font=("Helvetica", 16, "bold"), bg="#E7F4F5")
quiz_lt_button = tk.Button(qstart_lt_frame, text="Take Long-Term\nStress Quiz", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(ltquiz_start))
quiz_lt_label.pack(pady=10, padx=10)
quiz_lt_button.pack(fill="x", padx=10)

quiz_rv_label = tk.Label(qstart_rev_frame, text="What Are Your\nStress Patterns?", font=("Helvetica", 16, "bold"), bg="#E7F4F5")
quiz_rv_button = tk.Button(qstart_rev_frame, text="Review Your Stress", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(review_frame))
quiz_rv_label.pack(pady=10, padx=10)
quiz_rv_button.pack(fill="x", padx=10)


#Short-Term quiz screen
stquiz_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
stquiz_frame.pack(fill="y")
stquiz_frame.place(x=0, y=0, anchor=tk.NW)

stquiz_rating_frame = tk.Frame(stquiz_frame, bg="#E7F4F5")
stquiz_rating_frame.pack()
stquiz_rating_frame.place(relx=0.5, rely=0, anchor=tk.N)

    #Short-term quiz images
stquiz_face1_path = "resources\\face1.png"
stquiz_face2_path = "resources\\face2.png"
stquiz_face3_path = "resources\\face3.png"
stquiz_face1_orig = Image.open(stquiz_face1_path)
stquiz_face2_orig = Image.open(stquiz_face2_path)
stquiz_face3_orig = Image.open(stquiz_face3_path)
stquiz_face1_resize = stquiz_face1_orig.resize((75, 75))
stquiz_face2_resize = stquiz_face2_orig.resize((75, 75))
stquiz_face3_resize = stquiz_face3_orig.resize((75, 75))
stquiz_face1 = ImageTk.PhotoImage(stquiz_face1_resize)
stquiz_face2 = ImageTk.PhotoImage(stquiz_face2_resize)
stquiz_face3 = ImageTk.PhotoImage(stquiz_face3_resize)

stquiz_rating_frame.grid_rowconfigure(0, weight=1)
stquiz_rating_frame.grid_rowconfigure(1, weight=1)
stquiz_rating_frame.grid_rowconfigure(2, weight=1)
stquiz_rating_frame.grid_rowconfigure(3, weight=1)
stquiz_rating_frame.grid_columnconfigure(0, weight=1)
stquiz_rating_frame.grid_columnconfigure(1, weight=1)
stquiz_rating_frame.grid_columnconfigure(2, weight=1)

def setMood(new_mood, mood_label):
    if new_mood == "low":
        user.mood = "low_stress"
        mood_label["text"] = "Low Stress"
    elif new_mood == "med":
        user.mood = "med_stress"
        mood_label["text"] = "Medium Stress"
    elif new_mood == "high":
        user.mood = "high_stress"
        mood_label["text"] = "High Stress"
    else:
        user.mood = "unknown"
        mood_label["text"] = ""

stquiz_label= tk.Label(stquiz_rating_frame, text="Rate Your Current Stress:", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
stquiz_face1_button = tk.Button(stquiz_rating_frame, image = stquiz_face1, compound = tk.CENTER, width = 75, height = 75, relief="flat", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:setMood("low", stquiz_curstress))
stquiz_face2_button = tk.Button(stquiz_rating_frame, image = stquiz_face2, compound = tk.CENTER, width = 75, height = 75, relief="flat", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:setMood("med", stquiz_curstress))
stquiz_face3_button = tk.Button(stquiz_rating_frame, image = stquiz_face3, compound = tk.CENTER, width = 75, height = 75, relief="flat", font=("Helvetica", 22, "bold"), bg="#E7F4F5", fg="#1A1E2E", command = lambda:setMood("high", stquiz_curstress))
stquiz_curstress= tk.Label(stquiz_rating_frame, text=" ", font=("Helvetica", 16, "bold"), bg="#E7F4F5")
stquiz_return_button = tk.Button(stquiz_rating_frame, text="Return", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(quiz_frame))

stquiz_label.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=20)
stquiz_face1_button.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
stquiz_face2_button.grid(row=1, column=1, sticky="nsew", pady=20, padx=20)
stquiz_face3_button.grid(row=1, column=2, sticky="nsew", pady=20, padx=20)
stquiz_curstress.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=20)
stquiz_return_button.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=20)




#Long-Term quiz start screen
ltquiz_start = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
ltquiz_start.pack(fill="y")
ltquiz_start.place(x=0, y=0, anchor=tk.NW)

ltquiz_start_frame = tk.Frame(ltquiz_start, bg="#E7F4F5")
ltquiz_start_frame.pack()
ltquiz_start_frame.place(relx=0.5, rely=0, anchor=tk.N)

ltquiz_start_button = tk.Button(ltquiz_start_frame, text="Start Long-Term\nStress Quiz", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, 0))
ltquiz_return_button = tk.Button(ltquiz_start_frame, text="Return", font=("Helvetica", 22, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(quiz_frame))
ltquiz_start_button.pack(fill="x", pady=20)
ltquiz_return_button.pack(fill="x", pady=20)


#Long-Term quiz screen
ltquiz_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
ltquiz_frame.pack(fill="y")
ltquiz_frame.place(x=0, y=0, anchor=tk.NW)

ltquiz_start_frame = tk.Frame(ltquiz_frame, bg="red")
ltquiz_start_frame.pack()
ltquiz_start_frame.place(relx=0.5, rely=0, anchor=tk.N)

ltquiz_question_frame = tk.Frame(ltquiz_frame, bg="#E7F4F5")
ltquiz_question_frame.pack()
ltquiz_question_frame.place(relx=0.5, rely=0, anchor=tk.N)

ltquiz_label1 = tk.Label(ltquiz_question_frame, text="Rate how often the statement\nbelow applies to you on a\nweekly basis", font=("Helvetica", 14, "bold"), bg="#E7F4F5")
ltquiz_question = tk.Label(ltquiz_question_frame, text="I feel like I have way\ntoo many things to do.", font=("Helvetica", 14, "bold"), bg="#E7F4F5")
ltquiz_answer_frame = tk.Frame(ltquiz_question_frame, bg="#E7F4F5")
ltquiz_label1.pack(pady=20)
ltquiz_question.pack()
ltquiz_answer_frame.pack(pady=20)

ltquiz_answer_frame.grid_columnconfigure(0, weight=1)
ltquiz_answer_frame.grid_columnconfigure(1, weight=1)
ltquiz_answer_frame.grid_columnconfigure(2, weight=1)
ltquiz_answer_frame.grid_columnconfigure(3, weight=1)
ltquiz_answer_frame.grid_columnconfigure(4, weight=1)
ltquiz_answer_frame.grid_columnconfigure(5, weight=1)
ltquiz_answer_frame.grid_rowconfigure(0, weight=1)

ltq_iter = 0
ltq_score = 0

def runLTQuiz(question_label, weight):
    ltquiz_frame.tkraise()
    global ltq_iter
    if ltq_iter == 0:
        countLTQuiz(weight)
        ltq_iter += 1
    elif ltq_iter == 1:
        question_label["text"] = "I have noticed that I am\nsleeping less or more often\nthan I used to."
        ltq_iter += 1
        countLTQuiz(weight)
    elif ltq_iter == 2:
        question_label["text"] = "I feel physically tired most\nof the time, even when I\nhaven't exerted myself."
        ltq_iter += 1
        countLTQuiz(weight)
    elif ltq_iter == 3:
        question_label["text"] = "I'm too busy to spend\ntime with friends and family."
        ltq_iter += 1
        countLTQuiz(weight)
    elif ltq_iter == 4:
        ltq_iter = 0
        countLTQuiz(weight)
        endLTQuiz(ltquiz_score)
        swapFrame(ltquiz_end)
        question_label["text"] = "I feel like I have way\ntoo many things to do."
    

def countLTQuiz(weight):
    global ltq_score
    ltq_score += weight
    print(ltq_score)
    

ltquiz_answer1_button = tk.Button(ltquiz_answer_frame, text="Almost\nNever", width = 7, height = 2, relief="groove", font=("Helvetica", 10, "bold"), bg="#E7F4F5", fg="#1A1E2E", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, -2))
ltquiz_answer2_button = tk.Button(ltquiz_answer_frame, text="Rarely", width = 7, height = 2, relief="groove", font=("Helvetica", 10, "bold"), bg="#E7F4F5", fg="#1A1E2E", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, -1))
ltquiz_answer3_button = tk.Button(ltquiz_answer_frame, text="Some-\ntimes", width = 7, height = 2, relief="groove", font=("Helvetica", 10, "bold"), bg="#E7F4F5", fg="#1A1E2E", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, 0))
ltquiz_answer4_button = tk.Button(ltquiz_answer_frame, text="Often", width = 7, height = 2, relief="groove", font=("Helvetica", 10, "bold"), bg="#E7F4F5", fg="#1A1E2E", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, 1))
ltquiz_answer5_button = tk.Button(ltquiz_answer_frame, text="Very\nOften", width = 7, height = 2, relief="groove", font=("Helvetica", 10, "bold"), bg="#E7F4F5", fg="#1A1E2E", activebackground="#234265", activeforeground="white", command = lambda:runLTQuiz(ltquiz_question, 2))

ltquiz_answer1_button.grid(row=0, column=0, sticky="nsew", pady=20, padx=5)
ltquiz_answer2_button.grid(row=0, column=1, sticky="nsew", pady=20, padx=5)
ltquiz_answer3_button.grid(row=0, column=2, sticky="nsew", pady=20, padx=5)
ltquiz_answer4_button.grid(row=0, column=3, sticky="nsew", pady=20, padx=5)
ltquiz_answer5_button.grid(row=0, column=4, sticky="nsew", pady=20, padx=5)




#Long-Term quiz end screen
ltquiz_end = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
ltquiz_end.pack(fill="y")
ltquiz_end.place(x=0, y=0, anchor=tk.NW)

ltquiz_end_frame = tk.Frame(ltquiz_end, bg="#E7F4F5")
ltquiz_end_frame.pack()
ltquiz_end_frame.place(relx=0.5, rely=0, anchor=tk.N)

def endLTQuiz(score_label):
    global ltq_score
    if ltq_score < 3:
        score_label["text"] = str(ltq_score) + "\n(low)"
    if -2 < ltq_score < 2:
        score_label["text"] = str(ltq_score) + "\n(medium)"
    if ltq_score > 3:
        score_label["text"] = str(ltq_score) + " \n(high)"
    ltq_score = 0


ltquiz_label = tk.Label(ltquiz_end_frame, text="Your Stress Score:", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
ltquiz_score = tk.Label(ltquiz_end_frame, text="Your Score", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
ltquiz_label.pack(pady=20)
ltquiz_score.pack()

ltquiz_retake_button = tk.Button(ltquiz_end_frame, text="Retake Quiz", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(ltquiz_start))
ltquiz_retake_button.pack(pady=20)



#Stress review screen
review_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
review_frame.pack(fill="y")
review_frame.place(x=0, y=0, anchor=tk.NW)

review_ex_frame = tk.Frame(review_frame, bg="#E7F4F5")
review_ex_frame.pack()
review_ex_frame.place(relx=0.5, rely=0, anchor=tk.N)

review_img_path = "resources\\review_chart.png"
review_img_orig = Image.open(review_img_path)
review_img_resize = review_img_orig.resize((350, 208))
review_img = ImageTk.PhotoImage(review_img_resize)

review_ex_label = tk.Label(review_ex_frame, text="Review Long-Term Stress", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
review_ex_img = tk.Label(review_ex_frame, image = review_img, compound=tk.CENTER, bg="#E7F4F5")
review_ex_label.pack(pady=20)
review_ex_img.pack()


review_sync_button = tk.Button(review_ex_frame, text="Sync New Device", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(error_frame))
review_ins_button = tk.Button(review_ex_frame, text="Review Insights", font=("Helvetica", 16), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(error_frame))
review_sync_button.pack(side="left", fill="x", padx=10, pady=20)
review_ins_button.pack(side="left", fill="x", padx=10, pady=20)


#Error screen
error_frame = tk.Frame(body_frame, width = 450, height = 400, bg="#E7F4F5")
error_frame.pack(fill="y")
error_frame.place(x=0, y=0, anchor=tk.NW)

error_button_frame = tk.Frame(error_frame, bg="#E7F4F5")
error_button_frame.pack()
error_button_frame.place(relx=0.5, rely=0, anchor=tk.N)

error_label = tk.Label(error_button_frame, text="Coming Soon!", font=("Helvetica", 22, "bold"), bg="#E7F4F5")
error_button = tk.Button(error_button_frame, text="Return to Home", font=("Helvetica", 16, "bold"), bg="#205B95", fg="white", activebackground="#234265", activeforeground="white", command = lambda:swapFrame(home_frame))
error_label.pack(pady=20)
error_button.pack()



#run
if __name__ == "__main__":
    home_frame.tkraise()
    user = User("unknown", "unknown")
    window.mainloop()
    
