# Data Processing & Visualization Project

## 📌 Giới thiệu
Dự án này thực hiện **xử lý và trực quan hóa dữ liệu điểm thi THPT Quốc gia 2020** từ dữ liệu HTML thô được crawl từ website.

File chính **`process_all.py`** sẽ:
- Đọc toàn bộ dữ liệu HTML của tất cả thí sinh.
- Loại bỏ các Số Báo Danh (SBD) không hợp lệ (danh sách trong `exception.txt`).
- Chuyển đổi các ký tự Unicode lỗi sang tiếng Việt chuẩn (dựa vào `unicode.txt`).
- Xuất dữ liệu sạch ra file **`clean_data.csv`**.

---

## 📂 Cấu trúc thư mục & file

---

## 📊 Biểu đồ trực quan hóa
1. **plot1_SoHS_bo_thi.py** → Biểu đồ cột thể hiện số lượng học sinh bỏ thi của từng môn.
2. **plot2_So_mon_hs_thi.py** → Biểu đồ tròn thể hiện tỷ lệ số môn học sinh đăng ký thi (ví dụ: thi 5 môn chiếm 30%).
3. **plot3_DiemTB_theo_mon.py** → Biểu đồ cột thể hiện điểm trung bình của học sinh theo từng môn.
4. **plot4_DiemTB_theo_tuoi.py** → Biểu đồ cột kết hợp đường thể hiện điểm trung bình từng môn học theo nhóm tuổi.
5. **plot5_20HoPhoBien.py** → Biểu đồ thể hiện 20 họ phổ biến nhất của học sinh tham gia kỳ thi.

---

## 🛠 Yêu cầu
Cài đặt Python và các thư viện cần thiết:
```bash
pip install pandas matplotlib


