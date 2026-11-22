tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

if __name__ == "__main__":
    print("=== ỨNG DỤNG QUẢN LÝ CÔNG VIỆC ===")
    add_task("Học bài Git và GitHub")
