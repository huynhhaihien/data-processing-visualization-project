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

├── draw_data.txt # Dữ liệu thô sau khi crawl từ web

├── clean_data.csv # Dữ liệu đã xử lý và làm sạch

├── process_all.py # File xử lý chính: HTML -> CSV sạch

├── process_1_row.py # File xử lý thử cho 1 thí sinh (phục vụ kiểm tra logic ban đầu)

├── exception.txt # Danh sách SBD không hợp lệ (dùng trong process_all.py)

├── unicode.txt # Bảng chuyển ký tự lỗi sang tiếng Việt chuẩn (dùng trong process_all.py)

├── Vẽ biểu đồ/ # Thư mục chứa các file Python để vẽ biểu đồ

│ ├── plot1_SoHS_bo_thi.py # Biểu đồ cột: Số học sinh bỏ thi của từng môn

│ ├── plot2_So_mon_hs_thi.py # Biểu đồ tròn: Phân bố số môn mà học sinh thi (vd: thi 5 môn = 30%)

│ ├── plot3_DiemTB_theo_mon.py # Biểu đồ cột: Điểm trung bình của học sinh theo từng môn

│ ├── plot4_DiemTB_theo_tuoi.py # Biểu đồ cột + đường: Điểm trung bình từng môn theo nhóm tuổi

│ └── plot5_20HoPhoBien.py # Biểu đồ: 20 họ phổ biến nhất của học sinh tham gia kỳ thi

└── README.md # Mô tả dự án
---

# 💾 Dữ liệu lớn

File `draw_data.txt` quá lớn để upload lên GitHub (>100MB).  
Bạn có thể tải file này từ Google Drive:

[draw_data.txt](https://drive.google.com/file/d/1B0JyN7517X2zA5vNKyil5W6Yhl7fSdpG/view?usp=drive_link)

Sau khi tải về, giải nén vào thư mục dự án để sử dụng.
## 📊 Biểu đồ trực quan hóa
1. **plot1_SoHS_bo_thi.py** → Biểu đồ cột thể hiện số lượng học sinh bỏ thi của từng môn.
2. **plot2_So_mon_hs_thi.py** → Biểu đồ tròn thể hiện tỷ lệ số môn học sinh đăng ký thi (ví dụ: thi 5 môn chiếm 30%).
3. **plot3_DiemTB_theo_mon.py** → Biểu đồ cột thể hiện điểm trung bình của học sinh theo từng môn.
4. **plot4_DiemTB_theo_tuoi.py** → Biểu đồ cột kết hợp đường thể hiện điểm trung bình từng môn học theo tuổi.
5. **plot5_20HoPhoBien.py** → Biểu đồ thể hiện 20 họ phổ biến nhất của học sinh tham gia kỳ thi.

---

## 🛠 Yêu cầu
Cài đặt Python và các thư viện cần thiết:
```bash
  pip install pandas matplotlib
```


## 🚀 Cách chạy
1. Xử lý toàn bộ dữ liệu HTML thành dữ liệu sạch
```bash
    python process_all.py
```
2. (Tuỳ chọn) Kiểm tra xử lý cho 1 thí sinh
```bash
    python process_1_row.py
```
3. Vẽ biểu đồ
Chạy file Python tương ứng trong thư mục Vẽ biểu đồ/, ví dụ:
  ```bash
    python "Vẽ biểu đồ/plot1_SoHS_bo_thi.py"
  ```
📌 Ghi chú
  exception.txt và unicode.txt là dữ liệu hỗ trợ cho quá trình xử lý trong process_all.py.

👤 Tác giả: Huỳnh Hải Hiền

👤 Giáo viên hướng dẫn: Lại Tuấn Dũng


