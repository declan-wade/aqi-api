import paho.mqtt.subscribe as subscribe

def listener25():
    msg = subscribe.simple("aqi/sensor/particulate_matter_25m_concentration/state", auth = {'username':"agent", 'password':"passwd"}, hostname="10.1.1.15")
    response = msg.payload.decode('utf-8')
    return(response)

def listener10():
    msg = subscribe.simple("aqi/sensor/particulate_matter_10m_concentration/state", auth = {'username':"agent", 'password':"passwd"}, hostname="10.1.1.15")
    response = msg.payload.decode('utf-8')
    return(response)

def listener100():
    msg = subscribe.simple("aqi/sensor/particulate_matter_100m_concentration/state", auth = {'username':"agent", 'password':"passwd"}, hostname="10.1.1.15")
    response = msg.payload.decode('utf-8')
    return(response)