# BeardedTek-hassio-addons
My modified hassio-addons.

# Available Addons
  - tailscale 1.17.68 : This allows better subnet routing that the community hassio version.
  - GarageCTL Proxy : This allows you to run GarageCTL with INGRESS access. 
    - https://github.com/BeardedTek/garagectl
  - HassPyFrigate : Nicer Looking Frigate Notifications (DEPRICATED)
  - fEVR 0.3 : Rebuild of HassPyFrigate but WAY better
   
# HassPyFrigate
 - https://github.com/beardedtek/HassPyFrigate


## Python 3 CGI script for better looking notifications

![v0.1](https://github.com/BeardedTek/HassPyFrigate/raw/main/img/HassPyFrigate.png)

# SETUP

In Home Assistant Supervisor, add this repository, select and install HassPyFrigate

# Home Assistant Automations

## Android Companion App Notification

#### Example Android Actionable Notification

Click on "Event Viewer" to view HassPyFrigate Event Viewer

![Android Actionable Notification](https://github.com/BeardedTek/HassPyFrigate/raw/main/img/AndroidNotification.png)

The following Automation will send an actionable notification to the android companion app (Should work with iOS as well)

```

alias: HassPyFrigate Alert

description: HassPyFrigate Object Detection Alerts Using Frigate

trigger:

  - platform: mqtt

    topic: frigate/events

condition:

  - condition: template

    value_template: '{{ trigger.payload_json["type"] == "end" }}'

  - condition: template

    value_template: |-

      {{ trigger.payload_json["after"]["label"] == "person" or 

         trigger.payload_json["after"]["label"] == "car" or

         trigger.payload_json["after"]["label"] == "bird" or

         trigger.payload_json["after"]["label"] == "dog" or

         trigger.payload_json["after"]["label"] == "cat" or

         trigger.payload_json["after"]["label"] == "bear" or

         trigger.payload_json["after"]["label"] == "horse" 

      }}

action:

  - service: notify.mobile_app_sm_g986u1

    data:

      message: '{{ trigger.payload_json["after"]["label"] | title }} Detected'

      data:

        notification_icon: mdi:cctv

        ttl: 0

        priority: high

        sticky: true

        actions:

          - action: URI

            title: Snapshot

            uri: >-

              http://HOME_ASSISTANT_URL:8001/cgi-bin/hasspyfrigate.py?id={{trigger.payload_json['after']['id']}}&camera={{trigger.payload_json['after']['camera']}}&bbox=true&url=https://hass.jeandr.net/api/frigate/notifications/&time={{trigger.payload_json['after']['start_time']}}&css=../css/hasspyfrigate.css#

        image: >-

          /api/frigate/notifications/{{trigger.payload_json['after']['id']}}/snapshot.jpg?bbox=1

        tag: '{{trigger.payload_json["after"]["id"]}}'

        alert_once: true

mode: single

```
## IMPORTANT
If you use NGINX or similar proxy methods, you will need to add a new proxy host for port 8001 on your home assistant url.
Personally, I have a $5 linode set up with tailscale to my HA instance and nginx proxying both my home assistant, and my hasspyfrigate.
