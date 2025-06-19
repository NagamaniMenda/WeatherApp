import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "8000322674346bc9bf08f2b7ee5de93a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Create root window
root = Tk()
root.title("Weather App with Dynamic Background")
root.geometry("500x500")
root.resizable(False, False)

# Canvas for background
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill="both", expand=True)

# Load default background image
bg_image = ImageTk.PhotoImage(Image.open("default.jpg").resize((500, 500)))
bg_item = canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Entry field
city_entry = Entry(root, font=("Arial", 14), justify="center")
city_entry_window = canvas.create_window(250, 30, window=city_entry, width=300)

# Labels
temp_label = Label(root, font=("Arial", 16), bg="white")
desc_label = Label(root, font=("Arial", 12), bg="white")
result_label = Label(root, text="", fg="red", bg="white")
icon_label = Label(root, bg="white")

canvas.create_window(250, 90, window=temp_label)
canvas.create_window(250, 130, window=desc_label)
canvas.create_window(250, 170, window=result_label)
canvas.create_window(250, 220, window=icon_label)

# Update theme based on weather
def update_background(condition):
    try:
        condition = condition.lower()
        if "clear" in condition:
            image = Image.open("clear.jpg")
        elif "cloud" in condition:
            image = Image.open("clouds.jpg")
        elif "rain" in condition:
            image = Image.open("rain.jpg")
        elif "snow" in condition:
            image = Image.open("snow.jpg")
        elif any(word in condition for word in ["storm", "thunder", "lightning","thunderstorm","scattered clouds","light rain"]):
            image = Image.open("storm.jpg")
        else:
            image = Image.open("default.jpg")

        resized = image.resize((500, 500))
        bg = ImageTk.PhotoImage(resized)
        canvas.itemconfig(bg_item, image=bg)
        canvas.image = bg  # Save reference

    except Exception as e:
        print("Error loading background image:", e)

# Get weather from API
def get_weather():
    city = city_entry.get().strip()
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)

        if str(data.get('cod')) != "200":
            result_label.config(text="City not found or error.")
            icon_label.config(image='')
           
            return

        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print("Weather description:", desc) 
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_img = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(icon_url).content)))

        temp_label.config(text=f"Temperature: {temp}°C")
        desc_label.config(text=f"Condition: {desc.title()}")
        icon_label.config(image=icon_img)
        icon_label.image = icon_img
        result_label.config(text="")

        # 🔁 Smart background decision: snow if very cold
        if "snow" in desc.lower() or temp <= 2:
          update_background("snow")
        else:
          update_background(desc)


    except Exception as e:
        result_label.config(text="Error fetching weather data.")
        print("Error:", e)

# Button
get_btn = Button(root, text="Get Weather", command=get_weather)
canvas.create_window(250, 65, window=get_btn)

root.mainloop()
