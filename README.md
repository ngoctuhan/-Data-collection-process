# Data-collection-process

Qúa trình thu thập dữ liệu cho bài toán sử dụng video và sensor trên đồng hồ thông minh

I. Thiết bị

1. Máy quay: thiết bị có gắn camera như smartphone, webcam ..
2. Smartwatch android: sử dụng thêm ứng dụng sensor logger giúp ghi lại dữ liệu từ 2 cảm biến acc và gcc trên đồng hồ
3. Chân máy để cố định góc quay


II. Thao tác setup

Cố định góc quay với người quay sao cho có thể quay bán thân chân dung từ hông lên đến hết mặt.
Đeo đồng hồ ghi lại mã seri để xác định đồng hồ nào bên trái đồng hồ nào bên phải.

III. Bắt đầu quay

i. Start quay từ video trước, sau đó khởi động ứng dụng SENSOR LOGGER trên đồng hồ theo thứ tự bên trái trước và bên phải sau
    Mục đích giúp dễ dàng đồng bộ thời gian giúp cho việc xử lý dữ liệu sau dễ dàng hơn.
    
ii. Sau đó người quay giữ im lặng trong khoảng 3s và sau đó dơ tay lên vỗ tay thật mạnh, và lại để tay lại trang thái cân bằng.

iii.Quay theo kịch bạn có sẵn: mỗi thao tác thực hiện 3-5s sau đó lại nghỉ 1-2s và bắt đầu. 
  Thời gian thực hiện tầm 15-20p thì nghỉ ngơi,
  Sau mỗi đợt quay tắt đồng hồ trước sau đó tắt video ( không cần quan tâm thứ tự đồng hồ)

IV. Xử lý dữ liệu sau quay

i.  Tạo một thư mục N_x: x có thể là tên người hoặc ID người quay đánh số từ 1 - n.

ii. Trong thư mục N_x có 3 thư mục con gồm: VIDEO chứa các video, HAND-LEFT chứa các file data left, HAND-RIGHT chứa data sensor phải

iii.Chạy file replace_name_file.py thay đổi đường dẫn thư mục N_x tại dòng 34 để chuẩn hóa các tên file định dạng Nx_VIDEO_Part_x VÀ Nx_SENSOR_Part_x_L|R

iv. Gán nhãn video và dữ liệu theo hướng dẫn theo video tại link: https://www.youtube.com/watch?v=tZFr1pmB4zA&t=1s 

v.  Sau khi gán nhãn lưu video vào đúng thư mục N_x 

vi. Thực hiện gán như vậy với các thư mục khác

V. Cut dữ liệu

i.   Trước hết cắt dữ liệu video chạy file cut_video.py chỉnh thdm số tại dòng 97 98 99 bao gồm N_x, và số phần video

ii.  Video cut ra được lưu vào thư mục đặt tên bạn đặt trước chỉnh đường dẫn tại dòng: 41 42 89  

iii. Chuẩn hóa data data left-right sử dụng ELAN thêm 2 file linked ứng tay trái và phải video kéo gán nhãn từ điểm vỗ
tay trái và tay phải ta được thời gian chênh lệch

iii. Export data hand left, hand-right tại 2 file: export_sensor_data.py và file export_data_sensor_left.py
    Để export chỉ cần thay đổi đường dẫn của các thư mục trong hàm main. Hàm for là id của người từ 1 - n
    
iv. Như vậy được dữ liệu rồi

VI. Các file còn lại



