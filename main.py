import functions_framework
import google.auth
from google.auth.transport.requests import AuthorizedSession

@functions_framework.http
def hello_http(request):
    
    credentials, project = google.auth.default()
    authed_session = AuthorizedSession(credentials)

    body={
        "config": {
            "language_code": "en-US"
        },
        "audio":{
            "uri":"gs://your-bucket/your-input-file"
        },
        "output_config": {
            "gcs_uri":"gs://your-bucket/your-output-file"
        }
    }

    recognizeResult = authed_session.post(url='https://speech.googleapis.com/v1/speech:longrunningrecognize', json=body)

    print(f"recognizeResult: {recognizeResult.json()}")

    ops = recognizeResult.json()

    print(f"ops name: {ops['name']}")

    getOpsResult = authed_session.get(f"https://speech.googleapis.com/v1/operations/{ops['name']}")
    
    return getOpsResult.json()
