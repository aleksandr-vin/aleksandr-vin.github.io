---
title: "CHatGPT iOS App"
tags: mobile hackers chatgpt webrtc livekit proxy wss audio reverse-engineering debugging
---

ChatGPT iOS app has voice capabilities. There is no watchOS support. But I want it like Siri on my wrist.

Writing an watchOS app capable of recording an audio and stopping when no more text is transcribed (with the help of iOS companion app) is done. Now I need to reverse engineer the networking part of ChatGPT iOS app.

## Reversing ChatGPT iOS app

Using Charles proxy, and installing + trusting it's CA certificate on iPhone allows us to see what's is called by the app and what's inside.

Apart from some comms to https://chat.openai.com, that checks server status and profile data, we see one reply from https://ios.chat.openai.com/voice/get_token that points to wss://chatgpt.livekit.cloud:

```shell
% curl \
  -H "Host: ios.chat.openai.com" \
  -H "Cookie: __cf_bm=q5jG......GXHnlY=; _puid=user-DUj.....84%3D; _devicecheck=user-DUj....%3D; _cfuvid=coOlo....800000" \
  -H "accept: */*" \
  -H "content-type: application/json" \
  -H "oai-device-id: D8B0XXXX-XXXX-XXXX-XXXX-XXXXXX77E799" \
  -H "oai-client-type: ios" \
  -H "user-agent: ChatGPT/1.2023.311 (iOS 17.0.3; iPhone14,5; build 12705)" \
  -H "authorization: Bearer eyJhbGciOiJS...........MCGz32ehQBQ" \
  -H "accept-language: en-GB,en;q=0.9" \
  --compressed \
  "https://ios.chat.openai.com/voice/get_token" | jq .
{
  "url": "wss://chatgpt.livekit.cloud",
  "e2ee_key": "Z6apzs.....gJwN5",
  "context": "eyJhbGciOi..........64K7V46JAIWTSCE_Vg.-_W_xaze5z7T........................aDlB0uuw",
  "token": "eyJhbGciOiJIUzI1...........6IkpXVCJ9.eyJuYW1lIjoiIiwidmlkZW8.......WnJ4adZp_9XdI"
}
```

Where:

1. auth bearer token is JWT:
```
{
  "https://api.openai.com/profile": {
    "email": "aleksandr.vin@gmail.com",
    "email_verified": true
  },
  "https://api.openai.com/auth": {
    "poid": "org-oj.....",
    "user_id": "user-DUj...."
  },
  "iss": "https://auth0.openai.com/",
  "sub": "auth0|638e8...........53ec1",
  "aud": [
    "https://api.openai.com/v1",
    "https://openai.openai.auth0app.com/userinfo"
  ],
  "iat": 1699566816,
  "exp": 1700430816,
  "azp": "pdlLIX2Y..............5kBh",
  "scope": "openid profile email model.read model.request organization.read organization.write offline_access"
}
```

2. token in reply is a JWT:

```
{
  "name": "",
  "video": {
    "roomCreate": false,
    "roomList": false,
    "roomRecord": false,
    "roomAdmin": false,
    "roomJoin": true,
    "room": "fCA3X4........2vYGrN4",
    "canPublish": true,
    "canSubscribe": true,
    "canPublishData": true,
    "canPublishSources": [],
    "canUpdateOwnMetadata": false,
    "ingressAdmin": false,
    "hidden": false,
    "recorder": false
  },
  "metadata": "",
  "sha256": "",
  "sub": "User",
  "iss": "API3......Me8V",
  "nbf": 1700046186,
  "exp": 1700046206
}
```

3. context in reply looks like something encrypted (ChatGPT system context for their completion api?)

4. e2ee_key can be an end-to-end encryption key

Connecting to wss://chatgpt.livekit.cloud with some sample web app from https://docs.livekit.io/realtime/quickstarts/react/ with the token
do happen, but no activity or answer from ChatGPT participant:

![User and ChatGPT in chatgpt.livekit.cloud](/img/Screenshot 2023-11-15 at 14.26.21.png){: width="50%" }

Going further we run livekit server locally:

```shell
% docker run --rm livekit/livekit-server generate-keys
API Key:  APIX......Qu9
API Secret:  6hPC.......................rV3liV
% docker run --rm -p 7880:7880 -p 7881:7881 -p 7882:7882/udp \
  -e LIVEKIT_KEYS="APIX......Qu9: 6hPC.......................rV3liVV" \
  -e ROOM_EMPTY_TIMEOUT=0 \
  livekit/livekit-server
```

Then you need to generate token(s) for participants, using this nodejs script, for ex.:

```nodejs
const { AccessToken } = require('livekit-server-sdk');

const apiKey = "APIX......Qu9";
const apiSecret = "6hPC.......................rV3liV";

// if this room doesn't exist, it'll be automatically created when the first
// client joins
const roomName = 'name-of-room';

['ChatGPT', 'User'].forEach(participantName => {
  const at = new AccessToken(apiKey, apiSecret, {
    // identifier to be used for participant.
    // it's available as LocalParticipant.identity with livekit-client SDK
    identity: participantName,
  });
  at.addGrant({ roomJoin: true, room: roomName });

  const token = at.toJwt();
  console.log(participantName, 'access token', token);
});
```

Then joining the room as ChatGPT from web app and as User with `url` and `token` rewritten by Charles.

