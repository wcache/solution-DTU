import log

log.basicConfig(level=log.INFO)
logger = log.getLogger("dtu")


# ota 升级优化
# 新增系统日志上报功能
class RET:
    OK = "20000"
    HTTP_OK = "20001"
    MQTT_OK = "20002"
    SOCKET_TCP_OK = "20003"
    SOCKET_UDP_OK = "20004"
    Aliyun_OK = "20005"
    TXyun_OK = "20006"
    # 系统组件错误
    SIMERR = "3001"
    DIALINGERR = "3002"
    # 网络协议错误
    HTTPERR = "4001"
    REQERR = "4002"
    TCPERR = "4003"
    UDPERR = "4004"
    MQTTERR = "4005"
    ALIYUNMQTTERR = "4006"
    TXYUNMQTTERR = "4007"
    PROTOCOLERR = "4008"
    REQERR1 = "4009"
    QUECIOTERR = "4010"
    HWYUNERR = "4011"
    REQERR2 = "5000"
    # 功能错误
    PASSWORDERR = "5001"
    PASSWDVERIFYERR = "5002"
    HTTPCHANNELPARSEERR = "5003"
    CHANNELERR = "5004"
    DATATYPEERR = "5005"
    METHODERR = "5006"
    DATASENDERR = "5007"
    IOTTYPERR = "5008"
    NUMBERERR = "5009"
    MODBUSERR = "5010"
    # 解析错误
    JSONLOADERR = "6001"
    JSONPARSEERR = "6002"
    PARSEERR = "6003"
    DATAPARSEERR = "6004"
    POINTERR = "6005"
    READFILEERR = "6006"
    CONFIGNOTEXIST = "6007"
    # 提醒
    CMDPARSEERR = "7001"


error_map = {
    RET.OK: u"成功",
    RET.HTTP_OK: u"http connect success",
    RET.MQTT_OK: u"mqtt connect success",
    RET.SOCKET_TCP_OK: u"tcp connect success",
    RET.SOCKET_UDP_OK: u"udp connect success",
    RET.Aliyun_OK: u"aliyun connect success",
    RET.TXyun_OK: u"txyun connect success",
    # 系统
    RET.SIMERR: u"read sim card error",
    RET.DIALINGERR: u"dialing error",
    # 协议
    RET.HTTPERR: u"http request error",
    RET.REQERR: u"http request 500",
    RET.REQERR1: u"http request 302",
    RET.REQERR2: u"http request 404",
    RET.TCPERR: u"tcp connect failed",
    RET.UDPERR: u"udp connect failed",
    RET.MQTTERR: u"mqtt connect failed",
    RET.ALIYUNMQTTERR: u"aliyun connect failed",
    RET.TXYUNMQTTERR: u"txyun connect failed",
    RET.PROTOCOLERR: u"protocol parse error",
    RET.QUECIOTERR: u"quecthing connect failed",
    RET.HWYUNERR: u"huaweiyun connect failed",
    # 功能错误
    RET.PASSWORDERR: u"password not found",
    RET.PASSWDVERIFYERR: u"password verify error",
    RET.HTTPCHANNELPARSEERR: u"http param error",
    RET.CHANNELERR: u"through channel error",
    RET.DATATYPEERR: u"data type error",
    RET.METHODERR: u"method error",
    RET.DATASENDERR: u"through data send error",
    RET.IOTTYPERR: u"mqtt type error",
    RET.NUMBERERR: u"params number error",
    RET.MODBUSERR: u"modbus prase error",
    # 数据错误
    RET.JSONLOADERR: "json load err",
    RET.JSONPARSEERR: "json parse err",
    RET.PARSEERR: "parse error",
    RET.DATAPARSEERR: "data parse error",
    RET.POINTERR: "command code error",
    RET.READFILEERR: "read file error",
    # 提醒
    RET.CMDPARSEERR: "command parse error transfer to modbus"
}

class DTUException(Exception):
    def __init__(self, message):
        self.message = message