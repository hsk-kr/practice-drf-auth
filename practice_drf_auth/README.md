# practice drf auth

## Model

- User: `django.contrib.auth.models.User`
    | field            | description                                          | type     |
    | ---------------- | ---------------------------------------------------- | -------- |
    | username         | Username                                             | char     |
    | first_name       | First name                                           | char     |
    | last_name        | Last name                                            | char     |
    | email            | Email                                                | char     |
    | password         | Password                                             | char     |
    | groups           | Relationship to group                                | FK       |
    | user_permissions | Relationship to permission                           | FK       |
    | is_staff         | Whether this usre can access the admin site          | boolean  |
    | is_active        | Whether this use account should be considered active | boolean  |
    | is_superuser     | Use all permissions                                  | boolean  |
    | last_login       | A datetime of the user's last login                  | datetime |
    | date_joined      | When the account was created                         | datetime |

## RestAPI Documentation

### Sign up

- url: `/account/signup`
- method: `POST`
- body:
    ```
    {
        username,
        first_name,
        last_name,
        email,
        password
    }
    ```
- response: `200 OK`
    ```
    {
        token: [token]
    }
    ```

### Sign in

- url: `/account/signin`
- method: `POST`
- body: 
    ```
    {
        username,
        password
    }
    ```
- response: `200 OK`
    ```
    {
        token: [token]
    }
    ```

### Get My Account

- url: `/account`
- method: `GET`
- header:
    ```
    {
        'Authorization: Token [token]'
    }
    ```
- reponse: `200 OK`
    ```
    {
        [User]
    }
    ```

### Update My Account

- url: `/account`
- method: `PATCH`
- header:
    ```
    {
        'Authorization: Token [token]'
    }
- response: `200 OK`

### Delete My Account

- url: `/account`
- method: `DELETE`
- header:
    ```
    {
        'Authorization: Token [token]'
    }
- response: `200 OK`