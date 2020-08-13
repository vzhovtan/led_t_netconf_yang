from ncclient import manager

loopback_filter = """
    <filter>
      <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
          <name>Loopback0</name>
          <state/>
        </interface>
      </interfaces>
    </filter>
"""

with manager.connect(
    host='<selected_device_ip_address>',
    port=830,
    username='my_username',
    password='my_password',
    hostkey_verify=False,
    device_params={'name':'iosxr'}
) as m:
    # capturing server's capabilities
    for capability in m.server_capabilities:
        print(capability)

    loopback_status = m.get(loopback_filter).data_xml
    print(loopback_status)