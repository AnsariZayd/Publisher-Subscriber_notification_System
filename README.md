# Publisher Subscriber Notification System

This is a simple implementation of a publisher-subscriber notification system using Flask.

## API Endpoints

1. **Subscribe to a Topic**
   - **URL**: `/subscribe`
   - **Method**: POST
   - **Body**:
     ```json
     {
       "topicId": "topic1",
       "subscriberId": "sub1"
     }
     ```

2. **Notify Subscribers of a Topic**
   - **URL**: `/notify`
   - **Method**: POST
   - **Body**:
     ```json
     {
       "topicId": "topic1"
     }
     ```

3. **Unsubscribe from a Topic**
   - **URL**: `/unsubscribe`
   - **Method**: POST
   - **Body**:
     ```json
     {
       "topicId": "topic1",
       "subscriberId": "sub1"
     }
     ```

4. **Get Subscriptions**
   - **URL**: `/subscriptions`
   - **Method**: GET

## Postman Collection

Import the following JSON configuration into Postman to test the APIs.

[Postman Collection]([link-to-postman-collection](https://api.postman.com/collections/34666427-1edb9203-55c1-4828-bbe8-37ed9f0023e0?access_key=PMAT-01J05R66J6VKRCAG1JKBW3MCEB))

## Running Locally

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install flask

