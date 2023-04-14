
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
curl --location 'http://127.0.0.1:5000/add-account' \
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
curl --location 'http://127.0.0.1:5000/login' \
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
curl --location 'http://127.0.0.1:5000/get-disasters?name=' \
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
