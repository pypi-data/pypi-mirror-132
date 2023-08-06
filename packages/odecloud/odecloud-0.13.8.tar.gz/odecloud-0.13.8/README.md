# Official OdeServer Python API's Client

## Getting Started & Usage

1. Installation:

- Use Poetry:
    ```sh
    $ poetry add odecloud
    ```
- Or, use Pip:
    ```sh
    $ pip install odecloud
    ```

2. Instantiate your connection to OdeCloud's API:

- If you don't know your client credentials:
    ```py
    api = Api('https://server.odecloud.app/api/v1') # All API calls will be made to this domain.
    api.login('your-email@here.com', 'your_password')
    ```

- If you already know your client credentials:<br>
    ```py
    api = Api(
        base_url='https://server.odecloud.app/api/v1', # All API calls will be made to this domain
        client_key='YOUR CLIENT KEY',
        client_secret='YOUR CLIENT SECRET',
    )
    ```

3. Now, any calls can be made to OdeCloud's API. Examples below:
    ```py
    api.comments.get(createdBy=random_user_id) # GET /api/v1/comments?createdBy=random_user_id/
    api.comments.post(data=expected_payload) # POST /api/v1/comments/
    api.comments(random_comment_id).patch(data=expected_payload) # PATCH /api/v1/comments/random_comment_id/
    api.comments(random_comment_id).delete() # DELETE /api/v1/comments/random_comment_id/
    ```
Happy coding!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)