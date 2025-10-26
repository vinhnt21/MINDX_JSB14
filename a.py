import turtle
import math

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Phương Thúy Cute ❤️")
screen.setup(width=1000, height=700)

# Tạo turtle
pen = turtle.Turtle()
pen.speed(0)  # Tốc độ nhanh nhất
pen.pensize(3)
screen.tracer(0)  # Tắt animation để vẽ nhanh hơn

def move_to(x, y):
    """Di chuyển đến vị trí mà không vẽ"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def draw_heart(x, y, size=1):
    """Vẽ hình trái tim"""
    move_to(x, y)
    pen.color("red")
    pen.begin_fill()
    
    # Vẽ trái tim bằng các đường cong
    pen.left(45)
    pen.forward(size * 20)
    pen.circle(size * 10, 180)
    pen.right(90)
    pen.circle(size * 10, 180)
    pen.forward(size * 20)
    
    pen.end_fill()
    pen.setheading(0)

def draw_star(x, y, size=10):
    """Vẽ ngôi sao nhỏ"""
    move_to(x, y)
    pen.color("yellow")
    pen.begin_fill()
    
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        pen.forward(size)
        pen.left(72)
    
    pen.end_fill()

def write_cute_text(text, x, y, color="pink", font_size=40):
    """Viết text với font cute"""
    move_to(x, y)
    pen.color(color)
    pen.write(text, align="center", font=("Comic Sans MS", font_size, "bold"))

def draw_decorative_border():
    """Vẽ viền trang trí"""
    pen.color("purple")
    pen.pensize(5)
    
    # Vẽ khung chữ nhật bo tròn
    move_to(-400, 250)
    pen.setheading(0)
    
    for _ in range(2):
        pen.forward(600)
        pen.circle(-20, 90)
        pen.forward(300)
        pen.circle(-20, 90)

def draw_cute_decorations():
    """Vẽ các trang trí cute - giảm số lượng để nhanh hơn"""
    # Vẽ ít trái tim hơn
    heart_positions = [
        (-350, 200), (350, 200),
        (-320, 120), (320, 120),
        (-310, 20), (310, 20),
        (-300, -80), (300, -80)
    ]
    
    for x, y in heart_positions:
        draw_heart(x, y, 0.7)
    
    # Vẽ ít ngôi sao hơn
    star_positions = [
        (-370, 150), (370, 150),
        (-340, 70), (340, 70),
        (-330, -30), (330, -30)
    ]
    
    for x, y in star_positions:
        draw_star(x, y, 8)

def draw_main_hearts():
    """Vẽ những trái tim chính lớn hơn"""
    # Trái tim lớn ở giữa trên
    draw_heart(0, 180, 1.5)
    
    # Hai trái tim ở hai bên
    draw_heart(-200, 50, 1.2)
    draw_heart(200, 50, 1.2)
    
    # Trái tim ở dưới
    draw_heart(0, -150, 1.3)

def add_sparkles():
    """Thêm hiệu ứng lấp lánh - giảm bớt để nhanh hơn"""
    sparkle_positions = [
        (-250, 180), (250, 180),
        (-180, 100), (180, 100),
        (-160, 0), (160, 0),
        (-150, -100), (150, -100)
    ]
    
    pen.color("white")
    pen.pensize(2)
    
    for x, y in sparkle_positions:
        move_to(x, y)
        # Vẽ dấu + nhỏ làm hiệu ứng lấp lánh
        pen.forward(8)
        pen.backward(4)
        pen.left(90)
        pen.forward(4)
        pen.backward(8)
        pen.forward(4)
        pen.right(90)

# Vẽ viền trang trí
draw_decorative_border()

# Vẽ các trang trí cute
draw_cute_decorations()

# Vẽ những trái tim chính
draw_main_hearts()

# Thêm hiệu ứng lấp lánh
add_sparkles()

# Viết chữ "Phương Thúy" 
pen.pensize(3)
write_cute_text("Phương", 0, 80, "hotpink", 35)
write_cute_text("Thúy", 0, 35, "deeppink", 35)

# Thêm text cute bên dưới
write_cute_text("💖 Cute & Sweet 💖", 0, -50, "lightpink", 20)

# Vẽ một vài trái tim nhỏ xung quanh tên
small_hearts = [(-80, 90), (80, 90), (-70, 25), (70, 25)]
for x, y in small_hearts:
    draw_heart(x, y, 0.5)

# Thêm message cuối
pen.color("cyan")
move_to(0, -200)
pen.write("Made with ❤️ by Python Turtle", align="center", 
          font=("Arial", 12, "italic"))

# Giữ màn hình mở
pen.hideturtle()
screen.update()  # Hiển thị tất cả một lần
screen.exitonclick()

print("🎨 Hoàn thành! Click vào màn hình để thoát.")
print("💕 Chúc Phương Thúy luôn xinh đẹp và hạnh phúc! 💕")