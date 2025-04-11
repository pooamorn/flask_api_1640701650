from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, BUs 1640701650 <!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ฟอร์มจองโรงแรม</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      padding: 20px;
    }

    .booking-form {
      background: white;
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .booking-form h2 {
      text-align: center;
    }

    .booking-form label {
      display: block;
      margin-top: 10px;
    }

    .booking-form input, .booking-form select {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    .booking-form button {
      margin-top: 15px;
      width: 100%;
      padding: 10px;
      background-color: #28a745;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }

    .booking-form button:hover {
      background-color: #218838;
    }
  </style>
</head>
<body>

  <div class="booking-form">
    <h2>จองโรงแรม</h2>
    <form action="#" method="post">
      <label for="name">ชื่อผู้จอง:</label>
      <input type="text" id="name" name="name" required>

      <label for="checkin">วันที่เช็คอิน:</label>
      <input type="date" id="checkin" name="checkin" required>

      <label for="checkout">วันที่เช็คเอาท์:</label>
      <input type="date" id="checkout" name="checkout" required>

      <label for="guests">จำนวนผู้เข้าพัก:</label>
      <select id="guests" name="guests">
        <option value="1">1 คน</option>
        <option value="2">2 คน</option>
        <option value="3">3 คน</option>
        <option value="4">4 คน</option>
      </select>

      <button type="submit">จองเลย</button>
    </form>
  </div>




</style>
</head>
<body>

<h1>ห้องพักโรงแรมสุดหรู</h1>

<div class="gallery">
  <div class="room">
    <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/d7/ca/34/rooftop-pool.jpg?w=1200&h=-1&s=1" alt="ห้องดีลักซ์">
    <div class="room-description">
      <h3>ห้องดีลักซ์</h3>
      <p>ตกแต่งหรูหรา พร้อมวิวทะเล</p>
    </div>
  </div>

  <div class="room">
    <img src="https://riverineplace.com/wp-content/uploads/2023/12/types-hotel-rooms.jpg" alt="ห้องสวีท">
    <div class="room-description">
      <h3>ห้องสวีท</h3>
      <p>มีอ่างจากุซซี่ส่วนตัว และห้องนั่งเล่น</p>
    </div>
  </div>

  <div class="room">
    <img src="https://q-xx.bstatic.com/xdata/images/hotel/max500/339430581.jpg?k=48a4ada6bad21abb470b505609f89e1b36adaab5310b1f4a2cbf8253a8969bfb&o=" alt="ห้องวิวภูเขา">
    <div class="room-description">
      <h3>ห้องวิวภูเขา</h3>
      <p>บรรยากาศเงียบสงบ เหมาะกับการพักผ่อน</p>
    </div>
  </div>
</div>




</body>
</html>
 '
    

if __name__ == '__main__':
    app.run(debug=True, port=80)
