import tkinter as tk
from PIL import Image, ImageTk

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__power = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def initialize(self):
        self.__power = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def toggle_power(self):
        self.__power = not self.__power

    def toggle_mute(self):
        if self.__power:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__power:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__power:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__power and not self.__muted:
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        if self.__power and not self.__muted:
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def get_channel_image(self):
        if self.__power:
            try:
                image_path = f"{self.__channel}.png"
                original_image = Image.open(image_path)
                resized_image = original_image.resize((150, 150), Image.ANTIALIAS if hasattr(Image, "ANTIALIAS") else 3)
                return resized_image
            except FileNotFoundError:
                print(f"Image file not found: {image_path}")
                return Image.new("RGB", (150, 150), "gray")
        else:
            return Image.new("RGB", (150, 150), "black")

    def is_power_on(self):
        return self.__power

    def is_muted(self):
        return self.__muted

    def __str__(self):
        mute_status = "Muted" if self.__muted else "Unmuted"
        return f"Power = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}, {mute_status}"

class TelevisionRemote:
    def __init__(self, master):
        self.master = master
        self.master.title("TV Remote")
        self.tv = Television()

        self.image_box = tk.Label(self.master)
        self.image_box.grid(row=0, column=0, rowspan=4, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.volume_notch_canvas = tk.Canvas(self.master, width=150, height=10, bg="white")
        self.volume_notch_canvas.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

        self.volume_label = tk.Label(self.master, text="Volume: 0")
        self.volume_label.grid(row=5, column=0, columnspan=4, pady=10, sticky="nsew")

        self.mute_label = tk.Label(self.master, text="Mute: Unmuted")
        self.mute_label.grid(row=6, column=0, columnspan=4, pady=10, sticky="nsew")

        self.channel_label = tk.Label(self.master, text="Channel: 0")
        self.channel_label.grid(row=7, column=0, columnspan=4, pady=10, sticky="nsew")

        self.power_button = tk.Button(self.master, text="Power", command=self.toggle_power)
        self.power_button.grid(row=8, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.mute_button = tk.Button(self.master, text="Mute", command=self.toggle_mute, state=tk.DISABLED)
        self.mute_button.grid(row=8, column=2, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.volume_up_button = tk.Button(self.master, text="Vol Up", command=self.volume_up, state=tk.DISABLED)
        self.volume_up_button.grid(row=9, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.volume_down_button = tk.Button(self.master, text="Vol Down", command=self.volume_down, state=tk.DISABLED)
        self.volume_down_button.grid(row=9, column=2, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.channel_up_button = tk.Button(self.master, text="Ch Up", command=self.channel_up, state=tk.DISABLED)
        self.channel_up_button.grid(row=10, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.channel_down_button = tk.Button(self.master, text="Ch Down", command=self.channel_down, state=tk.DISABLED)
        self.channel_down_button.grid(row=10, column=2, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.create_number_pad()

        for i in range(12):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        self.update_channel_image()
        self.update_labels()

    def create_number_pad(self):
        for i in range(4):
            digit_button = tk.Button(self.master, text=str(i), command=lambda num=i: self.select_channel(num))
            digit_button.grid(row=11, column=i, pady=10, padx=5, sticky="nsew")

    def select_channel(self, channel):
        if self.tv.is_power_on():
            self.tv._Television__channel = channel
            self.update_channel_image()
            self.update_labels()

    def toggle_power(self):
        self.tv.toggle_power()
        state = tk.NORMAL if self.tv.is_power_on() else tk.DISABLED
        self.set_button_state(state)
        self.update_channel_image()
        self.update_labels()

    def toggle_mute(self):
        self.tv.toggle_mute()
        volume_state = tk.DISABLED if self.tv.is_muted() else tk.NORMAL
        self.volume_up_button.config(state=volume_state)
        self.volume_down_button.config(state=volume_state)
        self.update_labels()

    def channel_up(self):
        self.tv.channel_up()
        self.update_channel_image()
        self.update_labels()

    def channel_down(self):
        self.tv.channel_down()
        self.update_channel_image()
        self.update_labels()

    def volume_up(self):
        self.tv.volume_up()
        self.update_labels()

    def volume_down(self):
        self.tv.volume_down()
        self.update_labels()

    def update_channel_image(self):
        channel_image = self.tv.get_channel_image()
        photo = ImageTk.PhotoImage(channel_image)
        self.image_box.configure(image=photo)
        self.image_box.image = photo

    def update_labels(self):
        self.volume_label.config(text=f"Volume: {self.tv._Television__volume}")
        mute_status = "Muted" if self.tv._Television__muted else "Unmuted"
        self.mute_label.config(text=f"Mute: {mute_status}")
        self.channel_label.config(text=f"Channel: {self.tv._Television__channel}")

        self.update_volume_notch()

    def update_volume_notch(self):
        if self.tv.is_power_on():
            volume_width = (self.tv._Television__volume / self.tv.MAX_VOLUME) * 150
            self.volume_notch_canvas.delete("all")
            self.volume_notch_canvas.create_rectangle(0, 0, volume_width, 10, fill="green")

    def set_button_state(self, state):
        self.volume_up_button.config(state=state)
        self.volume_down_button.config(state=state)
        self.channel_up_button.config(state=state)
        self.channel_down_button.config(state=state)
        self.mute_button.config(state=state)

if __name__ == '__main__':
    root = tk.Tk()
    app = TelevisionRemote(root)
    root.mainloop()
