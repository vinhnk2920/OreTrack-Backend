<div align="center">
  <h1 style="color:#F3EB3B;"> Welcome to OreTrack Backend <img src="https://pic.chinesefontdesign.com/uploads/2017/11/chinesefontdesign.com-2017-11-16_10-37-52_166289.gif" width="75px"></h1>
</div>

<!-- TOC -->
* [OreTrack-Backend](#oretrack-backend)
  * [System design](#system-design)
    * [Use case diagram](#use-case-diagram)
    * [ERD](#erd)
  * [Tech stack](#tech-stack)
  * [Collection Postman](#collection-postman)
  * [API docs](#api-docs)
    * [1. API create account (admin)](#1-api-create-account-admin)
    * [2. API login](#2-api-login)
    * [3. API get disaster](#3-api-get-disaster)
    * [4. API list forecast](#4-api-list-forecast)
    * [5. API list alert message](#5-api-list-alert-message)
    * [6. API create alert message](#6-api-create-alert-message)
    * [6. API create alert message](#6-api-create-alert-message-1)
    * [7. API get SOS information](#7-api-get-sos-information)
    * [7. API get list SOS by disaster](#7-api-get-list-sos-by-disaster)
    * [8. API get near rescue](#8-api-get-near-rescue)
    * [9. API get rescue situation](#9-api-get-rescue-situation)
    * [10. API list coordinate rescue](#10-api-list-coordinate-rescue)
    * [11. API get detail sos](#11-api-get-detail-sos)
    * [12. API get detail sos](#12-api-get-detail-sos)
  * [Build Setup](#build-setup)
<!-- TOC -->

# OreTrack-Backend
Backend source code for OreTrack.
The purpose of OreTrack is to predict and prepare for emergency situations and to coordinate rescue efforts when disasters occur.


## System design

### Use case diagram
![](https://github.com/vinhnk2920/OreTrack-Backend/blob/main/static/Oretrack_usecase.png)

### ERD
![](https://github.com/vinhnk2920/OreTrack-Backend/blob/main/static/OreTrack-ER-diagram.png)

## Tech stack
1. Front-end: HTML, CSS (Bootstrap), JavaScript (VueJS)
2. Back-end: Python (flask)
3. Database: Mysql

## Collection Postman
![](https://github.com/vinhnk2920/OreTrack-Backend/blob/main/static/postman.png)

[Link postman collection](https://api.postman.com/collections/18193317-8662e077-45d6-403f-a821-52f4573142e7?access_key=PMAT-01GY3RQ2XSX6KTNC16X0A7RCWN)


## API docs

| Domain                        | Name       |
|-------------------------------|------------|
| https://backend.oretrack.life | production |
| http://127.0.0.1:5000         | local      |

### 1. API create account (admin)

> URL

```
{{url}}/add-account
```

> Params

| param         | type   | required |
|---------------|--------|----------|
| username      | string | YES      |
| password      | string | YES      |
| role          | int    | YES      |
| department_id | int    | YES      |

> CURL
```curl
curl --location '{{url}}/add-account' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho' \
--header 'Content-Type: application/json' \
--data '{
    "username": "vinhnk9",
    "password": "vinhnk2920",
    "role": 1,
    "department_id": 1
}'
```
> Success response
```json
{
    "data": [],
    "message": "Successfully registered!",
    "success": true
}
```

> False response
```json
{
    "data": [],
    "message": "User already exists!",
    "success": false
}
```

### 2. API login

> URL

```
{{url}}/login
```

> Params

| param    | type   | required |
|----------|--------|----------|
| username | string | YES      |
| password | string | YES      |


> CURL
```curl
curl --location '{{url}}/login' \
--header 'Content-Type: application/json' \
--data '{
    "username": "vinhnk9",
    "password": "vinhnk2920"
}'
```
> Success response
```json
{
    "message": "Login successful!!",
    "success": true,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho"
}
```

### 3. API get disaster

> URL

```
{{url}}/get-disasters
```

> Params

| param      | type     | required |
|------------|----------|----------|
| name       | string   | NO       |
| start_time | datetime | NO       |


> CURL
```curl
curl --location '{{url}}/get-disasters?name=' \
--header 'Content-Type: application/json' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```
> Success response
```json
{
    "data": [
        {
            "end_at": null,
            "full_address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
            "id": 1,
            "name": "Forest fire in Kon Tum",
            "risk_level": 3,
            "start_at": "Thu, 13 Apr 2023 15:00:03 GMT"
        }
    ],
    "message": "Get disasters successfully!",
    "success": true
}
```

### 4. API list forecast

> URL

```
{{url}}/list-forecast
```

> CURL
```curl
curl --location '{{url}}/list-forecast' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```
> Success response
```json
{
    "data": [
        {
            "disaster_name": "Động đất",
            "disaster_type": 1,
            "forecast_end": "Fri, 14 Apr 2023 00:00:00 GMT",
            "forecast_start": "Tue, 11 Apr 2023 00:00:00 GMT",
            "full_address": "xã Tản Lĩnh huyện Ba Vì",
            "id": 1,
            "image": null,
            "name": "ngập úng kèm theo lũ quét",
            "reported_by": "Trung tâm dự báo khí tượng thuỷ văn Việt Nam"
        }
    ],
    "message": "Get disasters successfully!",
    "success": true
}
```

### 5. API list alert message

> URL

```
{{url}}/list-alert-message
```

> CURL
```curl
curl --location '{{url}}/list-alert-message' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```
> Success response
```json
{
    "data": [
        {
            "content": "Thành phố Hà Nội thông báo đến các hộ gia đình trong địa phận xã Tiên Phong làm theo hướng dẫn sau đây để chuẩn bị phòng tránh tốt nhất cho bão số 8 sắp tới ",
            "created_at": "Sat, 15 Apr 2023 09:55:14 GMT",
            "created_by": 6,
            "disaster_id": 1,
            "id": 1,
            "name": "Tin nhắn cảnh báo",
            "updated_at": "Sat, 15 Apr 2023 09:55:14 GMT",
            "updated_by": null
        },
        {
            "content": "Thành phố Hà Nội thông báo bão số 8 đã đổ bộ, đội cứu hộ luôn sẵn sàng ứng cứu trong thời gian sớm nhất",
            "created_at": "Sat, 15 Apr 2023 09:56:57 GMT",
            "created_by": 6,
            "disaster_id": 1,
            "id": 2,
            "name": "Tin nhắn cảnh báo 2",
            "updated_at": "Sat, 15 Apr 2023 09:56:57 GMT",
            "updated_by": null
        }
    ],
    "message": "Get list alert message successfully!",
    "success": true
}
```

### 6. API create alert message

> URL

```
{{url}}/create-alert-message
```

> CURL
```curl
curl --location '{{url}}/create-alert-message' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Hướng dẫn kỹ năng an toàn trước lũ lụt 2",
    "disaster_id": 1,
    "content": "Để đảm bảo an toàn tính mạng và tài sản, người dân cần lưu ý: TRƯỚC LŨ: Thường xuyên theo dõi thông tin, cảnh báo mưa, lũ. Chuẩn bị thuyền, phao, bè, máng, vật nổi; gia cố nhà làm gác lửng, lối thoát trên mái nhà để ở tạm, cất giữ đồ đạc đề phòng lũ. Di chuyển gia súc, gia cầm, đồ đạc lên nơi cao để tránh ngập. Bảo vệ nguồn nước sạch; dự trữ nước uống, lương thực, thực phẩm, thuốc men, các vật dụng cần thiết đủ dùng ít nhất trong 7 ngày. Tìm hiểu, nắm bắt các tuyến đường sơ tán khẩn cấp đến nơi an toàn. Chủ động sơ tán khỏi vùng bãi sông, vùng thấp trũng, vùng có nguy cơ sạt lở, lũ quét, các công trường đang thi công.???? Dừng hoạt động tại các công trình đang thi công dở dang. Đề phòng lũ xảy ra vào ban đêm. Lưu giữ các số điện thoại và địa chỉ liên lạc trong trường hợp khẩn cấp.",
    "message_type": "tutorial"
}'
```
> Success response
```json
{
    "data": [],
    "message": "Create alert message successfully!",
    "success": true
}
```

### 6. API create alert message

> URL

```
{{url}}/create-alert-message
```

> Params

| param        | type   | required |
|--------------|--------|----------|
| name         | string | YES      |
| disaster_id  | int    | YES      |
| content      | string | YES      |
| message_type | string | YES      |

> CURL
```curl
curl --location '{{url}}/create-alert-message' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Hướng dẫn kỹ năng an toàn trước lũ lụt 2",
    "disaster_id": 1,
    "content": "Để đảm bảo an toàn tính mạng và tài sản, người dân cần lưu ý: TRƯỚC LŨ: Thường xuyên theo dõi thông tin, cảnh báo mưa, lũ. Chuẩn bị thuyền, phao, bè, máng, vật nổi; gia cố nhà làm gác lửng, lối thoát trên mái nhà để ở tạm, cất giữ đồ đạc đề phòng lũ. Di chuyển gia súc, gia cầm, đồ đạc lên nơi cao để tránh ngập. Bảo vệ nguồn nước sạch; dự trữ nước uống, lương thực, thực phẩm, thuốc men, các vật dụng cần thiết đủ dùng ít nhất trong 7 ngày. Tìm hiểu, nắm bắt các tuyến đường sơ tán khẩn cấp đến nơi an toàn. Chủ động sơ tán khỏi vùng bãi sông, vùng thấp trũng, vùng có nguy cơ sạt lở, lũ quét, các công trường đang thi công.???? Dừng hoạt động tại các công trình đang thi công dở dang. Đề phòng lũ xảy ra vào ban đêm. Lưu giữ các số điện thoại và địa chỉ liên lạc trong trường hợp khẩn cấp.",
    "message_type": "tutorial"
}'
```
> Success response
```json
{
    "data": [],
    "message": "Create alert message successfully!",
    "success": true
}
```

### 7. API get SOS information

> URL

```
{{url}}/get-sos-info
```

> Params

| param  | type | required |
|--------|------|----------|
| sos_id | int  | YES      |

> CURL
```curl
curl --location '{{url}}/get-sos-info?sos_id=1' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```
> Success response
```json
{
    "data": {
        "content": "I'm stuck in my home near the forest",
        "lat": 123.138,
        "lng": 12.761,
        "name": "Nguyen Hoang Nam",
        "status": null,
        "time": "Thu, 13 Apr 2023 19:51:11 GMT"
    },
    "message": "Get sos information successfully!",
    "success": true
}
```

### 7. API get list SOS by disaster

> URL

```
{{url}}/list-sos
```

> CURL
```curl
curl --location '{{url}}/list-sos?disaster_id=1' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```

> Params

| param    | type | required |
|----------|------|----------|
| disaster | int  | YES      |

> Success response
```json
{
    "data": [
        {
            "content": "I'm stuck in my home near the forest",
            "created_at": "Thu, 13 Apr 2023 19:51:11 GMT",
            "id": 1,
            "lat": 123.138,
            "lng": 12.761,
            "name": "Nguyen Hoang Nam",
            "number_of_people": null,
            "risk_level": 4,
            "status": null
        },
        {
            "content": "My cat curently stuck in the forest",
            "created_at": "Sat, 15 Apr 2023 15:54:25 GMT",
            "id": 2,
            "lat": 113.138,
            "lng": 12.16,
            "name": "Nguyen Quoc An",
            "number_of_people": 3,
            "risk_level": 3,
            "status": null
        }
    ],
    "message": "Get list sos successfully!",
    "success": true
}
```

### 8. API get near rescue

> URL

```
{{url}}/get-near-rescue
```

> CURL
```curl
curl --location '{{url}}/get-near-rescue?sos_id=2' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```

> Params

| param  | type | required |
|--------|------|----------|
| sos_id | int  | YES      |

> Success response
```json
{
    "data": [
        {
            "assigned_department": {
                "available": 4,
                "full_address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
                "id": 2,
                "member": 12,
                "phone": "0499284943"
            },
            "departments": [
                {
                    "address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
                    "available": 10,
                    "id": 1,
                    "member": 20,
                    "phone": "0399472948"
                },
                {
                    "address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
                    "available": 8,
                    "id": 2,
                    "member": 15,
                    "phone": "0399582948"
                },
                {
                    "address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
                    "available": 4,
                    "id": 3,
                    "member": 12,
                    "phone": "0499284943"
                }
            ]
        }
    ],
    "message": "Get near rescue successfully!",
    "success": true
}
```

### 9. API get rescue situation

> URL

```
{{url}}/create-coordinate-rescue
```

> CURL
```curl
curl --location '{{url}}/create-coordinate-rescue' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho' \
--header 'Content-Type: application/json' \
--data '{
    "coordinate_infor": [
        {
            "num_of_people": 3,
            "receive_team": 1
        },
        {
            "num_of_people": 5,
            "receive_team": 2
        }
    ],
    "disaster_id": 1,
    "order_team": 3
}'
```

> Params

| param            | type  | required |
|------------------|-------|----------|
| coordinate_infor | array | YES      |
| disaster_id      | int   | YES      |
| order_team       | int   | YES      |

> Success response
```json
{
    "data": [],
    "message": "Create coordinate rescue successfully!",
    "success": true
}
```

### 10. API list coordinate rescue

> URL

```
{{url}}/list-coordinate-rescue
```

> CURL
```curl
curl --location '{{url}}/list-coordinate-rescue?disaster_id=1&order_team=3' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```

> Params

| param       | type | required |
|-------------|------|----------|
| disaster_id | int  | YES      |
| order_team  | int  | YES      |

> Success response
```json
{
    "data": [
        {
            "id": 1,
            "num_of_people": 3,
            "receive_team": 1,
            "status": "success"
        },
        {
            "id": 2,
            "num_of_people": 5,
            "receive_team": 2,
            "status": "success"
        }
    ],
    "message": "List coordinate rescue successfully!",
    "success": true
}
```


### 11. API get detail sos

> URL

```
{{url}}/get-detail-sos
```

> CURL
```curl
curl --location '{{url}}/get-detail-sos?sos_id=1' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```

> Params

| param  | type | required |
|--------|------|----------|
| sos_id | int  | YES      |

> Success response
```json
{
    "data": {
        "address_id": 6,
        "content": "I'm stuck in my home near the forest",
        "id": 1,
        "lat": 123.138,
        "lng": 12.761,
        "name": "Nguyen Hoang Nam",
        "risk_level": 4,
        "status": null
    },
    "message": "Get detail sos successfully!",
    "success": true
}
```

### 12. API get detail sos

> URL

```
{{url}}/get-rescue-team
```

> CURL
```curl
curl --location '{{url}}/get-rescue-team?team_id=3' \
--header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho'
```

> Params

| param   | type | required |
|---------|------|----------|
| team_id | int  | YES      |

> Success response
```json
{
    "data": {
        "address": "Xã Ngọk Tem - huyện Kon Plong - tỉnh Kom Tum",
        "leader_name": null,
        "members": [
            {
                "email": null,
                "fullname": null,
                "phone": null
            },
            {
                "email": null,
                "fullname": null,
                "phone": null
            }
        ],
        "name": "Đội cứu hộ tây Ngok Pem",
        "num_of_member": 20,
        "phone": "0399472948"
    },
    "message": "Get detail sos successfully!",
    "success": true
}
```

## Build Setup

> flask --app app.py --debug run

