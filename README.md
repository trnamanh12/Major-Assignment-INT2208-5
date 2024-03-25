# Phân tích bán hàng
Dự án này được kế thừa từ dự án https://github.com/NinhDT22022522/Mobile-e-commerce-review-sentiment-classification. Mọi tiến độ hay phân công công việc của dự án trước được lưu tại [đây]([url](https://rainy-infinity-73a.notion.site/Ph-n-c-ng-96e1de5cf7bb4b3a9bc4b643d763daf9?pvs=4)).

Bài tập lớn môn Công nghệ phần mềm INT2208 5

## Thành Viên

1. Bùi Đức Mạnh - 22022602
2. Lê Việt Hùng - 22022666
3. Đàm Thái Ninh - 22022522
4. Trần Nam Anh - 22022569
## Hướng Dẫn Cài Đặt


## Gitflow
### Được giao task mới
- Pull develop: `git pull origin develop`
- Tạo nhánh mới từ develop: `git checkout -b <tên-branch>`
- Code x3,14
### Đang làm task cũ
- Pull develop về nhánh hiện tại vào mỗi ngày làm việc mới: `git pull origin develop`
- Code x3,14
- Commit và push code lên github mỗi khi kết thúc ngày làm việc:
  - `git add.`
  - `git commit -m "Message"`
  - `git push origin <tên-branch-hiện-tại>`

## Một vài câu lệnh git
- `git clone <url>`: clone repository về máy
- `git add .`: add toàn bộ thay đổi để commit
- `git commit -m "Commit Message"`: commit toàn bộ thay đổi với message chỉ định vào nhánh hiện tại
- `git push origin <tên-branch>`: push toàn bộ commit (tức là sự thay đổi về các file) ở nhánh hiện tại lên nhánh được chỉ định trên github
- `git pull origin <tên-branch>`: lấy toàn bộ commit (tức là sự thay đổi về các file) ở nhánh được chỉ định từ github về nhánh hiện tại
- `git checkout <tên-branch>`: chuyển sang nhánh được chỉ định
- `git checkout -b <tên-branch>`: tạo branch mới và chuyển sang đó (tên branch không được trùng nhau)
- `git branch -d <tên-branch>`: xoá branch được chỉ định khỏi máy (đương nhiên toàn bộ thay đổi có ở nhánh này cũng sẽ mất hết)
- **Nếu không quen có thể sử dụng GUI của VSC**
