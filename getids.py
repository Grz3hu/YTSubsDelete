import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    #Get subscriptions list
    request = youtube.subscriptions().list(
        part="snippet,contentDetails",
        maxResults=50,
        mine=True
    )

    subs=[]

    data = request.execute()
    items=data.get('items')
    for i in items:
        subs.append(i.get('snippet').get('resourceId').get('channelId'))
    print(subs)

if __name__ == "__main__":
    main()
