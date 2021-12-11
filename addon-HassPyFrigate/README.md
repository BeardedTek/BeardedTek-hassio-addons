# HassPyFrigate
## Nicer Frigate Notifications

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

# HassPyFrigate
## Python 3 CGI script for better looking notifications
![v0.1]: https://github.com/beardedtek/hasspyfrigate/img/HassPyFrigate.png

# Home Assistant Automations

## Android Companion App Notification
#### Example Android Actionable Notification
Click on "Event Viewer" to view HassPyFrigate Event Viewer
![Android Actionable Notification]: https://github.com/beardedtek/hasspyfrigate/img/AndroidNotification.png
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
              http://YOUR_SERVER/cgi-bin/hasspyfrigate.py?id={{trigger.payload_json['after']['id']}}&camera={{trigger.payload_json['after']['camera']}}&bbox=true&url=https://hass.jeandr.net/api/frigate/notifications/&time={{trigger.payload_json['after']['start_time']}}&css=../css/hasspyfrigate.css#
        image: >-
          /api/frigate/notifications/{{trigger.payload_json['after']['id']}}/snapshot.jpg?bbox=1
        tag: '{{trigger.payload_json["after"]["id"]}}'
        alert_once: true
mode: single
```

[HassPyFrigate]: https://github.com/beardedtek/hasspyfrigate
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
