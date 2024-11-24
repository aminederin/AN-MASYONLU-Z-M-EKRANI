import tkinter as tk
import random


class Ball:
    def __init__(self, canvas, x, y, size, color, dx, dy):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.dx = dx
        self.dy = dy
        self.ball_id = canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)

    def move(self):
        self.canvas.move(self.ball_id, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball_id)

        # Duvarlardan sekme
        if x1 <= 0 or x2 >= self.canvas.winfo_width():
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas.winfo_height():
            self.dy = -self.dy


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Çizim Ekranı")

        # Canvas oluşturma
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Varsayılan renk ve boyut
        self.selected_color = "red"
        self.selected_size = 20

        # Renk butonları
        self.color_frame = tk.Frame(root)
        self.color_frame.pack(side=tk.TOP, pady=10)

        tk.Label(self.color_frame, text="Renk Seç:").pack(side=tk.LEFT, padx=5)
        self.red_button = tk.Button(self.color_frame, bg="red", width=5, height=2,
                                    command=lambda: self.select_color("red"))
        self.red_button.pack(side=tk.LEFT, padx=5)
        self.blue_button = tk.Button(self.color_frame, bg="blue", width=5, height=2,
                                     command=lambda: self.select_color("blue"))
        self.blue_button.pack(side=tk.LEFT, padx=5)
        self.green_button = tk.Button(self.color_frame, bg="green", width=5, height=2,
                                      command=lambda: self.select_color("green"))
        self.green_button.pack(side=tk.LEFT, padx=5)

        # Boyut butonları
        self.size_frame = tk.Frame(root)
        self.size_frame.pack(side=tk.TOP, pady=10)

        tk.Label(self.size_frame, text="Boyut Seç:").pack(side=tk.LEFT, padx=5)

        self.small_button = tk.Canvas(self.size_frame, width=40, height=40, bg="white", highlightthickness=0)
        self.small_button.create_oval(10, 10, 30, 30, fill="black")
        self.small_button.bind("<Button-1>", lambda e: self.select_size(20))
        self.small_button.pack(side=tk.LEFT, padx=5)

        self.medium_button = tk.Canvas(self.size_frame, width=50, height=50, bg="white", highlightthickness=0)
        self.medium_button.create_oval(10, 10, 40, 40, fill="black")
        self.medium_button.bind("<Button-1>", lambda e: self.select_size(30))
        self.medium_button.pack(side=tk.LEFT, padx=5)

        self.large_button = tk.Canvas(self.size_frame, width=60, height=60, bg="white", highlightthickness=0)
        self.large_button.create_oval(10, 10, 50, 50, fill="black")
        self.large_button.bind("<Button-1>", lambda e: self.select_size(40))
        self.large_button.pack(side=tk.LEFT, padx=5)

        # Kontrol butonları
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(side=tk.TOP, pady=10)

        self.start_button = tk.Button(self.control_frame, text="Start", command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_canvas)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.speed_up_button = tk.Button(self.control_frame, text="Speed Up", command=self.speed_up)
        self.speed_up_button.pack(side=tk.LEFT, padx=10)

        # Topların özellikleri
        self.balls = []
        self.is_running = False
        self.speed_multiplier = 1.0

        self.canvas.bind("<Button-1>", self.add_ball)

    def select_color(self, color):
        self.selected_color = color

    def select_size(self, size):
        self.selected_size = size

    def add_ball(self, event):
        dx = random.choice([-3, -2, 2, 3])
        dy = random.choice([-3, -2, 2, 3])
        ball = Ball(self.canvas, event.x, event.y, self.selected_size, self.selected_color, dx, dy)
        self.balls.append(ball)

    def start_animation(self):
        if not self.is_running:
            self.is_running = True
            self.animate()

    def stop_animation(self):
        self.is_running = False

    def reset_canvas(self):
        self.stop_animation()
        for ball in self.balls:
            self.canvas.delete(ball.ball_id)
        self.balls.clear()

    def speed_up(self):
        self.speed_multiplier *= 1.5

    def animate(self):
        if self.is_running:
            for ball in self.balls:
                ball.dx *= self.speed_multiplier
                ball.dy *= self.speed_multiplier
                ball.move()
            self.speed_multiplier = 1.0  # Speed up sonrası hızı resetle
            self.root.after(20, self.animate)


# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
