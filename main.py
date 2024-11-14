import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Connect to SQLite database (creates database if it doesn't exist)
conn = sqlite3.connect('bikes.db')
cursor = conn.cursor()

# Create bikes table
cursor.execute('''CREATE TABLE IF NOT EXISTS bikes (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    category TEXT,
                    engine_capacity TEXT,
                    fuel_type TEXT,
                    mileage TEXT,
                    power TEXT,
                    torque TEXT,
                    top_speed TEXT,
                    price REAL,
                    image_path TEXT)''')
conn.commit()

# Uncomment and run this block once to add sample bike data
 sample_bikes = [
     ("Bajaj Pulsar 125", "Commuter", "125cc", "Petrol", "57 km/l", "11.8 hp", "10.8 Nm", "105 km/h", 750, "images/pulsar125.jpg"),
    ("Bajaj Pulsar NS125", "Commuter", "125cc", "Petrol", "50 km/l", "12 hp", "11 Nm", "110 km/h", 800, "images/pulsarns125.jpg"),
    ("Bajaj Platina 100", "Commuter", "100cc", "Petrol", "75 km/l", "7.9 hp", "8.3 Nm", "90 km/h", 600, "images/platina100.jpg"),
    ("Bajaj Platina 110", "Commuter", "110cc", "Petrol", "70 km/l", "8.6 hp", "9.81 Nm", "95 km/h", 650, "images/platina110.jpg"),
    ("Bajaj CT 110", "Commuter", "110cc", "Petrol", "70 km/l", "8.6 hp", "9.81 Nm", "90 km/h", 620, "images/ct110.jpg"),
    ("Bajaj CT 100", "Commuter", "100cc", "Petrol", "75 km/l", "7.9 hp", "8.3 Nm", "90 km/h", 600, "images/ct100.jpg"),
    ("Bajaj Avenger Street 160", "Cruiser", "160cc", "Petrol", "47 km/l", "15 hp", "13.7 Nm", "105 km/h", 950, "images/avengerstreet160.jpg"),
    ("Bajaj Avenger Cruise 220", "Cruiser", "220cc", "Petrol", "40 km/l", "19 hp", "17.5 Nm", "115 km/h", 1200, "images/avengercruise220.jpg"),
    ("Bajaj Dominar 250", "Sports", "250cc", "Petrol", "35 km/l", "27 hp", "23.5 Nm", "132 km/h", 1500, "images/dominar250.jpg"),
    ("Bajaj Dominar 400", "Sports", "400cc", "Petrol", "27 km/l", "40 hp", "35 Nm", "148 km/h", 2000, "images/dominar400.jpg"),
    ("Bajaj Pulsar RS200", "Sports", "200cc", "Petrol", "35 km/l", "24.5 hp", "18.7 Nm", "140 km/h", 1300, "images/pulsarrs200.jpg"),
    ("Bajaj Pulsar NS200", "Naked", "200cc", "Petrol", "36 km/l", "24 hp", "18.5 Nm", "136 km/h", 1200, "images/pulsarns200.jpg"),
    ("Bajaj Pulsar 150", "Commuter", "150cc", "Petrol", "50 km/l", "14 hp", "13.25 Nm", "110 km/h", 850, "images/pulsar150.jpg"),
    ("Bajaj Pulsar NS160", "Naked", "160cc", "Petrol", "42 km/l", "17 hp", "14.6 Nm", "120 km/h", 900, "images/pulsarns160.jpg"),
    ("Bajaj Pulsar 180F", "Commuter", "180cc", "Petrol", "45 km/l", "17 hp", "14.22 Nm", "122 km/h", 950, "images/pulsar180f.jpg"),
    ("Bajaj Pulsar 220F", "Sports", "220cc", "Petrol", "40 km/l", "20.4 hp", "18.55 Nm", "134 km/h", 1150, "images/pulsar220f.jpg"),
    ("Bajaj Pulsar NS250", "Naked", "250cc", "Petrol", "35 km/l", "24 hp", "20 Nm", "135 km/h", 1400, "images/pulsarns250.jpg"),
    ("Bajaj Discover 125", "Commuter", "125cc", "Petrol", "65 km/l", "11 hp", "11 Nm", "100 km/h", 650, "images/discover125.jpg"),
    ("Bajaj Discover 110", "Commuter", "110cc", "Petrol", "70 km/l", "8.5 hp", "9 Nm", "90 km/h", 620, "images/discover110.jpg"),
    ("Bajaj V15", "Commuter", "150cc", "Petrol", "50 km/l", "13 hp", "13 Nm", "110 km/h", 750, "images/v15.jpg"),
    ("Bajaj V12", "Commuter", "125cc", "Petrol", "55 km/l", "10.7 hp", "10.9 Nm", "105 km/h", 700, "images/v12.jpg"),
    ("Bajaj Dominar 250 ABS", "Sports", "250cc", "Petrol", "35 km/l", "27 hp", "23.5 Nm", "132 km/h", 1600, "images/dominar250abs.jpg"),
    ("Bajaj Avenger 160 Street ABS", "Cruiser", "160cc", "Petrol", "47 km/l", "15 hp", "13.7 Nm", "105 km/h", 980, "images/avenger160street.jpg"),
    ("Bajaj Dominar 400 ABS", "Sports", "400cc", "Petrol", "27 km/l", "40 hp", "35 Nm", "148 km/h", 2100, "images/dominar400abs.jpg"),
    ("Bajaj CT125", "Commuter", "125cc", "Petrol", "60 km/l", "10 hp", "10 Nm", "100 km/h", 650, "images/ct125.jpg"),
    ("Bajaj Pulsar 135", "Commuter", "135cc", "Petrol", "55 km/l", "13.5 hp", "11.4 Nm", "112 km/h", 750, "images/pulsar135.jpg")
]
 cursor.executemany("INSERT INTO bikes (name, category, engine_capacity, fuel_type, mileage, power, torque, top_speed, price, image_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_bikes)
 conn.commit()

# Function to show bike details in a new window
def show_bike_details(bike):
    details_window = Toplevel(root)
    details_window.title(bike[1])
    
    Label(details_window, text=f"Name: {bike[1]}", font=("Arial", 16)).pack()
    Label(details_window, text=f"Category: {bike[2]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Engine Capacity: {bike[3]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Fuel Type: {bike[4]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Mileage: {bike[5]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Power: {bike[6]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Torque: {bike[7]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Top Speed: {bike[8]}", font=("Arial", 12)).pack()
    Label(details_window, text=f"Price: ${bike[9]}", font=("Arial", 12)).pack()
    
    # Display the bike image
    img_path = bike[10]
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((250, 150), Image.ANTIALIAS)
        bike_img = ImageTk.PhotoImage(img)
        img_label = Label(details_window, image=bike_img)
        img_label.image = bike_img  # keep a reference to avoid garbage collection
        img_label.pack()
    else:
        Label(details_window, text="Image not found", font=("Arial", 12)).pack()

# Function to load bike cards based on search query
def load_bike_cards(search_query=""):
    for widget in bike_frame.winfo_children():
        widget.destroy()
    
    if search_query:
        cursor.execute("SELECT * FROM bikes WHERE name LIKE ?", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT * FROM bikes")
    bikes = cursor.fetchall()
    
    for bike in bikes:
        # Create a frame for each bike card
        bike_card = Frame(bike_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        bike_card.pack(pady=10, fill=X)
        
        # Display the bike image
        img_path = bike[10]
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((100, 60), Image.ANTIALIAS)
            bike_img = ImageTk.PhotoImage(img)
            img_label = Label(bike_card, image=bike_img)
            img_label.image = bike_img  # keep a reference to avoid garbage collection
            img_label.grid(row=0, column=0, rowspan=3, padx=10)
        
        # Display bike name and price
        Label(bike_card, text=bike[1], font=("Arial", 16, "bold")).grid(row=0, column=1, sticky=W)
        Label(bike_card, text=f"${bike[9]}", font=("Arial", 14)).grid(row=1, column=1, sticky=W)
        
        # View details button
        view_btn = Button(bike_card, text="View Details", command=lambda b=bike: show_bike_details(b))
        view_btn.grid(row=2, column=1, sticky=W)

# Main Tkinter window setup
root = Tk()
root.title("Bike Information App")

# Search bar
search_var = StringVar()
search_entry = Entry(root, textvariable=search_var, font=("Arial", 14), width=30)
search_entry.pack(pady=10)

# Search button
search_button = Button(root, text="Search", command=lambda: load_bike_cards(search_var.get()))
search_button.pack(pady=5)

# Frame to display bike cards
bike_frame = Frame(root)
bike_frame.pack(fill=BOTH, expand=True)

# Load bike cards on the main screen
load_bike_cards()

root.mainloop()

# Close database connection
conn.close()
