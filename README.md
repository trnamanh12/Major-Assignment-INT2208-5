# IntelliPurchase
## Báo cáo dự án: [link](https://www.notion.so/B-o-c-o-d-n-6466d99781d04cd9954d3b9336898c2f)

## Link dự án trước: [github](https://github.com/baitaploncnpm66/Mobile-e-commerce-review-sentiment-classification)
## Tài liệu về hệ thống:
- Problem Statement: [link](https://www.notion.so/M-t-v-n-b2e73a30053c4f6cb587a579313c0ff7?pvs=21)
- System Glossary: [link](https://www.notion.so/Ch-gi-i-h-th-ng-IntelliPurchase-d4f063a56cbd47ff87314c133c6407b0?pvs=21)
- System Specification: [link](https://www.notion.so/c-t-h-th-ng-IntelliPurchase-66e49c81288241d19ba850a029ae237d?pvs=21)
- System Supplementary Specification: [link](https://www.notion.so/c-t-b-sung-h-th-ng-IntelliPurchase-1c95bb4efb8a43a5a601621baf20ebf2?pvs=21)
- Scenarios, User Stories: [link](https://www.notion.so/Scenarios-v-User-stories-41987e52c308475fac5aafa920805ae6?pvs=21)
- User Manual: [link](https://www.notion.so/H-ng-d-n-s-d-ng-User-Manual-763c1e9529e04bccb7b9a24e78034a86?pvs=21)

# Bài tập lớn môn Công nghệ phần mềm INT2208 5
# Trang web phân tích bán hàng IntelliPurchase

## Thành Viên

1. Bùi Đức Mạnh - 22022602
2. Lê Việt Hùng - 22022666
3. Đàm Thái Ninh - 22022522
4. Trần Nam Anh - 22022569

## Hướng Dẫn Cài Đặt
```
git clone <url>
pip install -r requirements.txt
cd IntelliPurchase
python manage.py migrate
python manage.py runserver
```

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

## Phản hồi và Đóng góp

Chúng tôi cam kết phản hồi và đánh giá mọi yêu cầu từ cộng đồng người dùng. Bất kỳ issues, pull requests hoặc ý kiến đóng góp nào cũng được đánh giá và giải quyết một cách nhanh chóng.

Nếu bạn gặp bất kỳ vấn đề hoặc có ý kiến đóng góp, vui lòng tạo một issue mới hoặc một pull request. Chúng tôi luôn đánh giá cao sự hợp tác của cộng đồng và sẵn lòng cải thiện dự án cùng với bạn.
