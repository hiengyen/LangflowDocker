# Sử dụng image Python chính thức
FROM python:3.9-slim

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép requirements.txt và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn và file JSON
COPY . .

# Mở cổng 8080
EXPOSE 8080

# Lệnh chạy ứng dụng
CMD ["python", "app.py"]
