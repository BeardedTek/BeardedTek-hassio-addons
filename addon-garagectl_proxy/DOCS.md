This addon creates a proxy to a server run separately from Home Assistant so that you can have the benefit of access in the sidebar without running it as an addon.

Note that this addon does not run a service itself.

## Configuration

### Option: `server`

The `server` option sets the address of the service.

This must be in the format `host:port`. The following are valid examples:

- `pi.local:80`
- `192.168.2.15:80`

## Required Dependencies
- Network access to running service