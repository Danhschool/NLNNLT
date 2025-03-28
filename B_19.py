import math

def sin_taylor(x, n_terms=10):
    """
    Xấp xỉ sin(x) bằng khai triển Taylor
    x: Giá trị góc (radian)
    n_terms: Số lượng số hạng trong chuỗi Taylor
    """
    sin_approx = 0
    for k in range(n_terms):
        term = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sin_approx += term
    return sin_approx

# Nhập góc từ người dùng (theo độ)
x_degree = float(input("Nhập góc x (theo độ): "))

# Chuyển đổi từ độ sang radian
x_radian = math.radians(x_degree)

# Nhập số lượng số hạng Taylor cần lấy
n_terms = int(input("Nhập số lượng số hạng Taylor muốn lấy: "))

# Tính sin(x) xấp xỉ bằng chuỗi Taylor
sin_x_approx = sin_taylor(x_radian, n_terms)
real_sin_x = math.sin(x_radian)

# In kết quả
print(f"Giá trị gần đúng của sin({x_degree} độ) là: {sin_x_approx}")
print(f"Giá trị thực tế của sin({x_degree} độ) là: {real_sin_x}")
print(f"Sai số là: {abs(real_sin_x - sin_x_approx)}")
