continue_pro = "y"
while continue_pro == "y":
    num_employees = int(input("Nhập số lượng nhân viên: "))
    print()  
    for i in range(num_employees):
        print(f"Nhân viên {i + 1}")
        name = input("Tên nhân viên: ")
        days_worked = int(input("Số ngày đi làm: "))
        print("Thông tin nhân viên:")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {days_worked}")
        if days_worked < 20:
            print("Cần cải thiện chuyên cần\n")
        else:
            print("Nhân viên chuyên cần tốt\n")
    choice = input("Tiếp tục chương trình? (y/n): ")
    continue_pro = choice.strip().lower()
print("Chương trình kết thúc")
