from diameter.AVP import AVP

class AVP_OctetString(AVP):
    """AVP containing arbitrary data of variable length."""

    def __init__(self,code=0,payload="",vendor_id=0):
        AVP.__init__(self,code,payload,vendor_id)

    def queryValue(self):
        """Returns the payload as a string (Python2: equal to bytes)"""
        return str(self.payload)

    def setValue(self,value):
        self.payload = str(value)

    def __str__(self):
        return AVP.str_prefix__(self) + " " + self.queryValue()

    @staticmethod
    def narrow(avp):
        """Convert generic AVP to AVP_OctetString
        """
        a = AVP_OctetString(avp.code, vendor_id=avp.vendor_id)
        a.flags = avp.flags
        a.payload = avp.payload
        return a

def _unittest():
    pass
