
# OreTrack

## 1. API create account (admin)

> URL

```
{{url}}/add-account
```

> Params

| param    | type   | required |
|----------|--------|----------|
| username | string | YES      |
| password | string | YES      |
| role     | int    | YES      |

> CURL
```curl
curl --location '{{url}}/add-account' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJDlKaktkSFF3MEVUVWY0U0skYWNiYmQ2ZjgzMmFhNTE4Mjk5NDMyZDA0MzNmMmI1YWZkZGI1MTY1NGQzNzA3YTg4Y2Y0MTU5MWYzN2MwYTQyNSJ9.71t39P09T81WEg9IjFXUEWRzJ6fAOqcR5KlcQ9krJho' \
--header 'Content-Type: application/json' \
--data '{
    "username": "vinhnk9",
    "password": "vinhnk2920",
    "role": 1
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

## 2. API login

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

## 3. API get disaster

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

## 4. API list forecast

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

## 5. API list alert message

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