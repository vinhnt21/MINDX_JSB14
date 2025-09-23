---
title: markmap
markmap:
  colorFreezeLevel: 2
  initialExpandLevel: 3
  maxWidth: 300
---
# JSB Review

## Các khái niệm cơ bản về Web

### Cách Web hoạt động
- Browser (Request) -> Server (Response) -> Browser (Render)
- #### URL (Uniform Resource Locator)
  - Địa chỉ duy nhất của tài nguyên
  - `protocol://domain.name/path?query`
- #### IP Address
  - Địa chỉ số định danh thiết bị
  - Ví dụ: `172.217.167.78`
- #### Domain Name
  - Tên dễ nhớ thay cho địa chỉ IP
  - Ví dụ: `google.com`
- #### Server
  - Máy tính lưu trữ và cung cấp tài nguyên website
- #### Web 1, Web 2, Web 3
  - **Web 1.0**: Read-Only Web (Tĩnh)
    - Ví dụ: Trang web cá nhân chỉ hiển thị thông tin, không có tương tác.
  - **Web 2.0**: Social Web (Tương tác, người dùng tạo nội dung)
    - Ví dụ: Facebook, YouTube, Blog cá nhân cho phép bình luận, chia sẻ.
  - **Web 3.0**: Semantic & Decentralized Web (Phi tập trung, AI)
    - Ví dụ: Các ứng dụng blockchain, DApps, trợ lý ảo thông minh.

### Các thành phần của Web
- #### Header (Đầu trang)
  - Chứa logo, menu điều hướng
- #### Footer (Chân trang)
  - Chứa thông tin bản quyền, liên kết phụ
- #### Sidebar (Thanh bên)
  - Chứa thông tin bổ sung, danh mục
- #### Main (Content)
  - Khu vực nội dung chính của trang

## HTML (HyperText Markup Language)
- Ngôn ngữ đánh dấu, tạo cấu trúc và nội dung cho web (Bộ xương)

### Các thành phần chính của một trang HTML
- ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>Tiêu đề</title>
    </head>
    <body>
      </body>
  </html>
  ```

### Các thẻ HTML phổ biến

  - #### `<div>`
      - Thẻ khối để nhóm các phần tử
      - Ví dụ: `<div>Nội dung</div>`
  - #### `<h1>`, `<h2>`, ..., `<h6>`
      - Thẻ tiêu đề, phân cấp từ 1 đến 6
      - Ví dụ: `<h1>Tiêu đề lớn</h1>`
  - #### `<p>`
      - Thẻ đoạn văn
      - Ví dụ: `<p>Đây là một đoạn văn.</p>`
  - #### `<a>`
      - Thẻ liên kết (hyperlink)
      - Ví dụ: `<a href="https://google.com">Đi đến Google</a>`
  - #### `<img>`
      - Thẻ hình ảnh
      - Ví dụ: `<img src="image.jpg" alt="Mô tả ảnh">`
  - #### `<ul>`, `<ol>`, `<li>`
      - Thẻ danh sách (không thứ tự, có thứ tự, mục)
      - Ví dụ: `<ul><li>Mục 1</li><li>Mục 2</li></ul>`
  - #### `<blockquote>`
      - Trích dẫn một khối văn bản
      - Ví dụ: `<blockquote>"Trích dẫn"</blockquote>`
  - #### `<pre>`
      - Hiển thị văn bản theo định dạng sẵn
      - Ví dụ: `<pre>Text đã định dạng</pre>`
  - #### `<form>`
      - Biểu mẫu nhập liệu
      - Ví dụ: `<form action="/submit"></form>`
  - #### `<input>`
      - Trường nhập liệu trong form (text, password, submit,...)
      - Ví dụ: `<input type="text" placeholder="Tên của bạn">`
  - ...
### Attributes (Thuộc tính) của thẻ HTML

  - Cung cấp thêm thông tin cho thẻ
  - #### class
      - Gán tên lớp để định dạng bằng CSS
      - Ví dụ: `<p class="text-red">...</p>`
  - #### id
      - Định danh duy nhất cho một phần tử
      - Ví dụ: `<div id="header">...</div>`
  - #### href
      - (Hypertext Reference) - Đường dẫn cho thẻ `<a>`
      - Ví dụ: `<a href="/about.html">Về chúng tôi</a>`
  - #### src
      - (Source) - Nguồn cho thẻ `<img>`, `<script>`
      - Ví dụ: `<img src="logo.png">`
  - #### alt
      - (Alternative) - Văn bản thay thế cho hình ảnh
      - Ví dụ: `<img src="logo.png" alt="Logo công ty">`
  - ...
## CSS (Cascading Style Sheets)

  - Ngôn ngữ tạo kiểu, trang trí cho HTML (Da, tóc, quần áo)

### Cách sử dụng CSS trong HTML

  - #### Inline CSS
      - Dùng thuộc tính `style` trực tiếp trong thẻ HTML
      - Ví dụ: `<p style="color: blue;">Văn bản màu xanh</p>`
  - #### Internal CSS
      - Dùng thẻ `<style>` trong `<head>`
      - Ví dụ:
        ```html
        <head>
          <style>
            h1 { color: red; }
          </style>
        </head>
        ```
  - #### External CSS
      - Dùng file `.css` riêng và liên kết bằng thẻ `<link>` (Khuyến khích)
      - Ví dụ:
        ```html
        <head>
          <link rel="stylesheet" href="style.css">
        </head>
        ```

### Các loại selector trong CSS

  - **Element**: `p { ... }`
      - Ví dụ: `p { color: black; }` (Áp dụng cho tất cả các thẻ `<p>`)
  - **Class**: `.ten-class { ... }`
      - Ví dụ: `.button { background-color: blue; }` (Áp dụng cho các thẻ có `class="button"`)
  - **ID**: `#ten-id { ... }`
      - Ví dụ: `#header { font-size: 24px; }` (Áp dụng cho thẻ có `id="header"`)
  - **Attribute**: `[type="text"] { ... }`
      - Ví dụ: `input[type="submit"] { cursor: pointer; }` (Áp dụng cho thẻ `<input>` có `type="submit"`)
  - **Pseudo-class**: `:hover`, `:focus`
      - Ví dụ: `a:hover { color: green; }` (Áp dụng khi di chuột qua thẻ `<a>`)
  - ...
### Box Model (Mô hình hộp)

  - **Content**: Nội dung
      - Ví dụ: Kích thước thật của văn bản/hình ảnh.
  - **Padding**: Vùng đệm bên trong
      - Ví dụ: `padding: 10px;` (Tạo khoảng trống 10px quanh nội dung)
  - **Border**: Đường viền
      - Ví dụ: `border: 1px solid black;` (Viền 1px, màu đen)
  - **Margin**: Khoảng cách bên ngoài
      - Ví dụ: `margin: 20px;` (Tạo khoảng cách 20px với các phần tử khác)
  - ...
### Position

  - `static` (mặc định)
      - Ví dụ: Phần tử hiển thị theo luồng tài liệu thông thường.
  - `relative`
      - Ví dụ: `position: relative; top: 10px;` (Di chuyển 10px từ vị trí gốc)
  - `absolute`
      - Ví dụ: `position: absolute; top: 0; right: 0;` (Định vị tuyệt đối theo phần tử cha `relative`)
  - `fixed`
      - Ví dụ: `position: fixed; top: 0;` (Luôn cố định trên màn hình, không cuộn)
  - `sticky`
      - Ví dụ: `position: sticky; top: 0;` (Cố định khi cuộn đến một vị trí nhất định)
  - ...
### Display

  - `block` (chiếm cả dòng)
      - Ví dụ: `div { display: block; }` (Mỗi `div` sẽ bắt đầu trên một dòng mới)
  - `inline` (chỉ chiếm đủ chiều rộng)
      - Ví dụ: `span { display: inline; }` (Các `span` sẽ nằm trên cùng một dòng)
  - `inline-block`
      - Ví dụ: `img { display: inline-block; width: 100px; }` (Cho phép đặt chiều rộng/chiều cao nhưng vẫn nằm trên cùng dòng)
  - `none` (ẩn)
      - Ví dụ: `p { display: none; }` (Ẩn hoàn toàn phần tử)
  - `flex`
      - Ví dụ: `div.container { display: flex; }` (Biến một phần tử thành container flex)
  - ...
### Flexbox

  - Mô hình layout 1 chiều (hàng hoặc cột)
  - **Container**: `display: flex`, `justify-content`, `align-items`, `flex-direction`
      - Ví dụ: 
        ```css
        .flex-container {
          display: flex;
          justify-content: center; /* Căn giữa theo chiều ngang */
          align-items: center;   /* Căn giữa theo chiều dọc */
          flex-direction: row;   /* Sắp xếp các mục theo hàng */
        }
        ```

### Một số thuộc tính CSS cơ bản khác

  - #### font chữ
      - `font-size`
        - Ví dụ: `font-size: 16px;`
      - `font-family`
        - Ví dụ: `font-family: Arial, sans-serif;`
      - `font-weight`
        - Ví dụ: `font-weight: bold;`
  - #### background
      - `background-color`
        - Ví dụ: `background-color: #f0f0f0;`
      - `background-image`
        - Ví dụ: `background-image: url('bg.png');`
  - #### color
      - Đặt màu cho chữ
        - Ví dụ: `color: blue;`
  - ...
### Responsive Web Design
- Thiết kế web để hiển thị tốt trên mọi thiết bị (máy tính, tablet, điện thoại)
- #### Media Queries
  - Quy tắc CSS áp dụng dựa trên đặc điểm thiết bị (chiều rộng màn hình, loại thiết bị)
  - Ví dụ:
    ```css
    @media (max-width: 768px) {
      .my-element {
        width: 100%;
        font-size: 14px;
      }
    }
    ```

## Bootstrap

  - Framework CSS phổ biến nhất để xây dựng web responsive nhanh chóng

### Cách sử dụng

  - Dùng CDN (Content Delivery Network)
      - Ví dụ: Thêm `<link>` và `<script>` vào HTML từ Bootstrap CDN.
  - Liên kết file CSS và JS vào file HTML
      - Ví dụ: 
        ```html
        <head>
          <link rel="stylesheet" href="bootstrap.min.css">
        </head>
        <body>
          <script src="bootstrap.bundle.min.js"></script>
        </body>
        ```

### Các thành phần chính

  - #### Hệ thống lưới (Grid System)
      - Chia layout thành 12 cột
      - Sử dụng `.container`, `.row`, `.col-*`
      - Ví dụ: 
        ```html
        <div class="container">
          <div class="row">
            <div class="col-sm-4">Cột 1</div>
            <div class="col-sm-8">Cột 2</div>
          </div>
        </div>
        ```
  - #### Các thành phần (Components)
      - `Button`
        - Ví dụ: `<button class="btn btn-primary">Nút chính</button>`
      - `Navbar`
        - Ví dụ: `<nav class="navbar navbar-expand-lg navbar-light bg-light">...</nav>`
      - `Card`
        - Ví dụ: `<div class="card">...</div>`
      - `Form`
        - Ví dụ: `<form>...</form>`
      - `Modal`
        - Ví dụ: `<div class="modal">...</div>`
  - #### Các lớp tiện ích (Utility Classes)
      - **Spacing**: `m-*` (margin), `p-*` (padding)
        - Ví dụ: `<div class="mt-3 p-2">...</div>` (margin-top: 1rem, padding: 0.5rem)
      - **Colors**: `text-primary`, `bg-danger`
        - Ví dụ: `<p class="text-primary bg-danger">...</p>` (Chữ xanh, nền đỏ)
      - **Flexbox**: `d-flex`, `justify-content-center`
        - Ví dụ: `<div class="d-flex justify-content-center">...</div>` (Container flex, căn giữa nội dung)
      - **Text**: `text-center`, `fw-bold`
        - Ví dụ: `<p class="text-center fw-bold">...</p>` (Văn bản căn giữa, in đậm)