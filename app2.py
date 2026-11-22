# Danh sách lưu trữ các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc thành công: '{task_name}'")

# --- Điểm chạy chính của chương trình ---
if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH QUẢN LÝ CÔNG VIỆC (TO-DO LIST) ===")
    add_task("Học bài Git và GitHub")
    add_task("Thực hành tạo nhánh feature/list-tasks")