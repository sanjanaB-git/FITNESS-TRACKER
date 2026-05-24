from tkinter import *
from tkinter import messagebox
from datetime import date

# Main Window
root = Tk()
root.title("Fitness Tracker App")
root.geometry("500x650")
root.configure(bg="#dff6ff")

# Current Date
today = date.today()

# Heading
Label(
    root,
    text="Fitness Tracker App",
    font=("Arial", 22, "bold"),
    bg="#dff6ff",
    fg="#003566"
).pack(pady=10)

Label(
    root,
    text=f"Date: {today}",
    font=("Arial", 10),
    bg="#dff6ff"
).pack(pady=5)

# ---------------- BMI SECTION ----------------

bmi_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
bmi_frame.pack(pady=15, padx=20, fill="x")

Label(
    bmi_frame,
    text="BMI Calculator",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#0077b6"
).pack(pady=10)

Label(bmi_frame, text="Weight (kg)", bg="white").pack()
weight_entry = Entry(bmi_frame, width=25)
weight_entry.pack(pady=5)

Label(bmi_frame, text="Height (cm)", bg="white").pack()
height_entry = Entry(bmi_frame, width=25)
height_entry.pack(pady=5)

bmi_result = Label(
    bmi_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="green"
)
bmi_result.pack(pady=10)


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100

        bmi = weight / (height * height)

        # BMI Category
        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        bmi_result.config(
            text=f"Your BMI is {round(bmi,2)} ({status})"
        )

    except:
        messagebox.showerror("Error", "Please enter valid values")


Button(
    bmi_frame,
    text="Calculate BMI",
    bg="#0077b6",
    fg="white",
    width=20,
    command=calculate_bmi
).pack(pady=10)

# ---------------- WATER SECTION ----------------

water_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
water_frame.pack(pady=15, padx=20, fill="x")

Label(
    water_frame,
    text="Water Intake Tracker",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#0077b6"
).pack(pady=10)

Label(
    water_frame,
    text="Number of Glasses",
    bg="white"
).pack()

water_entry = Entry(water_frame, width=25)
water_entry.pack(pady=5)


def save_water():
    water = water_entry.get()

    if water == "":
        messagebox.showerror("Error", "Please enter water intake")
    else:
        messagebox.showinfo(
            "Saved",
            f"Water Intake Saved\n\n{water} glasses consumed today"
        )


Button(
    water_frame,
    text="Save Water Intake",
    bg="#00b4d8",
    fg="white",
    width=20,
    command=save_water
).pack(pady=10)

# ---------------- WORKOUT SECTION ----------------

workout_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
workout_frame.pack(pady=15, padx=20, fill="x")

Label(
    workout_frame,
    text="Workout Tracker",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#0077b6"
).pack(pady=10)

Label(workout_frame, text="Workout Name", bg="white").pack()
workout_entry = Entry(workout_frame, width=25)
workout_entry.pack(pady=5)

Label(
    workout_frame,
    text="Workout Duration (minutes)",
    bg="white"
).pack()

duration_entry = Entry(workout_frame, width=25)
duration_entry.pack(pady=5)


def save_workout():
    try:
        workout = workout_entry.get()
        duration = int(duration_entry.get())

        calories = duration * 5

        messagebox.showinfo(
            "Workout Saved",
            f"Workout: {workout}\n"
            f"Duration: {duration} mins\n"
            f"Calories Burned: {calories}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid workout details")


Button(
    workout_frame,
    text="Save Workout",
    bg="#38b000",
    fg="white",
    width=20,
    command=save_workout
).pack(pady=10)

# ---------------- FITNESS TIP ----------------

Label(
    root,
    text="Tip: Drink 8 glasses of water daily and exercise regularly!",
    font=("Arial", 11, "italic"),
    bg="#dff6ff",
    fg="#d00000"
).pack(pady=20)

# Run App
root.mainloop()